import json
import time
import urllib.request
import urllib.error

import http.cookiejar
import http.cookies

class Downloader(object):
    # Minimally emulates a modern browser with an "Accept" cookie set
    @staticmethod
    def get(url):
        try:
            cj = http.cookiejar.CookieJar()
            jar_cookie = http.cookiejar.Cookie(
                version=0,
                # name=cookie.key,
                name='AcceptedCookie_www.almedalsveckan.info_',
                # value=cookie.value,
                value='true',
                port=None,
                port_specified=False,
                # domain=cookie['domain'],
                domain='www.almedalsveckan.info',
                domain_specified=True,
                domain_initial_dot=False,
                # path=cookie['path'],
                path='/',
                path_specified=True,
                secure=False,
                expires=None,
                discard=True,
                comment=None,
                comment_url=None,
                rest={'HttpOnly': None},
                rfc2109=False
            )
            cj.set_cookie(jar_cookie)
            opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
            opener.addheaders = [('user-agent',
                                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36')]
            # urllib.request.install_opener(opener)
            # req = urllib.request.Request(url)
            # req.add_header('user-agent',
            #                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36')
            # response=urllib.request.urlopen(req).read()
            with opener.open(url) as f:
                response = f.read()
            return response
        except urllib.error.HTTPError as err:
            print(f"ERROR {err.code}: Could not download {url}.")
            if err.code == 403:
                print("Retrying in 10 seconds")
                time.sleep(10)
                return Downloader.get(url)
            else:
                print("Permanent error: skipping this event")
                return None

    def get_json(url):
        return json.loads(Downloader.get(url).decode("utf-8"))
