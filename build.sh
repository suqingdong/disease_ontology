rm -rf build *.egg-info dist

python3 setup.py build sdist bdist_wheel

rm -rf build *.egg-info

