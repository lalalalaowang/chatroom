import tornado.web


class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        data = dict(
            title='用户登录'
        )
        self.render('login.html', data=data)
