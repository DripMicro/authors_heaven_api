
from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """ 
    The first few fields belong to the profiles Model
    however we can refrence them in the UserSerializer,
    with the use of 'source' as the User_model is one_to_to 
    relationship to the Profile_model
    """
    gender = serializers.CharField(source="profile.gender")
    phone_number = PhoneNumberField(source="profile.phone_number")
    profile_photo = serializers.ReadOnlyField(source="profile.profile_photo")
    country = CountryField(source="profile.country")
    city = serializers.CharField(source="profile.city")
    
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "gender",
            "phone_number",
            "profile_photo",
            "country",
            "city",
        ]

        """ 
        We make use of SerializerMethodField for first_name,
        last_name, full_name 
        -> This is a read-only field. It gets its value by calling a method on the serializer 
           class it is attached to.
        -> The serializer method referred to by the method_name argument should accept a single argument (in addition to self),
           which is the object being serialized
         """
        def get_first_name(self,obj):
            return obj.first_name.title()
        
        def get_last_name(self, obj):
            return obj.last_name.title()

        def get_full_name(self, obj):
            first_name = obj.user.first_name.title()
            last_name = obj.user.last_name.title()
            return f"{first_name} {last_name}"

        

        def to_representation(self,instance):
            """
            Custom relational fields :
            To implement a custom relational field, you should override RelatedField,
            and implement the .to_representation(self, value) method. 
            This method takes the target of the field as the value argument, and should
            return the representation that should be used to serialize the target. 
            The value argument will typically be a model instance.

            """
            representation = super(UserSerializer, self).to_representation(instance)
            if instance.is_superuser:
                representation["admin"] = True
            return representation

class CreateUserSerializer(UserCreateSerializer):
    """ Making use of the doser UserCreateSerializer """
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "password"]
