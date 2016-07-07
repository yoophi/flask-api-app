# -*- coding: utf-8 -*-
"""
Flask-Api-App
-------------------

RESTful API 를 제공하는 App 개발을 위한 Base Class
"""
import os
import re
from setuptools import setup


def find_version(fname):
    '''Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    '''
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version


__version__ = find_version(os.path.join("flask_api_app", "__init__.py"))

setup(
    name='Flask-Api-App',
    version=__version__,
    url='http://github.com/yoophi/flask-api-app/',
    license='MIT License',
    author='Pyunghyuk Yoo',
    author_email='yoophi@gmail.com',
    description='Base Flask extension for RESTful Flask App',
    long_description=__doc__,
    packages=['flask_api_app',
              'flask_api_app.core',
              'flask_api_app.core.accounts',
              'flask_api_app.core.api',
              'flask_api_app.core.main',
              ],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask==0.11.1',
        'Flask-Admin==1.4.2',
        'Flask-Security==1.7.5',
        'Flask-SQLAlchemy==2.1',
        'Flask-OAuthlib==0.9.3',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)