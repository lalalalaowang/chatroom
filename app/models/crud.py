from app.tools.orm import ORM
from app.models.models import User
from datetime import datetime
from werkzeug.security import generate_password_hash  # 用来生成加密的密码


def get_datetime():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class Crud:
    # 唯一性验证
    @staticmethod
    def user_unique(data, flag=1):
        session = ORM.db()
        user = None
        try:
            query = session.query(User)
            if 1 == flag:  # flag=1 检查用户名是否存在
                user = query.filter_by(name=data).first()
            if 2 == flag:  # flag=2 检查邮箱是否存在
                user = query.filter_by(email=data).first()
            if 3 == flag:  # flag=3 检查手机是否存在
                user = query.filter_by(phone=data).first()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        if user:
            return True
        else:
            return False

    @staticmethod
    def save_regist_user(form):
        session = ORM.db()
        flag = True
        try:
            user = User(
                name=form.data['name'],
                pwd=generate_password_hash(form.data['pwd']),
                email=form.data['email'],
                phone=form.data['phone'],
                sex=None,
                constellation=None,
                face=None,
                info=None,
                createAt=get_datetime(),
                updateAt=get_datetime(),
            )
            session.add(user)
        except Exception as e:
            session.rollback()
            flag = False
        else:
            session.commit()
        finally:
            session.close()
        return flag
