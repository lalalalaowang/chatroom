import tornado.web


class PlayChatHandle(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        data = dict(
            title='弹幕视频',
        )
        self.render('playchat.html', data=data)
