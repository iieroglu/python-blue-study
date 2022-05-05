import identity.identity.authenticator as auth


def test_auth():
    authenticator = auth.Authenticator()
    resp = authenticator.authenticate()
    assert resp == '123'
