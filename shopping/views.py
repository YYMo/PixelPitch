from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers


import shopping.models as m

# Create your views here.

def index(request):
    return redirect('/artists')

def artist_view(request):
    template = 'artist_profile.html'
    id = request.GET['id']
    context = {"id": id}
    return render(request, template, context)

def artist_list_view(request):
    template = 'artist_list.html'
    context = {}
    return render(request, template, context)

def item_view(request):
    template = 'item.html'
    id = request.GET['id']
    context = {
        "id": id,
        "item": m.Item.objects.get(id=id).jsObject(),
    }
    return render(request, template, context)

def get_artist_list(request):
    fake_artist_list = [
        {
            "name":"artist one",
            "description":" asdfas asdf asdf asdf adf ",
        },
        {
            "name":"artist two",
            "description": "sfasbaegndlvnoewi isafnkasjnawehegf sdnf asdf",
        },
    ]

    artists = m.Artist.objects.filter(active=True)
    artists_list = []
    for artist in artists:
        print artist
        artists_list.append(artist.jsObject())

    data = {
        "artists": artists_list,
    }
    return JsonResponse(data)

def get_artist_profile(request):
    id = request.GET['id']
    a = m.Artist.objects.get(id=id)
    its = m.Item.objects.filter(creator=a)
    
    items = []
    for it in its:
        items.append(it.jsObject())

    artist = {
        "id": a.id,
        "nickname": a.nick_name,
        "description": a.description,
        "img_url": a.avatar,
        "items": items,
        "one_sentence_description": a.one_sentence_description,
        "title": a.description_title,

    }
    return JsonResponse(artist)

def get_item_info(request):
    id = request.GET['id']
    a = m.Item.objects.get(id=id)
    item = a.jsObject()
    return JsonResponse(item)