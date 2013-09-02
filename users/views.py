# import datetime
from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
# from django.views import generic
#
# from users.models import user
#
#
# import hashlib
#
# from django.contrib import auth
# from django.http import HttpResponse, HttpResponseRedirect
# from django.template.response import TemplateResponse
# from django.views.decorators.debug import sensitive_post_parameters
# from django.template import RequestContext
# from django.contrib.auth.decorators import login_required
# from django.conf import settings
# from django.utils.http import cookie_date
# new utc
# from django.utils.timezone import utc
# from users.utils import get_session
# from modules.templatetags.module_tags import list_source_filters, list_topic_filters, list_article_filters

def home(request):
    return render(request, 'user/home.html')

