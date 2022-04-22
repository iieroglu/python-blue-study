from flask import Flask
import services.auth_service as auth_service

app = Flask(__name__)


@app.route('/')
def hello_world():
    app.logger.info('env: %s' % app.env)
    return 'hello world'


@app.route('/login')
def login():
    app.logger.info('abc: %s', app.name)
    as_obj = auth_service.AuthService()
    as_obj.check_password('')
    return 'auth successful'

