# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from util import HttpUtil

# Create your views here.
def joke(req):
    jokes = HttpUtil.getJokes()
    return render_to_response('joke.html', {'jokes':jokes})

