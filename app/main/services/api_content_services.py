import calendar
import time
import uuid
from http import HTTPStatus

from werkzeug.exceptions import BadRequest

from app.main import config

from flask import current_app as cur_app


def save_content(data):
    print("sumit")
    return "ddd"   # return {"item": "hello"}, HTTPStatus.CREATED.value


def get_all(page, limit):
    print("hello")
    return "dsd", HTTPStatus.OK.value


def delete_content(id):
    try:
        print("hello")
        # return {
        #     "message": "article deleted successfully.",
        # }, HTTPStatus.OK.value
    except:
        print("jee")
        # return {"message": "article does not exists."}, HTTPStatus.OK.value
