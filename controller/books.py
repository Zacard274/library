import json

from flask import Blueprint, request

from orm import Pdb
from .base import json_success, before_request, current_user

books_bp = Blueprint('books', __name__)


# before_request = books_bp.before_request(before_request)


@books_bp.route('/', methods=['GET', 'POST'])
def index():
    # user = current_user
    # print(user)
    books = Pdb.book.get_all_books()
    return json_success(books)


@books_bp.route('/search', methods=['GET', 'POST'])
def search():
    keyword = request.args.get('keyword')
    param = eval(request.args.get('param'))

    books = Pdb.book.search_books(keyword, **param)
    if books:
        return json_success(books)
    return json_success(None)
