#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import  logging; logging.basicConfig(level = logging.INFO)

import asyncio, os, time, json
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=u'<h1>你好！</h1>', content_type='text/html',charset='utf-8')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    rev = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server start at http://127.0.0.1:9000...')
    return rev
    
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()