from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

def get_user_by_session_key(session_key):
    user = None
    try:
        session = Session.objects.get(session_key=session_key)
        uid = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(pk=uid)
    except:
        pass
    return user

def get_session(session_key):
    try:
        session = Session.objects.get(session_key=session_key)
    except:
        session = None
    return session