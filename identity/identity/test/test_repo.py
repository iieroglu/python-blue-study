from jproperties import Properties
import identity.identity.repo.data_source as data_source
import identity.identity.repo.db_crud_operations as db_crud_operations


def test_repo_connect():
    connect_db()
    assert True


def test_get_student():
    mysql_data_source = connect_db()
    user_operations = db_crud_operations.User(mysql_data_source)
    user_operations.add_item()


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
