import identity.authenticator as auth


class AuthService:

    def check_password(self, passwd):
        if passwd == '':
            return True

