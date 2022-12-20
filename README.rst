flask-json-db
=============

A flask extension to log a variable value inside view in a JSON file


Installation
============

For stable version 
   - pip install flask-json-db

For developement 
   - git clone https://github.com/Agent-Hellboy/flask-json-db
   - cd flask-json-db
   - python -m venv .venv 
   - source .venv/bin/activate

Example
=======

.. code:: py

    from flask import Flask
    from flask_json_db import JSONDB

    app = Flask(__name__)
    app.config["JSONFILE"] = "custom.json" #optional 
    json_db = JSONDB(app)

    @app.route('/')
    def hello_world():
        json_db.write({"landing_view_var":"landing_view_var_value"})
        return 'Hello World'

    @app.route("/home")
    def home():
        json_db.write({"home_var":["jshajdhjs"]})
        return 'ghj'

    @app.route("/new_home")
    def new_home():
        db.write({"new_home_var": "new_home_var_value"})
        return "hjk"

    if __name__ == '__main__':
        app.run()


 open the custom.json and get to know about these variable values

General Info
============

   - I don't know how can it be helpful but it is helpful for me :)

   
Contributing
============

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
