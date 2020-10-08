import logging
import os
import re

from flask import Flask, request


logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)


@app.route('/auth')
def route_auth():
    m = re.search('^/git/(.*\.git)', request.headers.get('X-Original-Uri'))
    if m is None:
        return '', 403
    repositoryDirectory = f'/opt/git/{m.group(1)}'
    passwordFile = f'{repositoryDirectory}/.git-nginx/passwd'
    app.logger.info(f"""{request.headers.get('X-Original-Uri')} => {passwordFile}""")
    if not os.path.isfile(passwordFile):
        return '', 200
    # TODO: Verify the accessing user with the password file
    return '', 401, {'WWW-Authenticate': 'Basic realm="Protected"'}


if __name__ == "__main__":
    app.run(port=3000)
