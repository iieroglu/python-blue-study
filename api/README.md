docker rmi -f  $(docker images -f "dangling=true" -q)

for each module to create python env =>

cd module (catalog tender etc..)
python3 -m venv venv

#api
pip3 install -r requirements.txt

#web-ui
pip3 install -r requirements.txt 