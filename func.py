import exifread
from datetime import datetime
import config
import time
import requests


# 通过经纬度获取地址,调用百度地图API
def getTrueAddress(latitude, longitude):
    url = "https://api.map.baidu.com/reverse_geocoding/v3"
    ak = "Hrf5RG7vxBeo4nI5hPvqLx6BodxQTuNK"
    location = str(latitude) + ',' + str(longitude)
    params = {
        "ak": ak,
        "output": "json",
        "location": location,
    }
    response = requests.get(url=url, params=params)
    if response:
        response = response.json()
        return response['result']['formatted_address']


# 储存照片文件
def saveImg(file):
    file_name = file.filename
    ext = file_name.rsplit('.', 1)[1]  # 文件后缀
    unix_time = int(time.time())
    new_filename = str(unix_time) + '.' + ext  # 修改文件名
    file_dir = config.UPLOAD_FOLDER + '\\' + new_filename
    file.save(file_dir)
    return new_filename


# 获取照片exif信息
def getImgExif(filename):
    file_dir = "./static/image/" + filename
    file = open(file_dir, 'rb')
    tags = exifread.process_file(file)
    file.close()
    date_time = 'null'
    address = 'null'
    if 'Image DateTime' in tags:
        date_time = tags['Image DateTime']
        date_time = datetime.strptime(date_time.values, '%Y:%m:%d %H:%M:%S')
    if 'GPS GPSLatitudeRef' in tags and 'GPS GPSLongitudeRef' in tags:
        ns_ref = tags['GPS GPSLatitudeRef'].values  # S / N
        ew_ref = tags['GPS GPSLongitudeRef'].values  # E / W
        latitude = tags['GPS GPSLatitude'].values  # 纬度
        longitude = tags['GPS GPSLongitude'].values  # 经度
        latitude = float(latitude[0] + latitude[1] / 60 + latitude[2] / 3600)
        longitude = float(longitude[0] + longitude[1] / 60 + longitude[2] / 3600)
        if ns_ref == 'S':
            latitude = -latitude  # 南纬记为负
        if ew_ref == 'W':
            longitude = -longitude  # 西经记为负
        address = getTrueAddress(latitude, longitude)
    return {'date_time': date_time, 'address': address}
