# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import Context, loader
from util import HttpUtil
from django.http import HttpResponse
# Create your views here.


def joke(req):
    jokes = HttpUtil.getJokes('-1')
    lastid = jokes[-1]['id']
    return render_to_response('joke.html', {'jokes':jokes,'lastid':lastid})


def morejoke(req, lastid):
    jokes = HttpUtil.getJokes(lastid)
    lastid = jokes[-1]['id']
    if req.is_ajax():
        t = loader.get_template('ajax_joke.html')
        html = t.render(Context({'jokes': jokes}))
        return HttpResponse(html)
    return render_to_response('joke.html', {'jokes': jokes, 'lastid': lastid})


def picture(req):
    pictures = HttpUtil.getPictures('-1')
    lastid = pictures[-1]['id']
    return render_to_response('picture.html', {'pictures': pictures,'lastid':lastid})


def morepicture(req,lastid):
    pictures = HttpUtil.getPictures(lastid)
    lastid = pictures[-1]['id']
    return render_to_response('picture.html', {'pictures': pictures, 'lastid': lastid})


def video(req):
    videos = HttpUtil.getVideos('-1')
    lastid = videos[-1]['id']
    return render_to_response('video.html', {'videos':videos,'lastid':lastid})


def morevideo(req,lastid):
    videos = HttpUtil.getVideos(lastid)
    lastid = videos[-1]['id']
    return render_to_response('video.html', {'videos':videos,'lastid':lastid})


def album(req):
    albums = HttpUtil.getAlbums('-1')
    lastid = albums[-1]['id']
    return render_to_response('album.html', {'albums':albums,'lastid':lastid})


def morealbum(req,lastid):
    albums = HttpUtil.getAlbums(lastid)
    lastid = albums[-1]['id']
    return render_to_response('album.html', {'albums':albums,'lastid':lastid})


def albumbeauty(req,aid,page):
    albums = HttpUtil.getAlbumVideoAndBeauty(aid, page)
    pre = 0
    page = int(page)
    if page > 0:
        pre = page -1
    page = page + 1
    more = 1
    if len(albums)==0:
        page = page - 2
        more = 0
    if req.is_ajax():
        t = loader.get_template('ajax_album_beauty.html')
        html = t.render(Context({'albums': albums}))
        return HttpResponse(html)
    return render_to_response('albumbeauty.html', {'albums': albums, 'next': page,'pre':pre, 'aid': aid,'more':more})


def albumpic(req,aid,page):
    pics = HttpUtil.getAlbumVideoAndBeauty(aid,page)
    pre = 0
    page = int(page)
    if page > 0:
        pre = page - 1
    page = page + 1
    more = 1
    if len(pics) == 0:
        page = page - 2
        more = 0
    return render_to_response('albumpic.html', {'pics': pics, 'next': page,'pre':pre, 'aid': aid,'more':more})


def albumvideo(req,aid,page):
    videos = HttpUtil.getAlbumVideoAndBeauty(aid,page)
    pre = 0
    page = int(page)
    if page > 0:
        pre = page - 1
    page = page + 1
    more = 1
    if len(videos) == 0:
        page = page - 2
        more = 0
    return render_to_response('albumvideo.html', {'videos': videos, 'next': page,'pre':pre, 'aid': aid,'more':more})

