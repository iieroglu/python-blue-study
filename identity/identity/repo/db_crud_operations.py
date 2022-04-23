class DbObj:
    def __init__(self, data_source):
        self.data_source = data_source

    def add_item(self):
        raise NotImplemented


class User(DbObj):

    def add_item(self):
        conn = self.data_source.get_connection()
        my_cursor = conn.cursor()  # cursor() method create a cursor object
        try:
            # Execute SQL Query to insert record
            my_cursor.execute("insert into users values(NULL,'Ilker', 'Eroglu', '', '')")
            conn.commit()  # Commit is used for your changes in the database
            print('Record inserted successfully...')
        except:
            # rollback used for if any error
            conn.rollback()
        print("User added")