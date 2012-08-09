from django.shortcuts import render_to_response 
from django.template import RequestContext

# Create your views here.
def main(request):
    return render_to_response('main.html', {}, context_instance=RequestContext(request))

def members(request):
    return render_to_response('main.html', {"path": request.path}, context_instance=RequestContext(request))

def join(request):
    return render_to_response('main.html', {"path": request.path}, context_instance=RequestContext(request))

def contact(request):
    return render_to_response('main.html', {"path":request.path}, context_instance=RequestContext(request))
