from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Artist
from .forms import AlbumForm




def album_list(request):
    albums = Album.objects.all()
    return render(request, 'beats/album_list.html', {'albums': albums})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'beats/album_detail.html', {'album': album})


def album_new(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm()
    return render(request, 'beats/album_edit.html', {'form': form})
    
def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'beats/album_edit.html', {'form': form})

def artist_page(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'beats/artist_page.html', {'artist': artist})
    
def create_artist(request):
    if request.method == "POST":
        form = AlbumForm()
        return render(request, 'beats/create_artist.html', {'form':form})
    elif request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            title =form.data['title']
            artist =form.data['artist']
            year = form.data['year']
            validated_artist = Artist.objects.get_or_create(artist=artist)[0]
            album = Album.objects.create(artist=validated_artist, title=title, year=year)
            album.save()
            return redirect('album_list', pk=album.pk)

def album_delete(request, pk):
    album_to_delete = get_object_or_404(Album, pk=pk)
    album_to_delete.delete()
    return redirect('album_list')

# from .models import Album, Artist
# from .forms import AlbumForm, AlbumArtistForm, OrderByForm




