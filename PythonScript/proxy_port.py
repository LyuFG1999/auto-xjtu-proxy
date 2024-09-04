# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 08:30:47 2024

@author: Lyu
"""
import re
import copy
import asyncio
from mitmproxy import http
from mitmproxy import ctx
from mitmproxy.tools.dump import DumpMaster
from mitmproxy.options import Options
from binascii import hexlify, unhexlify
from Crypto.Cipher import AES

# -------------------------
#          网页转换
# -------------------------

class WebvpnUrl:
    KEY_ = b'wrdvpnisthebest!'
    IV_ = b'wrdvpnisthebest!'
    SIZE = 128
    PREFIX = '77726476706e69737468656265737421'
    PREFIX_LEN = len(PREFIX)
    URL_INFO = {
        'webvpn': {
            'protocol': 'https',
            'host': '',
            'port': '',
        },
        'target': {
            'protocol': '',
            'host': '',
            'port': '',
            'url': '/',
        }
    }

    def __init__(self, inst_host=''):
        self.INST_HOST = inst_host
        self.url_info = copy.deepcopy(WebvpnUrl.URL_INFO)

    def __encrypt(self, text):
        key = WebvpnUrl.KEY_
        cfb_iv = WebvpnUrl.IV_
        size = WebvpnUrl.SIZE
        cfb_cipher_encrypt = AES.new(key, AES.MODE_CFB, cfb_iv, segment_size=size)

        message = text.encode('utf-8')
        mid = cfb_cipher_encrypt.encrypt(message)
        return hexlify(mid).decode()

    def __decrypt(self, ciphertext):
        key = WebvpnUrl.KEY_
        cfb_iv = WebvpnUrl.IV_
        size = WebvpnUrl.SIZE

        message = unhexlify(ciphertext.encode('utf-8'))
        cfb_cipher_decrypt = AES.new(key, AES.MODE_CFB, cfb_iv, segment_size=size)
        return cfb_cipher_decrypt.decrypt(message).decode('utf-8')

    def __get_url(self, mode):
        host_encrypted_target, url = None, None
        host_target = self.url_info['target']['host']
        if host_target != '' and mode == 'encode':
            host_encrypted_target = WebvpnUrl.PREFIX + self.__encrypt(host_target)
        elif host_target == '':
            return ''

        port_webvpn = str(self.url_info['webvpn']['port'])
        if port_webvpn != '' and mode == 'encode':
            port_webvpn = ':' + port_webvpn

        port_target = str(self.url_info['target']['port'])
        if port_target != '':
            if mode == 'encode':
                port_target = '-' + port_target
            elif mode == 'decode':
                port_target = ':' + port_target
        if mode == 'encode':
            url = '%s://%s%s/%s%s/%s%s' % (
                self.url_info['webvpn']['protocol'],
                self.url_info['webvpn']['host'],
                port_webvpn,
                self.url_info['target']['protocol'],
                port_target,
                host_encrypted_target,
                self.url_info['target']['url'],
            )
        elif mode == 'decode':
            url = '%s://%s%s%s' % (
                self.url_info['target']['protocol'],
                host_target,
                port_target,
                self.url_info['target']['url'],
            )
        return url

    def __get_url_info_from_plain(self, url):
        self.url_info = copy.deepcopy(WebvpnUrl.URL_INFO)

        self.url_info['webvpn']['host'] = self.INST_HOST

        st1 = url.split('//')
        self.url_info['target']['protocol'] = st1[0][:-1]
        if st1[0] == '' or st1[0] == 'http:':
            self.url_info['webvpn']['protocol'] = 'https'
        else:
            self.url_info['webvpn']['protocol'] = st1[0][:-1]

        host = re.match('[0-9,a-z,A-Z,\.\-\:]*', st1[1]).group(0)
        my_url = st1[1][len(host):]
        if my_url == '' or my_url[0] != '/':
            my_url = '/' + my_url
        self.url_info['target']['url'] = my_url

        if host.find(':') != -1:
            host, port = host.split(':')
            self.url_info['target']['host'] = host
            self.url_info['target']['port'] = port
        else:
            self.url_info['target']['host'] = host

    def __get_url_info_from_encrypted(self, url):
        self.url_info = copy.deepcopy(WebvpnUrl.URL_INFO)

        self.url_info['webvpn']['host'] = self.INST_HOST

        st1 = url.split('//')
        if st1[0] == '':
            st1[0] = 'https:'
        self.url_info['webvpn']['protocol'] = st1[0][:-1]

        index1 = st1[1].find('/')
        st2 = st1[1][0:index1]

        if st2.find(':') != -1:
            st2_1 = st2.split(':')
            self.url_info['webvpn']['port'] = st2_1[1]

        st3 = st1[1][index1 + 1:]
        index2 = st3.find('/')
        st4 = st3[0:index2]

        if st4.find('-') != -1:
            st4_1 = st4.split('-')
            self.url_info['target']['protocol'] = st4_1[0]
            self.url_info['target']['port'] = st4_1[1]
        else:
            self.url_info['target']['protocol'] = st4

        st5 = st3[index2 + 1:]
        host_encrypted_target = re.match('[0-9,a-f]*', st5).group(0)
        my_url = st5[len(host_encrypted_target):]
        if my_url == '' or my_url[0] != '/':
            my_url = '/' + my_url
        self.url_info['target']['url'] = my_url

        host_target = self.__decrypt(host_encrypted_target[WebvpnUrl.PREFIX_LEN:])
        self.url_info['target']['host'] = host_target

    def url_encode(self, url=''):
        if url != '':
            self.__get_url_info_from_plain(url)
        return self.__get_url(mode='encode')

    def url_decode(self, url=''):
        if url != '':
            self.__get_url_info_from_encrypted(url)
        return self.__get_url(mode='decode')


def convert_url(url: str) -> str:
    d = WebvpnUrl("webvpn.xjtu.edu.cn")
    url_con = d.url_encode(url)
    return url_con
    
# -------------------------
#          修改代理
# -------------------------
class AutoRedirect:
    def request(self, flow: http.HTTPFlow) -> None:
        original_url = flow.request.pretty_url
        
        # 检查是否是例外 URL
        if original_url.startswith("https://webvpn.xjtu.edu.cn"):
            print("正在加载 URL {}.".format(original_url)) 
            return
        else:
            # 使用 redirect_url 函数修改请求的 URL
            modified_url = convert_url(original_url)
            
            # 如果 URL 有变化，则返回一个 302 重定向响应
            if original_url != modified_url:
                print(" 正在转换 URL {} --> {}.".format(original_url,modified_url)) 
                # 返回一个 302 重定向
                flow.response = http.Response.make(
                    302,  # 302 重定向
                    b"",  # 响应体为空
                    {"Location": modified_url}  # 设置重定向的目标 URL
                )

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