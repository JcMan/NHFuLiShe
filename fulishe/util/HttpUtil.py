# -*- coding:utf-8 -*-
import requests, json ,time

def getJokeUrl(lastid):
    url = '''http://120.26.78.221/weibofun/weibo_list.php?apiver=10901&category=weibo_jokes&max_timestamp={max}&latest_viewed_ts={last}&platform=aphone&sysver=4.3&appver=1.2.2&buildver=1.2.2&app_ver=10202&uid=-1&udid=a_c588e7ca0f8b9899&channel=store360&page=0&page_size=30'''
    url = url.replace("{max}",lastid)
    url = url.replace("{last}",lastid)
    return url
def getJokes(lastid):
    result = requests.get(getJokeUrl(lastid))
    items = json.loads(str(result.content))
    items = items['items']
    for item in items:
        t = int(item['update_time'])
        item['id'] = item['update_time']
        item['update_time'] = time.strftime("%Y/%m/%d %H:%M", time.localtime(float(t)))
        item['likes'] = str(int(float(item['likes'])))
    return items


def getPictureUrl(lastid):
    url = 'http://fuli1024.com/weibofun/weibo_list.php?apiver=10901&category=weibo_pics&page=0&page_size=30&max_timestamp={max}&latest_viewed_ts={last}&platform=aphone&sysver=5.1&appver=1.2.3&buildver=1.2.3&app_ver=10203&uid=-1&udid=a_fe79a4abf13e4f7d&channel=meizu'
    url = url.replace("{max}", lastid)
    url = url.replace("{last}", lastid)
    return url


def getPictures(lastid):
    result = requests.get(getPictureUrl(lastid))
    items = json.loads(str(result.content))
    items = items['items']
    for item in items:
        t = int(item['update_time'])
        item['id'] = item['update_time']
        item['update_time'] = time.strftime("%Y/%m/%d %H:%M", time.localtime(float(t)))
        item['likes'] = str(int(float(item['likes'])))
    return items

def getVideoUrl(lastid):
    url = 'http://fuli1024.com/weibofun/weibo_list.php?apiver=10901&category=weibo_videos&page=0&page_size=30&max_timestamp={max}&latest_viewed_ts={last}&platform=aphone&sysver=5.1&appver=1.2.3&buildver=1.2.3&app_ver=10203&uid=-1&udid=a_fe79a4abf13e4f7d&channel=meizu'
    url = url.replace("{max}", lastid)
    url = url.replace("{last}", lastid)
    return url


def getVideos(lastid):
    result = requests.get(getVideoUrl(lastid)) 
    items = json.loads(str(result.content))
    items = items['items']
    for item in items:
        t = int(item['update_time'])
        item['id'] = item['update_time']
        if len(item['wbody'])>40:
            item['wbody'] = (item['wbody'][0:40]+'...')
        item['update_time'] = time.strftime("%Y/%m/%d %H:%M", time.localtime(float(t)))
        item['likes'] = str(int(float(item['likes'])))
    return items




