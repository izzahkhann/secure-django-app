from django.contrib.auth.signals import user_login_failed
from tasks.models import AuditLog

def log_failed_login(sender, credentials, request, **kwargs):
    username = credentials.get('username')
    AuditLog.objects.create(user=None, action=f"Failed login attempt: {username}")

user_login_failed.connect(log_failed_login)
