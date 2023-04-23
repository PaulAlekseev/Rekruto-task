from django.http import HttpResponse, Http404


def greeting(request):
    name = request.GET.get('name')
    message = request.GET.get('message')

    if name is None or message is None:
        raise Http404("You need to specify name and message parameters")
    response = f"Hello, {name}! {message}"
    return HttpResponse(response)
