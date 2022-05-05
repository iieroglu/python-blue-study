import identity.identity.repo.base_repo as base_repo


class Session(base_repo.DbObj):

    def __init__(self, data_source, session_id, user_id, access_token, access_token_exp, refresh_token, active):
        super().__init__(data_source)
        self.id = session_id
        self.user_id = user_id
        self.access_token = access_token
        self.access_token_exp = access_token_exp
        self.refresh_token = refresh_token
        self.active = active

    def add_item(self):
        try:
            conn = self.data_source.get_connection()
            cursor = conn.cursor()
            mysql_insert_query = """INSERT INTO sessions (id, user_id, access_token, access_token_expiry, refresh_token, 
                                    active) VALUES (%s, %s, %s, %s, %s, %s) """

            record = (self.id, self.user_id, self.access_token, self.access_token_exp, self.refresh_token,
                      self.active)
            cursor.execute(mysql_insert_query, record)
            conn.commit()

            print('Record inserted successfully.. Record Id: %s' % self.id)
            return self
        except BaseException as err:
            # rollback used for if any error
            print(err)
            conn.rollback()
        print("User added")

    def get_by_id(self, session_id):
        try:
            conn = self.data_source.get_connection()
            cursor = conn.cursor()
            sqlite_select_query = """SELECT * from sessions where id = %s"""
            params = (session_id, )
            cursor.execute(sqlite_select_query, params)
            record = cursor.fetchone()
            u = Session(None, record[0], record[1], record[2], record[3], record[4], record[5])
            cursor.close()
            return u
        except BaseException as err:
            print(err)

    def get_sessions_by_user_id(self, user_id):
        try:
            conn = self.data_source.get_connection()
            cursor = conn.cursor()
            sqlite_select_query = """SELECT * from sessions where user_id = %s"""
            params = (user_id, )
            cursor.execute(sqlite_select_query, params)
            records = cursor.fetchall()
            sessions = []
            print("Total rows are:  ", len(records))
            print("Printing each row")
            for row in records:
                print("Id: ", row[0])
                print("UserId: ", row[1])
                print("AccessToken: ", row[2])
                print("AccessTokenExp: ", row[3])
                print("RefreshToken: ", row[4])
                print("Active: ", row[5])
                s = Session(None, row[0], row[1], row[2], row[3], row[4], row[5])
                sessions.append(s)
                print("\n")
            cursor.close()
            return sessions
        except BaseException as err:
            print(err)

    def get_all(self):
        try:
            conn = self.data_source.get_connection()
            cursor = conn.cursor()
            sqlite_select_query = """SELECT * from sessions"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            print("Total rows are:  ", len(records))
            print("Printing each row")
            for row in records:
                print("Id: ", row[0])
                print("UserId: ", row[1])
                print("AccessToken: ", row[2])
                print("AccessTokenExp: ", row[3])
                print("RefreshToken: ", row[4])
                print("Active: ", row[5])
                print("\n")

            cursor.close()
        except BaseException as err:
            print(err)

    def update_item(self):
        try:
            conn = self.data_source.get_connection()
            cursor = conn.cursor()
            mysql_insert_query = """UPDATE sessions set user_id = %s, access_token = %s, access_token_expiry = %s, 
                                    refresh_token = %s, active = %s where id = %s """

            record = (self.user_id, self.access_token, self.access_token_exp, self.refresh_token, self.active, self.id)
            cursor.execute(mysql_insert_query, record)
            conn.commit()

            print('Record updated successfully.. Record Id: %s' % self.id)
            return self
        except BaseException as err:
            # rollback used for if any error
            print(err)
            conn.rollback()
        print("Session updated")
