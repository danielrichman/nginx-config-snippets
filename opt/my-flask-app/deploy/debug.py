#!/opt/my-flask-app/venv/bin/python

import os
import logging
from my_project import app

app.secret_key = os.urandom(16)
app.config['TRAP_BAD_REQUEST_ERRORS'] = True

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter("%(levelname)s %(name)s: %(message)s"))

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(handler)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
