from django.http import HttpResponse


def home(request):
    return HttpResponse("Basufka is running!")
