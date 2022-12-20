import json
import os

from flask import current_app
from flask import _app_ctx_stack as app_stack
from flask import _request_ctx_stack as req_stack


class JSONDB:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("JSONFILE", "flask_json.json")
        self.j_data = {}
        self.num = 0
        if hasattr(app, "teardown_appcontext"):
            app.teardown_appcontext(self.app_teardown)
        else:
            app.teardown_request(self.req_teardown)

    def write(self, data):
        self.f = open(current_app.config["JSONFILE"], "w")
        self.num += 1
        self.j_data[self.num] = data
        json.dump(self.j_data, self.f)

    def app_teardown(self, exception):
        if exception:
            self.num += 1
            self.j_data[self.num] = "got a pythonic exception"
            json.dump(self.j_data, self.f)
