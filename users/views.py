from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist
from users.models import user

def home(request):
    return render(request, 'user/home.html')

def login(request):
    try:
        email = request.POST['email']
        password = request.POST['password']

    except MultiValueDictKeyError:
        msg = 'Try with valid email & password'
        return redirect('/', {'error_msg': msg})

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
                return render(request, 'user/index.html', {'user': officer.name, 'email': officer.email, 'password':officer.password})
            else:
                msg = 'Try with valid password'
                return render(request, 'user/home.html', {'error_msg': msg})

