from rest_framework import serializers

from user.models import UserProfile  
from rest_auth.serializers import UserDetailsSerializer

class UserSerializer(serializers.ModelSerializer):

    #phone = serializer.PhoneNumberField(source="user.phone")
    #address = serializers.CharField(source="user.phone")

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('phone','address')

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('user', {})
        phone = profile_data.get('phone')
        address = profile_data.get('address')

        instance = super(UserSerializer, self).update(instance, validated_data)

        # get and update user profile
        profile = instance.userprofile
        if profile_data and phone:
            profile.phone = phone
            profile.save()
        return instance