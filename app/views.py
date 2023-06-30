import json
from django.views import View
from django.http import JsonResponse
from app.models import Users
from app import forms

# Create your views here.

class UserListView(View):
    http_method_names = ['get']

    def get(self, request):
        users = Users.objects.all()
        user_data = list(users.values('name', 'is_active'))

        return JsonResponse({'users': user_data})

class CreateUserView(View):
    http_method_names = ['post']

    def post(self, request):
        name = request.POST.get('name')
        password = request.POST.get('password')
        print(request)
        is_passed = forms.UserForm.is_valid(request.POST)
        print(is_passed)
        user = Users.objects.create(name=name, password=password)

        return JsonResponse({'message': 'User created successfully', 'user_id': user.id})
