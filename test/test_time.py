import sys
import requests
sys.path.append("..")
from socket import gethostbyname

from utils import Timer


if __name__ == "__main__":
    # timer = Timer()

    url = "https://www.jd.com/"
    # print(gethostbyname(url))
    s = requests.Session()
    for i in range(5):
        # ret = s.get(url)
        ret = requests.get(url, stream=True)
        # print(ret.headers)
        # print(dir(ret))
        # print(ret.cookies)
        # print(ret.connection)
        print(ret.elapsed.total_seconds())
        # print(dir(ret.elapsed))