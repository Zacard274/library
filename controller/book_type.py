import json
from flask import request, Blueprint
from orm import Pdb
from .base import json_success

book_type_db = Blueprint('book_type', __name__)


@book_type_db.route('/search/')
def search():
    param = request.args.get('param')  #request.querystring
    if isinstance(param, str):
        json.loads(param)

    book_type = Pdb.book_type.search_types(param)
    return json_success(book_type)
