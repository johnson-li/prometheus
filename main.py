from flask import Flask
from api.ping import ping_api

app = Flask(__name__)

app.register_blueprint(ping_api)

if __name__ == '__main__':
    app.run()
