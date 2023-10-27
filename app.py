import config
from exts import db
from flask import Flask
from blueprint.post import bp as post_bp
from blueprint.query import bp as query_bp
from blueprint.order import bp as order_bp


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
# 注册蓝图
app.register_blueprint(post_bp)
app.register_blueprint(query_bp)
app.register_blueprint(order_bp)
# 创建数据库
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run()
