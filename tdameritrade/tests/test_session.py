
class TestSession:
    def test_can_call(self):
        from tdameritrade import session
        session.TDASession()

    def test_init_header(self):
        from tdameritrade.session import TDASession
        test_token = {"token": ""}
        TDASession().set_token(test_token)
