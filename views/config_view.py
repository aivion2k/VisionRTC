import json
from aiohttp import web

CONFIG_FILE = 'configs/config.json'

async def get_config(request):
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
        return web.json_response(config)
    except Exception as e:
        return web.json_response({"status": "error", "message": str(e)})
