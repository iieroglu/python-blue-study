from jproperties import Properties
import identity.identity.repo.data_source as data_source
import identity.identity.repo.session_repo as session_repo
from datetime import datetime, timedelta
import uuid

session_uuid = str(uuid.uuid4())
user_uuid = str(uuid.uuid4())

N_DAYS_LATER = 90


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


def test_add_session():
    mysql_data_source = connect_db()
    access_token = str(uuid.uuid4())
    refresh_token = str(uuid.uuid4())

    today = datetime.now()
    access_toke_exp = today + timedelta(days=N_DAYS_LATER)

    formatted_date = access_toke_exp.strftime('%Y-%m-%d %H:%M:%S')
    session_operations = session_repo.Session(mysql_data_source, session_uuid, user_uuid, access_token, formatted_date,
                                              refresh_token, True)
    session_operations.add_item()


def test_get_session_by_id():
    mysql_data_source = connect_db()
    session_operations = session_repo.Session(mysql_data_source, None, None, None, None, None, None)
    session = session_operations.get_by_id(session_uuid)
    print('Session => access_token: %s ' % session.access_token)


def test_get_session_by_user_id():
    mysql_data_source = connect_db()
    session_operations = session_repo.Session(mysql_data_source, None, None, None, None, None, None)
    sessions = session_operations.get_sessions_by_user_id(user_uuid)
    print('Get sessions by user_id length => : %s ' % len(sessions))


def test_update_session():
    mysql_data_source = connect_db()
    session_operations = session_repo.Session(mysql_data_source, None, None, None, None, None, None)
    session_update = session_operations.get_by_id(session_uuid)
    session_update.data_source = mysql_data_source
    session_update.access_token = str(uuid.uuid4())
    session_update.access_toke_exp = datetime.now() + timedelta(days=80)
    session_update.update_item()
