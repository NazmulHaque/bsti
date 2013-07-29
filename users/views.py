import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from users.models import user


import hashlib

from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.decorators.debug import sensitive_post_parameters
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils.http import cookie_date
# new utc
from django.utils.timezone import utc

from users.forms import LoginForm
from users.utils import get_session
# from modules.templatetags.module_tags import list_source_filters, list_topic_filters, list_article_filters

def home(request):
    return render(request, 'user/home.html')


@sensitive_post_parameters()
def login(request):
    """
    Displays the login form and handles the login action.
    """
    if request.user.is_authenticated():

        if request.method == "POST" and 'request_from' in request.POST \
            and request.POST.get('request_from','') and request.POST.get('request_from','') == 'popup':
            return  HttpResponse('true');

        if 'HTTP_REFERER' in request.META and request.META['HTTP_REFERER']:
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            return HttpResponseRedirect('/')
    if request.method == "POST":
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            is_valid_user = False

    #         if user:
    #             if user.is_staff or user.is_superuser:
    #                 is_valid_user = True
    #             else:
    #                 for group in user.groups.all():
    #                     if group.name == request.website.subdomain:
    #                         is_valid_user = True
    #                         break
            if is_valid_user:
                auth.login(request, user)
                response = HttpResponse('true')
                # Set cookies for varnish. If you are not using
                # varnish then you dont need to do this.
                # m = hashlib.md5()
                # m.update('%s-%s' % (user.email, settings.SECRET_KEY))
                # bstiuid = m.hexdigest()
                # expires = request.session.get_expiry_date()
                # response.set_cookie('BSTIUID', value=bstiuid, expires=expires)
                return response
            else:
                template = "user/home.html"
        else:
             template = "user/home.html"
    else:
        form = LoginForm()
        template = "user/home.html"
    return TemplateResponse(request, template, {'form': form})


# @login_required
# def logout(request):
#     session = get_session(request.COOKIES['sessionid'])
#     session.expire_date =  datetime.datetime.utcnow().replace(tzinfo=utc)
#     session.save()
#     user = request.user
#     # TODO: We need to track down website here.
#     page_editors = user.pageeditor_set.filter(ended_at=None)
#
#     for pe in page_editors:
#         #pe.ended_at = datetime.datetime.now().replace(tzinfo=None)
#         # new utc
#         pe.ended_at = datetime.datetime.utcnow().replace(tzinfo=utc)
#         pe.save()
#     auth.logout(request)
#
#     if 'HTTP_REFERER' in request.META and request.META['HTTP_REFERER']:
#         response = HttpResponseRedirect(request.META['HTTP_REFERER'])
#     else:
#         response = HttpResponseRedirect('/')
#
#     response.delete_cookie('BSTIUID')
#     return response
