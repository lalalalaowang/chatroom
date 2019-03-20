import tornado.web
from werkzeug.datastructures import MultiDict


class CommonHandler(tornado.web.RequestHandler):

    @property
    def params(self):
        data = self.request.arguments
        data = {
            k: list(
                map(lambda val: str(val, encoding='utf-8'), v)
            )
            for k, v in data.items()
        }
        return data

    def fdata(self):
        print(self.params)
        return MultiDict(self.params)
