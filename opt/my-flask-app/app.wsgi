import logging
import flask
from logging.handlers import SysLogHandler, SMTPHandler
from notam import app

app.secret_key = "something-secret"
app.config['EMAIL_TO'] = ["you@domain.co.uk"]
app.config['EMAIL_FROM'] = "my-flask-app@domain.co.uk"
app.config['EMAIL_SERVER'] = "localhost"

_format_string = "my-flask-app: %(name)s %(levelname)s %(message)s"
# see /etc/rsyslog.d/100-wsgi-apps.conf
syslog_handler = SysLogHandler(facility=SysLogHandler.LOG_LOCAL5,
                               address="/dev/log")
syslog_handler.setLevel(logging.INFO)
syslog_handler.setFormatter(logging.Formatter(_format_string))

# https://gist.github.com/danielrichman/5892462
class FlaskFormatter(logging.Formatter):
    def format(self, record):
        s = super(FlaskFormatter, self).format(record)
        try:
            if flask.has_request_context():
                if s[-1:] != "\n":
                    s = s + "\n"
                s += self.formatRequest(flask.request, flask.session)
        except:
            pass
        return s

    def formatRequest(self, request, session):
        bits = ["\nFlask Request: {r.method} {r.base_url!r}\n"
                "endpoint {r.endpoint}\n\n"
                    .format(r=request)]

        def dump_dict(bits, key, items):
            bits.append("{0}:\n".format(key))
            bits += ["    {0!r}: {1!r}\n".format(k, v) for k, v in items]
            bits.append("\n")

        dump_dict(bits, "args", request.args.iteritems(True))
        dump_dict(bits, "form", request.form.iteritems(True))
        dump_dict(bits, "cookies", request.cookies.iteritems())
        dump_dict(bits, "headers", request.headers.iteritems())
        dump_dict(bits, "session", session.iteritems())

        bits.append("data:\n    {0}".format(request.data))

        return ''.join(bits)

_format_email = \
"""%(levelname)s from logger %(name)s

Time:       %(asctime)s
Location:   %(pathname)s:%(lineno)d
Module:     %(module)s
Function:   %(funcName)s

%(message)s"""
mail_handler = SMTPHandler(app.config['EMAIL_SERVER'],
                           app.config['EMAIL_FROM'],
                           app.config['EMAIL_TO'],
                           "my-flask-app error logger")
mail_handler.setLevel(logging.ERROR)
mail_handler.setFormatter(FlaskFormatter(_format_email))

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(syslog_handler)
root_logger.addHandler(mail_handler)

application = app
