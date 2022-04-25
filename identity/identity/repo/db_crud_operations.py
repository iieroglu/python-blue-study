class DbObj:
    def __init__(self, data_source):
        self.data_source = data_source

    def add_item(self):
        raise NotImplemented


class User(DbObj):

    def __init__(self, data_source, user_id, name, surname, date_of_birth, email, gsm):
        super().__init__(data_source)
        self.id = user_id
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.email = email
        self.gsm = gsm

    def add_item(self):
        try:
            conn = self.data_source.get_connection()
            cursor = conn.cursor()
            mysql_insert_query = """INSERT INTO users (id, name, surname, date_of_birth, email, gsm) 
                                    VALUES (%s, %s, %s, %s, %s, %s) """

            record = (self.id, self.name, self.surname, self.date_of_birth, self.email, self.gsm)
            cursor.execute(mysql_insert_query, record)
            conn.commit()

            print('Record inserted successfully.. Record Id: %s' % self.id)
            return self
        except BaseException as err:
            # rollback used for if any error
            print(err)
            conn.rollback()
        print("User added")

    def get_by_id(self, user_id):
        try:
            conn = self.data_source.get_connection()
            cursor = conn.cursor()
            sqlite_select_query = """SELECT * from users where id = %s"""
            params = (user_id, )
            cursor.execute(sqlite_select_query, params)
            record = cursor.fetchone()
            u = User(None, record[0], record[1], record[2], record[3], record[4], record[5])
            cursor.close()
            return u
        except BaseException as err:
            print(err)


    def get_all(self):
        try:
            conn = self.data_source.get_connection()
            cursor = conn.cursor()
            sqlite_select_query = """SELECT * from users"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            print("Total rows are:  ", len(records))
            print("Printing each row")
            for row in records:
                print("Id: ", row[0])
                print("Name: ", row[1])
                print("Email: ", row[2])
                print("Salary: ", row[3])
                print("\n")

            cursor.close()
        except BaseException as err:
            print(err)
