
DIR := ${CURDIR}
DOCS_DIR = docs
DIST := ${CURDIR}/dist

.PHONY: clean build publish

clean:
	$(MAKE) -C ${DOCS_DIR} clean
	$(PYTHON) setup.py clean
	rm -rf ${DIST}

build:
	$(PYTHON) setup.py sdist

publish: clean build
	$(PIP) install twine
	$(PYTHON) -m twine upload --repository testpypi ${DIST}/*
	@echo
	@echo "Test with the following line:"
	@echo "pip install --index-url https://test.pypi.org/simple/ auto-sklearn"
	@echo
	@echo "Once you have decided it works, publish to actual pypi with"
	@echo "python -m twine upload dist/*"
