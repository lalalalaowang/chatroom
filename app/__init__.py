import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options
import logging

from .configs import configs
from .urls import urls

# 设置运行端口的配置
define('port', type=int, default=8080, help='运行端口')


class CustomApplication(tornado.web.Application):
    def __init__(self):
        settings = configs  # 导入配置
        handlers = urls  # 导入urls
        super(CustomApplication, self).__init__(handlers=handlers, **settings)  # 调用父类方法创建application


def create_http_server():
    tornado.options.parse_command_line()  # 可从命令行读取配置
    http_server = tornado.httpserver.HTTPServer(CustomApplication())
    http_server.listen(options.port)  # 监听端口
    tornado.ioloop.IOLoop.instance().start()  # 开启循环
