from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Главная страница')

def group_posts(request):
    return HttpResponse('Записи групп')

def any_slug(request, slug):
    return HttpResponse(f'{slug}')