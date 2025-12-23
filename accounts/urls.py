from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, dashboard_view, profile_view, audit_log_view

urlpatterns = [
    # Registration
    path("register/", register_view, name="register"),

    # Login / Logout
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Dashboard & Profile
    path("dashboard/", dashboard_view, name="dashboard"),
    path("profile/", profile_view, name="profile"),

    # Admin-only Audit Log
    path("audit-log/", audit_log_view, name="audit_log"),
]
