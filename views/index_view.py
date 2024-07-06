import os
from aiohttp import web

ROOT = os.path.dirname(os.path.dirname(__file__))

async def index(request):
    content = open(os.path.join(ROOT, "static", "index.html"), "r").read()
    return web.Response(content_type="text/html", text=content)
