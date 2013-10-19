from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
# from django.contrib.sessions.models import Session
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist
from users.models import user

def login(request):
    try:
        if request.session['officer_id']:
            return redirect('/officer')
    except KeyError:
        try:
            email = request.POST['email']
            password = request.POST['password']

        except MultiValueDictKeyError:
            msg = 'Try with valid email & password'
            render(request, 'user/home.html', {'error_msg': msg})
        else:
            try:
                officer = user.objects.get(email = email)
            except ObjectDoesNotExist:
                msg = 'Try with valid email.'
                return render(request, 'user/home.html', {'error_msg': msg})
            else:
                user_password = officer.password
                if user_password == password:
                    request.session['officer_id'] = officer.id
                    return redirect('/officer')
                else:
                    msg = 'Try with valid password'
                    return render(request, 'user/home.html', {'error_msg': msg})

def registration(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']

    if name != '' and email != '' and password != '':
        try:
            officer = user.objects.get(email = email)
        except ObjectDoesNotExist:
            officer = user(name = name, email = email, password = password)
            officer.save()
            try:
                officer = user.objects.get(email = email)
            except ObjectDoesNotExist:
                msg = 'Try Later.'
            else:
                msg = 'Congratualtions!! Log in ...'
        else:
            msg = 'Email already exists. Try another ...'
    else:
        msg = 'Fill empty fields.'
    return render(request, 'user/home.html', {'reg_msg': msg,})



def logout(request):
    del request.session['officer_id']
    return redirect('/')

def home(request):
    try:
        if request.session['officer_id']:
            return redirect('/officer')
    except KeyError:
        if request.GET.get('login') == 'login':
            return login(request)
        elif request.GET.get('reg') == 'registration':
                return registration(request)
        else:
            return render(request, 'user/home.html')


def reset_password(request, officer):
    old_password = request.POST['old-password']
    new_password = request.POST['new-password']

    if officer.password == old_password:
        officer.password = new_password
        officer.save()
        if officer.password == new_password:
            msg = 'Your password changed successfully.'
            return msg
    else:
        msg = 'Enter correct current password.'
        return msg

def officer(request):
    try:
        if request.session['officer_id']:
            officer = user.objects.get(pk = request.session['officer_id'])
            if request.GET.get('reset') == 'password':
                msg = reset_password(request, officer)
            else:
                msg = ''

            return render(request, 'user/index.html', {'user': officer.name, 'email': officer.email, 'message':msg,})
    except KeyError:
        return redirect('/')

