from django.views import generic
from .models import Album, Song
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from  django.urls import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    # model = Album
    context_object_name = 'all_albums'


    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(generic.UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(generic.DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')
