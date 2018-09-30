import json
from flask import Blueprint, request
from orm import Pdb
from .base import json_success

city_bp = Blueprint('city', __name__)


@city_bp.route('/search', methods=['GET', 'POST'])
def search():
    param = request.args.get('param')
    if isinstance(param, str):
        param = json.loads(param)

    city = Pdb.city.search_city(param)
    return json_success(city)
