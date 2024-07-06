import os
from aiohttp import web

ROOT = os.path.dirname(os.path.dirname(__file__))

async def javascript(request):
    content = open(os.path.join(ROOT, "static", "client.js"), "r").read()
    return web.Response(content_type="application/javascript", text=content)
