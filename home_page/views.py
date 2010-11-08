# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse
# The messages framework will only be available from django 1.2 onwards. Since
# most people are still using <= 1.1.1, we fallback on the backported message
# framework:
try:
    from django.contrib import messages
except ImportError:
    import django_messages_framework as messages #backport of messages framework

from .forms import ProfileForm

@login_required
def profile(request):
    '''
    Displays page where user can update their profile.
    
    @param request: Django request object.
    @return: Rendered profile.html.
    '''
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print data

            #Update user with form data
            request.user.first_name = data['first_name']
            request.user.last_name = data['last_name']
            request.user.email = data['email']
            request.user.save()

            messages.success(request, 'Successfully updated profile!')
    else: 
        #Try to pre-populate the form with user data.
        form = ProfileForm(initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        })

    return render_to_response('app/profile.html', {
                                'form': form,
                                'user': request.user,
                              },
                              context_instance = RequestContext(request))