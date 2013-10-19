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
def logout(request):
    del request.session['officer_id']
    return redirect('/')

def home(request):
    try:
        if request.session['officer_id']:
            return redirect('/officer')
    except KeyError:
        if request.GET.get('login'):
            return login(request)
        else:
            return render(request, 'user/home.html')



def officer(request):
    try:
        if request.session['officer_id']:
            officer = user.objects.get(pk = request.session['officer_id'])
            print officer.name
            print officer.email
            return render(request, 'user/index.html', {'user': officer.name, 'email': officer.email, 'password':officer.password})
    except KeyError:
        return redirect('/')

