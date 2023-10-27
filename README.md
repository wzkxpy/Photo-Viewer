# Photo-Viewer

基于Python Flask框架的网页端照片浏览器。

可上传本地照片并查看，能够展示照片拍摄时间地点信息。

运行前请在config.py文件中补充入数据库相关信息。

经纬度到地址名称的转换调用了百度地图的api，请在func.py文件的getTrueAddress方法中填入您申请的百度地图开发者ak

申请链接https://lbsyun.baidu.com/apiconsole/key/create#/home

项目所需环境文件requirements.txt，可使用如下命令安装环境

`pip install -r requirements.txt`
