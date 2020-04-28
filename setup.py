  # -*- coding: utf-8 -*-

from pathlib import Path
import sys

import pkg_resources
from setuptools import setup

import django_numpy


BASE_DIR = Path(__file__).parent

if sys.version_info[0] == 2:
    from codecs import open

# Read requirements
with (BASE_DIR / "requirements.txt").open() as requirements_txt:
    _REQUIRES = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

# Read description
with open(BASE_DIR / "README.rst", encoding='utf-8') as f:
    _LONG_DESCRIPTION = f.read()

_CLASSIFIERS = (
    'Development Status :: 5 - Production/Stable',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Libraries :: Python Modules',
)
_KEYWORDS = ' '.join([
    'python',
    'django',
    'database',
    'numpy',
])

setup(
    name='django-numpy',
    version=django_numpy.__version__,
    description=django_numpy.__description__,
    long_description=_LONG_DESCRIPTION,
    author=django_numpy.__author__,
    author_email=django_numpy.__email__,
    maintainer=django_numpy.__author__,
    maintainer_email=django_numpy.__email__,
    url=django_numpy.__url__,
    download_url=django_numpy.__url__,
    packages=[
        'django_numpy',
    ],
    include_package_data=True,
    install_requires=_REQUIRES,
    extras_require={
        'dev': [
            'setuptools',
            'pip',
            'wheel',
            'prospector'
        ]
    },
    license=django_numpy.__license__,
    zip_safe=False,
    keywords=_KEYWORDS,
    classifiers=_CLASSIFIERS,
)
