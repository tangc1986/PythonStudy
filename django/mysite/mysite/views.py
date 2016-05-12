from django.http import HttpResponse, Http404
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = ['<tr><td>%s</td><td>%s</td></tr>' % ('request.path', request.path),
            '<tr><td>%s</td><td>%s</td></tr>' % ('request.get_host()', request.get_host()),
            '<tr><td>%s</td><td>%s</td></tr>' % ('request.get_full_path()', request.get_full_path()),
            '<tr><td>%s</td><td>%s</td></tr>' % ('request.is_secure()', str(request.is_secure())),
            ]
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

