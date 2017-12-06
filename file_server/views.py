import mimetypes

from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist

from file_server.models import File


def get_content_type(name):
    content_type = mimetypes.guess_type(name)[0]
    if not content_type:
        if name.endswith('.svg'): content_type = 'image/svg+xml'
        if name.endswith('.woff'): content_type = 'application/font-woff'
        if name.endswith('.ttf'): content_type = 'application/x-font-ttf'
        if name.endswith('.otf'): content_type = 'application/x-font-ttf'
        if name.endswith('.svgf'): content_type = 'image/svg+xml'
        if name.endswith('.eot'): content_type = 'application/vnd.ms-fontobject'
    return content_type

def serve(request, path):
    try:
        f = File.objects.get(path=path)
    except ObjectDoesNotExist:
        return HttpResponseNotFound()

    response = HttpResponse()
    response['Content-Type'] = get_content_type(path)
    response.write(f.content)
    return response
