#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from setuptools import setup


name = 'drf_mixin_tools'
package = 'drf_mixin_tools'
description = 'Collection of helpfull tools for drf'
url = 'https://github.com/nabakirov/drf_mixin_tools'
author = 'Nursultan Abakirov'
author_email = 'nabakirov@gmail.com'
license = 'MIT'
version = '0.0.3'


if sys.argv[-1] == 'publish':
    if os.system("pip freeze | grep wheel"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a {0} -m 'version {0}'".format(version))
    print("  git push --tags")
    sys.exit()


setup(
    name=name,
    version=version,
    url=url,
    license=license,
    description=description,
    author=author,
    author_email=author_email,
    packages=['drf_mixin_tools'],
    package_data={'drf_mixin_tools': []},
    install_requires=[
        'Django>=2.0.4',
        'djangorestframework>=3.8.2',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
