for each module to create python env =>

cd module (identity catalog tender etc..)

python3 -m venv venv

---------------------------------------------------------------

#identity \
pip3 install -r requirements.txt 

#to build identity as a python library \
pip3 install wheel \
pip3 install setuptools \
pip3 install twine 

#python setup.py pytest \
python3 setup.py bdist_wheel 

---------------------------------------------------------------

#api \
pip3 install -r requirements.txt 


---------------------------------------------------------------

Dockerization 

Lets start with clearing docker images;  

docker rmi -f  $(docker images -f "dangling=true" -q) 

docker-compose up -d --build 


---------------------------------------------------------------

Mysql Tables

docker rm -f mysql
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=testdb -e MYSQL_ROOT_HOST='%' -d mysql/mysql-server:5.7


create table users(id VARCHAR(40) DEFAULT (uuid()) primary key, name VARCHAR(255), surname VARCHAR(255), date_of_birth TIMESTAMP, email VARCHAR(255), gsm VARCHAR(255))

create table sessions(user_id VARCHAR(255), access_token VARCHAR(255), access_token_expiry timestamp, refresh_token VARCHAR(255), INDEX (user_id, access_token))
