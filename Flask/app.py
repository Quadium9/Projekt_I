from flask import Flask
from API.star import field
from API.user import user_api
from API.constellation import constellation_api

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = b'\xaa\x89u\xf7M\xf03\xcb\x1b\xc6#\xd2"\x8b\xf8\xb7'


app.register_blueprint(field, url_prefix='/star')
app.register_blueprint(user_api, url_prefix='/user')
app.register_blueprint(constellation_api, url_prefix='/constellation')

if __name__ == '__main__':
    app.run()
