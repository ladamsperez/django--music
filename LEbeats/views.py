from django.shortcuts import render

# Create your views here.
def album_list(request):
    return render(request, 'beats/album_list.html', {})