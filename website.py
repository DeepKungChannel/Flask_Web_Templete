from flask import Flask



def create_app():
    app = Flask(__name__, template_folder="public")
    app.config["SECRET_KEY"] = "klsdjfpoiuw29834*#$^()@#)$"
    
    from routes.home import home_blueprint

    app.register_blueprint(home_blueprint, url_prefix="/")
    
    return app