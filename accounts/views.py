from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import RegisterForm
from tasks.models import Task, AuditLog

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

@login_required
def dashboard_view(request):
    if request.user.is_superuser:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(user=request.user)
    
    return render(request, "accounts/dashboard.html", {"tasks": tasks, "is_admin": request.user.is_superuser})

@login_required
def profile_view(request):
    user_tasks = Task.objects.filter(user=request.user)
    return render(request, "accounts/profile.html", {"user_tasks": user_tasks, "user": request.user})

@staff_member_required
def audit_log_view(request):
    logs = AuditLog.objects.all().order_by('-timestamp')
    return render(request, "accounts/audit_log.html", {"logs": logs})
