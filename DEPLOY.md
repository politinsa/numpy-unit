build:
---
python setup.py sdist bdist_wheel
python -m twine upload dist/*

Doc:
---
pandoc --from=markdown --to=rst --output=README.rst README.md
cd docs && make clean && make html

Coverage:
---
coverage run numpy_unit/tests.py
codecov --token=token