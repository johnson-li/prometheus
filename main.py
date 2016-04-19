from flask import Flask
from api.ping import ping_api
from api.log import log_api
from api.static import static_api

app = Flask(__name__)

app.register_blueprint(ping_api)
app.register_blueprint(log_api)
app.register_blueprint(static_api)

if __name__ == '__main__':
    app.run()
