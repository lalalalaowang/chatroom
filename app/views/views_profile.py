import tornado.web


class ProfileHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        data = dict(
            title='用户信息',
        )
        self.render('userprofile.html', data=data)
