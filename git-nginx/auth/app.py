import base64
import crypt
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
    # Verify the accessing user with the password file
    try:
        if authorization := request.headers.get('Authorization'):
            if m := re.search('Basic (\S+)$', authorization):
                user, password = base64.b64decode(m.group(1)).decode(encoding='ascii').split(':')
                with open(passwordFile, mode='r', encoding='ascii') as f:
                    while line := f.readline():
                        # e.g. user:pass => line is user:$6$salt123$MhMr4gc.nIFOX9ZdA3KP4lSRB684iMcUE47pBxQENRYP6Um3vZ3yph28wOwI0nJ0Et.0bUMqLKr59jn67i9QF1
                        values = line.rstrip(os.linesep).split(':')
                        if values[0] == user:
                            expected = values[1]
                            # $6$salt123$... => $6$salt123
                            salt = '$'.join(expected.split('$')[:-1])
                            passwordHash = crypt.crypt(password, salt)
                            if passwordHash == expected:
                                return '', 200
                            break
    except:
        return '', 400
    return '', 401, {'WWW-Authenticate': 'Basic realm="Protected"'}


if __name__ == "__main__":
    app.run(port=3000)
