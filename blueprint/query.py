from datetime import datetime
from flask import Blueprint, request, render_template
from model import Image

bp = Blueprint('query', __name__, url_prefix='/')


@bp.route('/addressQuery')
def addressQuery():
    address = request.args.get('address', default='', type=str)
    images = Image.query.filter(Image.address.like('%' + address + '%')).all()
    return render_template('index.html', images=images)


@bp.route('/timeQuery')
def timeQuery():
    start_time = request.args.get('start_time', default='', type=str)
    end_time = request.args.get('end_time', default='', type=str)
    start_time = datetime.strptime(start_time, '%Y-%m-%d')
    end_time = datetime.strptime(end_time, '%Y-%m-%d')
    images = Image.query.filter(Image.datetime > start_time, Image.datetime < end_time).all()
    return render_template('index.html', images=images)
