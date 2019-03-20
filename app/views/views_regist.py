from app.views.views_common import CommonHandler
from app.tools.forms import RegistForm
from app.models.crud import Crud


class RegistHandle(CommonHandler):

    def get(self, *args, **kwargs):
        data = dict(
            title='用户注册'
        )
        self.render('regist.html', data=data)

    def post(self, *args, **kwargs):
        data = self.fdata()
        form = RegistForm(data)
        res = dict(code='0')
        if form.validate():
            if Crud.save_regist_user(form):
                res['code'] = '1'
        else:
            res = form.errors
            res['code'] = '0'
        self.write(res)
