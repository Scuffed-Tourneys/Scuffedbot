@ECHO off

python -m venv ./
cd Scripts
pip.exe install -r ../requirements.txt

cd ../src
(echo TOKEN= & echo MONGO_USR= & echoMONGO_PWD=) > .env