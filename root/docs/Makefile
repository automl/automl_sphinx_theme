SPHINXBUILD = sphinx-build
.PHONY: clean buildapi html

clean:
	rm -rf html
	rm -rf api
	rm -rf _autosummary

html:
	sphinx-build -b html . html -a

all:
	make clean
	make html
