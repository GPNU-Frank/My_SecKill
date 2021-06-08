import requests
from base import BaseLogin


class JDLogin(BaseLogin):
    def __init__(self):
        super(BaseLogin, self).__init__()
        self.name = "登录京东"

        self.qrcode_img_file = "jd_qr_code.png"

        self.url = 'https://qr.m.jd.com/show'

        self.session = None

    def get_qrcode(self):
        payload = {
            'appid': 133,
            'size': 147,
            't': str(int(time.time() * 1000)),
        }
        headers = {
            'User-Agent': self.spider_session.get_user_agent(),
            'Referer': 'https://passport.jd.com/new/login.aspx',
        }
        resp = self.session.get(url=url, headers=headers, params=payload)

        if not response_status(resp):
            logger.info('获取二维码失败')
            return False

        save_image(resp, self.qrcode_img_file)
        logger.info('二维码获取成功，请打开京东APP扫描')
        open_image(self.qrcode_img_file)
        return True