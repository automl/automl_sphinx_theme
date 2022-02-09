
PIP := pip
PYTHON := python
DIR := "${CURDIR}"
DOCS_DIR = docs
DIST := "${CURDIR}/dist"

.PHONY: clean build publish

clean:
	$(MAKE) -C ${DOCS_DIR} clean
	$(PYTHON) setup.py clean
	rm -rf "${DIST}"

build:
	$(PYTHON) setup.py sdist

publish: clean build
	$(PIP) install twine
	$(PYTHON) -m twine upload --repository testpypi ${DIST}/*
	@echo
	@echo "Test with the following:"
	@echo "* Create a new virtual environment to install the uplaoded distribution into"
	@echo "* Run the following:"
	@echo
	@echo "        pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ automl_sphinx_theme"
	@echo
	@echo "* Run this to make sure it can import correctly, plus whatever else you'd like to test:"
	@echo
	@echo "        python -c 'import automl_sphinx_theme'"
	@echo
	@echo "Once you have decided it works, publish to actual pypi with"
	@echo
	@echo "    python -m twine upload dist/*"
