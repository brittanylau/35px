from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
# from django.template import loader
from django.shortcuts import render
from .models import Photo

# Create your views here.
def index(request):
    latest_photo_list = Photo.objects.order_by('-pub_date')[:5]
    context = { 'latest_photo_list': latest_photo_list }
    return render(request, 'feed/index.html', context)

def detail(request, photo_id):
    # try:
    #    photo = Photo.objects.get(pk=photo_id)
    # except Photo.DoesNotExist:
    #    raise Http404("Photo does not exist.")
    photo = get_object_or_404(Photo, pk=photo_id)
    return render(request, 'feed/detail.html', {'photo': photo})

def comment(request, photo_id):
    response = ("You're commenting on photo %s.")
    return HttpResponse(response % photo_id)

def post(request):
    return render(request, 'feed/post.html')
