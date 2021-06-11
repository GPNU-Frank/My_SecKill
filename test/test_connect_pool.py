
import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import os
import threading
import time

session = None

def my_get(session):
    url = "https://www.jd.com"
    print(session)
    for i in range(2):
        resp = session.get(url=url)
        # print(resp.elapsed)
        # print(len(session.get_adapter(url).poolmanager.pools))
        # print(threading.get_ident(), session.get_adapter(url).get_connection(url).num_connections, session.get_adapter(url).get_connection(url).num_requests)
        # print(i, resp.elapsed)
        print(threading.get_ident(), resp.elapsed)
        # print(len(adapter.poolmanager.pools))

# def test():
#     print(1)
if __name__ == "__main__":


    url = "https://www.jd.com"

    pool_connections = 10
    pool_maxsize = 10
    max_retries = 3

    session = requests.Session()

    adapter = requests.adapters.HTTPAdapter(pool_connections=pool_connections, pool_maxsize=pool_maxsize, max_retries=max_retries)

    # print(dir(adapter))
    # print(adapter)
    # print(adapter.poolmanager)
    # print(dir(adapter.poolmanager))
    # pool = adapter.get_connection(url)
    # print(adapter.get_connection(url))
    # print(adapter.poolmanager.pools)
    # print(len(adapter.poolmanager.pools))
    # session.mount('http://', adapter)

    session.mount('https://', adapter)

    work_count = 10
    # with ThreadPoolExecutor(work_count) as pool:
    with ProcessPoolExecutor(work_count) as pool:
        for i in range(work_count):
            # pool.submit(my_get, args=(session,))
            pool.submit(my_get, session)


    # for i in range(10):
    #     resp = session.get(url=url)
    #     # print(dir(resp))
    #     print(i, resp.elapsed)
    #     print(len(adapter.poolmanager.pools))
    #     # print("Connections: {}; Requests: {}".format(pool.num_connections, pool.num_requests))
    time.sleep(60)