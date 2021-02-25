from rest_framework import serializers
from stamp.models import Diller, Plotter, Mold, Users


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class DillerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diller
        fields = '__all__'


class DillerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diller
        fields = '__all__'


class PlotterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plotter
        fields = '__all__'


class MoldDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mold
        fields = '__all__'
