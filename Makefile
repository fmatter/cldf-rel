define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

test:
	pylint src
	flake8 src
	mypy src

coverage:
	coverage run -m pytest
	coverage html
	$(BROWSER) htmlcov/index.html

pypi:
	poetry publish --build
	rm -r dist

release:
	bump2version release --commit --tag
	git push; git push --tags
	make pypi
	bump2version patch
	git commit -am "bump"; git push