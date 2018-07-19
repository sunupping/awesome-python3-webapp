#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
    文本注释
'''
__author__ = 'sj'

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(text='Awesome')

def init():
    app = web.Application()
    app.add_routes([web.get('/', index)])
    web.run_app(app, host='127.0.0.1', port=8089)
    logging.info('server started at http://127.0.0.1:8089...')

if __name__ == '__main__':
    init()



