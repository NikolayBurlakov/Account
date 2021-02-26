from rest_framework import serializers
from stamp.models import Diller, Plotter, Mold, User
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory, InlineFormSetView


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    languages = serializers.ListField(child=serializers.CharField(max_length=30, allow_blank=True),
                                      source="userprofile.languages")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password', 'lanugages')

    def create(self, validated_data, instance=None):
        profile_data = validated_data.pop('userprofile')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        Diller.objects.update_or_create(user=user, **profile_data)
        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
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


class PlotterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plotter
        fields = '__all__'


class MoldDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mold
        fields = '__all__'


class MoldListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mold
        fields = '__all__'
