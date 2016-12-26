from app.models import Followers
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout


def home(request):
    if request.user.is_authenticated():
        followers = Followers.objects.filter(user=request.user)
    else:
        followers = []
    return render(request, 'home.html', {'followers': followers})


def login(request):
    return render(request, 'login.html', {'request': request, 'user': request.user})


def logout(request):
    auth_logout(request)
    return redirect('/')


def follower(request, id):
    follower = Followers.objects.get(id_str=id)
    return render(request, 'follower.html', {'follower': follower})


def search(request):
    q = request.POST.get('q')
    result = Followers.objects.filter(screen_name__istartswith=q)
    message = str(result.count()) + ' found!'
    return render(request, 'home.html', {'followers': result, 'q': q, 'message': message})
