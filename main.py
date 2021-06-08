import sys
from extend.jd_spider_requests import *




if __name__ == "__main__":
    jd_seckill = JdSeckill()

    print(dir(jd_seckill))

    jd_seckill.login_by_qrcode()

    # jd_seckill.reserve()
    print(jd_seckill.get_username())