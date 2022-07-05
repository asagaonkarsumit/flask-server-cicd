import calendar
import time
import uuid
from http import HTTPStatus
import os
import random
import subprocess
from subprocess import PIPE
import requests
from werkzeug.exceptions import BadRequest

from app.main import config
from app.main.config import ssl_logger

from flask import current_app as cur_app


def save_content(data):

    return {"status": "hello sumitdddd11"}


def check_ssl_status(fqdn):
    ssl_active = True
    try:
        req = requests.get(f'https://{fqdn}/')
    except requests.exceptions.SSLError as e:
        ssl_active = False
        ssl_logger.exception(f"ssl is not active for this fqdn -- {fqdn}")
    except Exception as e:
        ssl_logger.exception(
            f"exception while check ssl status i function-- {fqdn}")

    print("sumit")
    # return {"item": "hello"}, HTTPStatus.CREATED.value
    return {"status": True}


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
