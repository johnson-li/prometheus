from flask import Flask
from flask_compress import Compress
# from api.ping import ping_api
# from api.log import log_api
# from api.static import static_api
from mongoapi.log import mongo_log_api

app = Flask(__name__)
Compress(app)

# app.register_blueprint(ping_api)
# app.register_blueprint(log_api)
# app.register_blueprint(static_api)
app.register_blueprint(mongo_log_api)

if __name__ == '__main__':
    app.run()
