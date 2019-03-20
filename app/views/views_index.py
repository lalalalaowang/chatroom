import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("lalalalaowang")
        data = dict(
            title='视频列表'
        )
        self.render('index.html', data=data)
