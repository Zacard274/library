from flask import Blueprint
from orm import Pdb
import json
import datetime

books_bp = Blueprint('books', __name__)


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


@books_bp.route('/')
def index():
    books = Pdb.book.get_all_books()
    return json.dumps(books, cls=DateEncoder)

