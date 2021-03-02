drf_mixin_tools
======================================

|pypi-version|

Overview
--------

Collection of helpful tools for djangorestframework

Requirements
------------

-  Python (3.5, 3.6)
-  Django (2.0)
-  Django REST Framework (3.8)

Installation
------------

Install using ``pip``

.. code:: bash

    $ pip install drf-mixin-tools


Examples
--------

serializer.py

.. code:: python

    from rest_framework import serializers


    class ListSerializer(serializers.ModelSerializer)
        ...


    class DetailSerializer(serializers.ModelSerializer)
        ...


    class RequestSerializer(serializers.ModelSerializer)
        ...

views.py

.. code:: python

    from rest_framework.viewsets import ModelViewSet
    from rest_framework.permissions import IsAuthenticated, AllowAny

    from drf_mixin_tools.mixins import ActionSerializerClassMixin, ActionPermissionClassesMixin

    from .serializers import ListSerializer, RequestSerializer, DetailSerializer


    class ModelViewSet(ActionSerializerClassMixin,
                       ActionPermissionClassesMixin,
                       ModelViewSet):
        serializer_class = AdListSerializer

        action_serializer_class = {
            'list': AdListSerializer,
            'create': RequestSerializer,
            'update': RequestSerializer,
            'partial_update': RequestSerializer,
            'retrieve': DetailSerializer
        }

        permission_classes = (IsAuthenticated,)

        action_permission_classes = {
            'list': (AllowAny,),
            'retrieve': (AllowAny,)
        }
