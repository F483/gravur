# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


help:
	@echo "Some usefull development shortcuts."
	@echo "  clean      Remove all generated files."
	@echo "  test       Run tests and analysis tools."
	@echo "  devsetup   Setup development environment."
	@echo "  publish    Build and upload package to pypi."


clean:
	@rm -rf env
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg
	@find | grep -i ".*\.pyc$$" | xargs -r -L1 rm


devsetup: clean
	@virtualenv -p /usr/bin/python2 --system-site-packages env/py2
	@virtualenv -p /usr/bin/python3 --system-site-packages env/py3
	@env/py2/bin/python setup.py develop
	@env/py3/bin/python setup.py develop
	@env/py2/bin/pip install pudb
	@env/py3/bin/pip install pudb
	@env/py2/bin/pip install ipython
	@env/py3/bin/pip install ipython


run:
	#@env/py2/bin/python -m gravur
	@env/py3/bin/python -m gravur


test: devsetup
	@env/py2/bin/python setup.py test
	@env/py3/bin/python setup.py test
	# import pudb; pu.db # to set break point


publish: test
	@env/py2/bin/python setup.py register sdist upload
