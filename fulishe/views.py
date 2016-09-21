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

