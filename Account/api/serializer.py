from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import (ModelSerializer,
									HyperlinkedIdentityField,
									SerializerMethodField,
									ValidationError,
									EmailField,
									CharField
									)

from Account.models import Profile

class BalanceSerilize(ModelSerializer):
	class Meta:
		model=Profile
		fields=[
		'balance'
		]
