from flask import Blueprint, render_template
from model import Image

bp = Blueprint('order', __name__, url_prefix='/')


@bp.route('/')
def idDesc():
    id_desc = Image.query.order_by(Image.id.desc()).all()  # 默认
    return render_template('index.html', images=id_desc)


@bp.route('/id_asc')
def idAsc():
    id_asc = Image.query.all()
    return render_template('index.html', images=id_asc)


@bp.route('/time_asc')
def timeAsc():
    time_asc = Image.query.order_by(Image.datetime).all()
    return render_template('index.html', images=time_asc)


@bp.route('/time_desc')
def timeDesc():
    time_desc = Image.query.order_by(Image.datetime.desc()).all()
    return render_template('index.html', images=time_desc)


@bp.route('/address')
def addressAsc():
    address_asc = Image.query.order_by(Image.address).all()
    return render_template('index.html', images=address_asc)
