import sys
sys.path.append("..")

from extend.jd.jd_login import JDLogin

if __name__ == "__main__":
    jd_login = JDLogin()
    jd_login.get_qrcode()
