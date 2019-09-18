from rest_framework import serializers
# from test_app.models import Product
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username' )


# class ProductSerializer(serializers.Serializer):
#     product_id = serializers.IntegerField()
#     product = serializers.SerializerMethodField('get_product_name')

#     def get_product_name(self, obj):
#         if obj.get("product_id"):
#             obj_product = Product.objects.filter(id=obj.get("product_id")).first()
#             if obj_product:
#                 return obj_product.name
#         return None


# class UserprofileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Userprofile
#         fields = ('id','name','email','password')
#         extra_kwargs = {'password' : {'write_only' :True}}

#         def create(self,validated_data):
#             user.Userprofile(
#             email.validated_data['email'],
#             name.validated_data['name']
#             )

#             user.set_password.validated_data['password']
#             user.save()
#             return user