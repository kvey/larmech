from django.shortcuts import render
from core.models import (PartListing, )

from django.shortcuts import render_to_response,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.forms.formsets import formset_factory
from django import forms
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.template import RequestContext, loader, Context

# Create your views here.

def home(request):
    return all_items(request)

def all_items(request):
    return render_to_response("all_parts.html", {
        "parts": PartListing.objects.all()
        }, context_instance=RequestContext(request))

def item_detail(request):
    return render_to_response("detail_part.html", {
        "parts": PartListing.objects.get(request.GET['part'])
        }, context_instance=RequestContext(request))
