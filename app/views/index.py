from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('fitzme/index.html')
    context = {
        'user': request.user,
    }
    return HttpResponse(template.render(context, request))