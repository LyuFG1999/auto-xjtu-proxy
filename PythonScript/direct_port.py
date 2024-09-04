# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 08:30:47 2024

@author: Lyu
"""

import asyncio
from mitmproxy import http
from mitmproxy.tools.dump import DumpMaster
from mitmproxy.options import Options

# -------------------------
#          直连
# -------------------------
class AutoRedirect:
    def request(self, flow: http.HTTPFlow) -> None:
        pass

    def response(self, flow: http.HTTPFlow) -> None:
        pass
    
    
async def start_proxy():
    opts = Options(listen_host="127.0.0.1", listen_port=12380)
    m = DumpMaster(opts)
    addon = AutoRedirect()
    m.addons.add(addon)
    
    try:
        print("Starting mitmproxy on 127.0.0.1:12380")
        await m.run()
    except KeyboardInterrupt:
        await m.shutdown()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    if loop.is_running():
        loop.create_task(start_proxy())
    else:
        loop.run_until_complete(start_proxy())