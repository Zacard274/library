import json
from flask import Blueprint, request
import pymysql
from orm import Pdb
from .base import json_fail, json_success

user_bp = Blueprint('user', __name__)

INPUT_ILLEGAL = "the input information is duplicate"
PASSWORDS_DIFFER = "the two passwords do not match"
LOGIN_ERROR = "the mobileNumber and password do not match"
PARAM_ERROR = "parameter is invalid"


class RegisterItem(object):
    def __init__(self):
        self.username = request.form.get('username')
        self.password1 = request.form.get('password1')
        self.password2 = request.form.get('password2')
        self.mobile_number = request.form.get('mobile_number')

    def check_param(self):
        if all([self.username, self.password1, self.password2, self.mobile_number]):
            if self.password1 != self.password2:
                return False, PASSWORDS_DIFFER
            else:
                return True, ''
        return False, PARAM_ERROR


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    req_item = RegisterItem()
    is_param_valid, msg = req_item.check_param()
    if not is_param_valid:
        return json_fail(msg)

    existed_mobile_number = Pdb.user.search_users({'mobileNumber': req_item.mobile_number})
    existed_username = Pdb.user.search_users({'username': req_item.username})

    if any([existed_mobile_number, existed_username]):
        return json_fail(INPUT_ILLEGAL)

    param = {'username': req_item.username, 'password': req_item.password1, 'mobileNumber': req_item.mobile_number}
    try:
        Pdb.user.add_users(param)
    except pymysql.err.IntegrityError as e:
        return json_fail(e)

    return json_success('')


class LoginItem(object):
    def __init__(self):
        self.mobile_number = request.form.get('mobile_number')
        self.password = request.form.get('password')

    def check_param(self):
        if all([self.mobile_number, self.password]):
            return True, ''

        return False, PARAM_ERROR


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    login_item = LoginItem()
    is_param_valid, msg = login_item.check_param()
    if not is_param_valid:
        return json_fail(msg)

    user = Pdb.user.search_users({'password': login_item.password, 'mobileNumber': login_item.mobile_number})

    if user:
        return json_success('')

    return json_fail(LOGIN_ERROR)
