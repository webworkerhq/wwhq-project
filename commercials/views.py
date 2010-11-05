# Create your views here.
from django.http import HttpResponse
from django.template import Template, Context
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    t = Template("Hello {{ person }}")
    d = Context({"person":"fernando"})
    return HttpResponse(t.render(d))
