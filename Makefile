init:
	pip install -e .

test: init
	python tests/test_*
	rm -rf float_range.egg-info
