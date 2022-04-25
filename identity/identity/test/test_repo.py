from jproperties import Properties
import identity.identity.repo.data_source as data_source
import identity.identity.repo.db_crud_operations as db_crud_operations
from datetime import datetime
import uuid

def test_repo_connect():
    connect_db()
    assert True


def connect_db():
    configs = get_config()
    mysql_data_source = data_source.MysqlDataSource(db_user=configs.get('DB_USER').data,
                                                    db_pass=configs.get('DB_PASS').data,
                                                    db_schema=configs.get('DB_SCHEMA').data)
    mysql_data_source.connect()
    return mysql_data_source


def get_config():
    configs = Properties()
    with open('test_config.properties', 'rb') as config_file:
        configs.load(config_file)
    print('dbuser %s ' % configs.get('DB_USER').data)
    return configs


def test_add_user():
    mysql_data_source = connect_db()
    birthdate = datetime(1984, 8, 9)
    formatted_date = birthdate.strftime('%Y-%m-%d %H:%M:%S')
    user_operations = db_crud_operations.User(mysql_data_source, str(uuid.uuid4()), 'Ilker', 'Eroglu', formatted_date,
                                              'iieroglu@gmail.com', '+905323255873')
    user_operations.add_item()


def test_get_user_by_id():
    mysql_data_source = connect_db()
    user_operations = db_crud_operations.User(mysql_data_source, None, None, None, None, None, None)
    user = user_operations.get_by_id('cec7b0f2-3e49-4b69-b37e-a20dddc375aa')
    print('User => name: %s ' % user.name)
