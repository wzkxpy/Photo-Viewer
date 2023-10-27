import os

# 路径信息
basedir = os.path.abspath(os.path.dirname(__file__))  # 当前项目的绝对路径
UPLOAD_FOLDER = basedir + '\\static\\image'

# 数据库配置信息
HOSTNAME = 'localhost'
PORT = '3306'
USERNAME = ''  # mysql用户名
PASSWORD = ''  # mysql密码
DATABASE = '' # 数据库名称
DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
SQLALCHEMY_DATABASE_URI = DB_URI

