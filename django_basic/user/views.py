from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User

def home(request):
    user_id = request.session.get('user')

    if user_id:
        user = User.objects.get(pk=user_id)
        return HttpResponse(user.username)

    return HttpResponse('Home!')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')
    

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not (username and password):
            res_data['error'] = '모든 값을 입력해야합니다.'
        else:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                # 비밀번호가 일치, 로그인 처리를!
                # 세션!
                request.session['user'] = user.id
                return redirect('/')
            else:
                res_data['error'] = '비밀번호를 틀렸습니다.'

        return render(request, 'login.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user = User(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )

            user.save() 

        return render(request, 'register.html', res_data)