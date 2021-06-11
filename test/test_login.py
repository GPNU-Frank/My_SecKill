import sys
sys.path.append("..")

from extend.jd.jd_login import JDLogin
from extend.jd.jd_session import JDSession

if __name__ == "__main__":
    jd_session = JDSession()
    # print(dir(jd_session))
    jd_login = JDLogin(jd_session)

    print(jd_login.is_login)
    jd_login.login_by_qrcode()
