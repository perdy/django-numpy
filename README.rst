============
Django Numpy
============

:Version: 1.0.1
:DjangoNumpy: Production/Stable
:Author: José Antonio Perdiguero López

Django Numpy is an application for Django projects that adds some utilities and integration tools with Numpy.

Quick start
===========

#. Install this package using pip::

    pip install django-numpy

#. Add *PROJECT_PATH* to your django settings module.
#. Add *status* to your **INSTALLED_APPS** settings like this::

    INSTALLED_APPS = (
        ...
        'django_numpy',
    )

Database Fields
===============

This package adds a new Field type that manages numpy arrays. This field is based on django ArrayField, that
*only works with PostgreSQL backend*. The **NumpyArrayField** behave just like Django's ArrayField so all parameters
defined in `official docs <https://docs.djangoproject.com/en/1.10/ref/contrib/postgres/fields/#arrayfield>`_.
