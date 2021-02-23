from rest_framework import serializers
from stamp.models import Diller
from django.contrib.auth.models import User


class DillerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diller
        fields = ('id', 'username', 'plotter')


class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'plotter', 'amount_of_mold')

