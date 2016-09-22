# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from util import HttpUtil

# Create your views here.


def joke(req):
    jokes = HttpUtil.getJokes('-1')
    lastid = jokes[-1]['id']
    return render_to_response('joke.html', {'jokes':jokes,'lastid':lastid})


def morejoke(req,lastid):
    jokes = HttpUtil.getJokes(lastid)
    lastid = jokes[-1]['id']
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

