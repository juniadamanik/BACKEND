from rest_framework.decorators import api_view
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView

@api_view(["POST"])
def registerPage(request):
    if request.method == "POST":
        if "email" and "username" and "password" in request.data:
            User.objects.create_user(email=request.data["email"],username=request.data["username"],password=request.data["password"])
            return Response("Register Success")

@api_view(["POST"])
def loginPage(request):
    if request.method == "POST":
        username = request.data["username"]
        password = request.data["password"]
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return Response("Login success")
        else:
            return Response("Login Failed")

@api_view(["POST"])
@login_required
def logoutView(request):
    logout(request)
    return Response("Logged out")
