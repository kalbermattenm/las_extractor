# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='las_extractor',
    version='0.1',
    description='SITN, a sitn project',
    author='sitn',
    author_email='sitn@ne.ch',
    url='http://www.ne.ch/sitn',
    install_requires=[
        'pyramid',
        'SQLAlchemy',
        'waitress',
        'sqlahelper',
        'pyramid_debugtoolbar',
        'pyramid_tm',
        'papyrus'
    ],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'paste.app_factory': [
            'main = las_extractor:main',
        ],
    },
)
