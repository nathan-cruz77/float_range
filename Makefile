init:
	pip install -e .

test: init
	python tests/test_*
	rm -rf float_range.egg-info

readme:
	pandoc --output=README --to rst README.md

update-pypitest:
	python setup.py register -r pypitest
	python setup.py sdist upload -r pypitest
	rm -r dist
	rm MANIFEST

update-pypi:
	python setup.py register -r pypi
	python setup.py sdist upload -r pypi
	rm -r dist
	rm MANIFEST
