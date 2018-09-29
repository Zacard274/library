from flask import Blueprint, request
from orm import Pdb
import json

user_bp = Blueprint('user', __name__)

MOBILENUMBER_DUPLICATE = "the mobileNumber is duplicate"
PASSWORDS_DIFFER = "the two passwords do not match"
LOGIN_ERROR = "the mobileNumber and password do not match"


@user_bp.route('/regist/')
def regist():
    username = request.form.get('username')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    mobile_number = request.form.get('mobile_number')

    existed_mobile_number = Pdb.user.search_users({'mobileNumber': mobile_number})

    if existed_mobile_number:
        return json.dumps({'result_code': 'error', 'result_desc': MOBILENUMBER_DUPLICATE})
    else:
        if password1 != password2:
            return json.dumps({'result_code': 'error', 'result_desc': PASSWORDS_DIFFER})
        else:
            param = {'username': username, 'password': password1, 'mobileNumber': mobile_number}
            Pdb.user.add_users(param)
            return json.dumps({'result': 'success'})


@user_bp.route('/login/')
def login():
    mobile_number = request.form.get('mobile_number')
    password = request.form.get('password')

    user = Pdb.user.search_users({'password': password, 'mobileNumber': mobile_number})

    if user:
        return json.dumps({'result_code': 'success'})
    else:
        return json.dumps({'result_code': 'error', 'result_desc': LOGIN_ERROR})
