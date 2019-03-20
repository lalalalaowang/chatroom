from app.views.views_index import IndexHandler as index
from app.views.views_playchat import PlayChatHandle as play_chat
from app.views.views_regist import RegistHandle as regist
from app.views.views_login import LoginHandler as login
from app.views.views_profile import ProfileHandler as profile

urls = [
    (r'/', index),
    (r'/playchat/', play_chat),
    (r'/regist/', regist),
    (r'/login/', login),
    (r'/profile/', profile),
]
