from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.core.serializers import serialize
# Create your views here.
from rest_framework.decorators  import api_view
from rest_framework.response import Response
from rest_framework import status
# from test_app.serializers import ProductsSerializer
from rest_framework import generics
from . import models
from . import serializers

class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
   

def index(request):
    return render(request, "users/index.html")

# @api_view(['GET'])
# def list_products(request):
#     response_data = {}
#     response_data["data"] = ProductSerializer(
#                                     [{"program": i} for i in [1, 2, 3]],
#                                    many=True
#                                 ).data
#     return Response(response_data, status=status.HTTP_200_OK)
    
# def index(request):
#             responseData = {
#                 'id': 4,
#                 'name': 'Test Response',
#                 'roles' : ['Admin','User']
#             }
        
#             return JsonResponse(responseData)
    
# def index(request):
#             template = loader.get_template('index.html')
#             context = {
#                 'hello':"world"
#             }
#             return HttpResponse(template.render(context, request)) 
        
            


# def index(request):
#     data = serializers.serialize('json', Product.objects.all())
#     return HttpResponse(data, content_type='application/json')






# def index(request):

#     return JsonResponse(responseData)
