"""
server_ui specific views
"""

from helios.models import *
from heliosauth.security import *
from view_utils import *

import helios.views
import helios
from helios.crypto import utils as cryptoutils
from heliosauth.security import *
from helios.security import can_create_election

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotAllowed

from django.conf import settings

import copy
import heliosauth.views as auth_views

def get_election():
  return None

def home(request):
  # load the featured elections
  featured_elections = None

  user = get_user(request)
  create_p = can_create_election(request)
  elections_voted = None

  if not user:
    return HttpResponseRedirect('/')

  if user.superadmin_p:
    elections_administered = Election.objects.filter().select_related().order_by('-created_at').defer('encrypted_tally',
                                                                            'result')
  else:
    if create_p:
      elections_administered = Election.get_by_user_as_admin(user,
                                                             archived_p=None,
                                                             limit=None)
    else:
      elections_administered = None

    if user:
      elections_voted = Election.get_by_user_as_voter(user, limit=5)
    else:
      return HttpResponseRedirect("/auth/?return_url=/")
      elections_voted = None


    if user and not user.election:
      return HttpResponseRedirect(reverse("helios.views.election_new"))

  auth_systems = copy.copy(settings.AUTH_ENABLED_AUTH_SYSTEMS)
  try:
    auth_systems.remove('password')
  except: pass

  login_box = auth_views.login_box_raw(request, return_url="/", auth_systems=auth_systems)

  return render_template(request, "index", {'elections': featured_elections,
                                            'elections_administered' : elections_administered,
                                            'elections_voted' : elections_voted,
                                            'create_p':create_p,
                                            'login_box' : login_box})

def about(request):
  return HttpResponse(request, "about")

