import json
from flask import Blueprint, request
from orm import Pdb
from .base import json_success

books_bp = Blueprint('books', __name__)


@books_bp.route('/', methods=['GET', 'POST'])
def index():
    books = Pdb.book.get_all_books()
    return json_success(books)


@books_bp.route('/search', methods=['GET', 'POST'])
def search():
    param = request.args.get('param')
    # print(dir(request))
    if isinstance(param, str):
        # 如果前端给到的是json，需要先转成dict
        param = json.loads(param)

    books = Pdb.book.search_books(param)
    return json_success(books)
