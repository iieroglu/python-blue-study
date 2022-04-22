for each module to create python env =>

cd module (identity catalog tender etc..)

python3 -m venv venv

---------------------------------------------------------------

#identity
pip3 install -r requirements.txt 

#to build identity as a python library
pip3 install wheel
pip3 install setuptools
pip3 install twine

#python setup.py pytest
python setup.py bdist_wheel

---------------------------------------------------------------

#api
pip3 install -r requirements.txt


================================================================

Dockerization

Lets start with clearing docker images; 

docker rmi -f  $(docker images -f "dangling=true" -q)

docker-compose up -d --build

