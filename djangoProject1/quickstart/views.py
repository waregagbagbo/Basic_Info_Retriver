from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

"""We will have to create viewsets to fetch data from our serializer"""