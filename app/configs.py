import os

bash_path = os.path.dirname(__file__)

configs = dict(
    debug=True,  # 配置是否开启debug模式
    static_path=os.path.join(bash_path, 'static'),  # 指定静态文件目录
    template_path=os.path.join(bash_path, 'templates'),  # 指定模板目录
    xsrf_cookies=True,  # 开启xsrf保护
    cookie_secret='5906a71156114b71b30f9296afdd2f14  '  # 设置xsrf密钥
)

db_configs = dict(
    host='127.0.0.1',
    port='3306',
    name='chatroom',
    user='root',
    password='111222aA',
)
