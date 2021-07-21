from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Album
from .forms import AlbumForm
from django.shortcuts import redirect



def album_list(request):
    albums = Album.objects.filter(date_added__lte=timezone.now()).order_by('date_added')
    return render(request, 'beats/album_list.html', {'albums': albums})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'beats/album_detail.html', {'album': album})

def album_new(request, pk):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.artist = request.user
            album.date_added = timezone.now()
            album.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm()
    return render(request, 'beats/album_edit.html', {'form': form})

def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save(commit=False)
            album.author = request.user
            album.date_added = timezone.now()
            album.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'beats/album_edit.html', {'form': form})
