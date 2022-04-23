import identity.authenticator as auth


class AuthService:

    def check_password(self, passwd):
        authenticator = auth.Authenticator()
        resp = authenticator.authenticate()
        return passwd == resp

