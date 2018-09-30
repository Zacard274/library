import json
from flask import request, Blueprint
from orm import Pdb
from .base import json_success

book_type_db = Blueprint('book_type', __name__)


@book_type_db.route('/search', methods=['GET', 'POST'])
def search():
    param = request.args.get('param')
    if isinstance(param, str):
        param = json.loads(param)

    book_type = Pdb.book_type.search_types(param)
    return json_success(book_type)
