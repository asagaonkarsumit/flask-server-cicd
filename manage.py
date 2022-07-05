import os
import sys
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


from app import blueprint
from app.main import create_app
from flask_cors import CORS


app = create_app('test')
CORS(app, resources={r"/": {"origins": "*"}})

app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    app.run(port=5001)


if __name__ == '__main__':
    manager.run()
