import json
from pathlib import Path
from setuptools import setup, find_packages


BASE_DIR = Path(__file__).resolve().parent
version_info = json.load(BASE_DIR.joinpath(
    'disease_ontology', 'version', 'version.json').open())


setup(
    name=version_info['prog'],
    version=version_info['version'],
    author=version_info['author'],
    author_email=version_info['author_email'],
    description=version_info['desc'],
    long_description=BASE_DIR.joinpath('README.md').open().read(),
    long_description_content_type="text/markdown",
    url='https://github.com/suqingdong/disease_ontology',
    project_urls={
        'Documentation': 'https://suqingdong.github.io/disease_ontology/',
        'Tracker': 'https://github.com/suqingdong/disease_ontology/issues',
    },
    license='BSD License',
    install_requires=BASE_DIR.joinpath(
        'requirements.txt').open().read().strip().split('\n'),
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'disease_ontology = disease_ontology.bin.main:main',
        ]},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ]
)
