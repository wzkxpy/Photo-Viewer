from flask import Blueprint, request, url_for, redirect
from exts import db
from model import Image
from func import saveImg, getImgExif

bp = Blueprint('post', __name__, url_prefix='/post')


@bp.route('/add', methods=['POST'])
def imgAdd():
    # 获取图片文件
    file = request.files.get('file')
    # 储存文件,返回新文件名
    new_filename = saveImg(file)
    # 获取相关信息,存入数据库
    exif = getImgExif(new_filename)
    image = Image(url=new_filename)
    if exif['date_time'] != 'null':
        image.datetime = exif['date_time']
    if exif['address'] != 'null':
        image.address = exif['address']
    db.session.add(image)
    db.session.commit()
    print(123)
    return '图片上传成功'


@bp.route('/address', methods=['POST'])
def addressPost():
    address = request.form['address']
    return redirect(url_for('query.addressQuery', address=address))


@bp.route('/time', methods=['POST'])
def timePost():
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    return redirect(url_for('query.timeQuery', start_time=start_time, end_time=end_time))
