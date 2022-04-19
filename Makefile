all:
	@echo "Select a desired action (env, install)!"

env:
	/usr/bin/env python3 -m venv env
	source ./env/bin/activate; pip install -r ./requirements.txt

install: env
	@./script/install.sh

