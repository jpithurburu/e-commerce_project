import os

from flask import Flask

def create_app(test_config=None):
    #Create a config the application
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'e-commerce.sqlite')
    )

    if test_config is None:
        #loading config instance is there is one when not testing
        app.config.from_pyfile('config.py', silent = True)
    else:
        #loading the test config
        app.config.from_mapping(test_config)
    
    #Check the instance folder existence
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    import db,auth
    db.init_app(app)
    app.register_blueprint(auth.bp)
    

    return app