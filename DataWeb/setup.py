import os
from setuptools import setup


PACKAGE_NAME='DataWeb'
version_file = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'VERSION'))
version = version_file.read().strip()
print version

setup(
    name=PACKAGE_NAME,
    version=version,
    packages=[PACKAGE_NAME],
    include_package_data=True,
    install_requires=['flask',
                      'lxml',
                      'markdown2',
                      'py',
                      'blinker',
                      'decorator',
                      'FLask-Login',
                      'FLask-Mail',
                      'Flask-User',
                      'Flask-SQLAlchemy',
                      'Flask-WhooshAlchemy',
                      'Flask-WTF',
                      'flipflop',
                      'pbr',
                      'six',
                      'SQLAlchemy',
                      'sqlalchemy-migrate',
                      'sqlparse',
                      'Tempita',
                      'Whoosh',
                      'WTForms',
                      'enum34'])
