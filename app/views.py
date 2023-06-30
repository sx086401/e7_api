import json
from django.views import View
from django.http import JsonResponse
from app.models import Users
from app import forms

# Create your views here.

class UserView(View):
    def get(self, request):
        users = Users.objects.all()
        user_data = list(users.values('name', 'is_active'))

        return JsonResponse({'users': user_data})

    def post(self, request):
        try:
            request_data = json.loads(request.body)
            form = forms.UserForm(request_data)
            if (form.is_valid()):
                user = Users.objects.create(name=form.cleaned_data['name'], password=form.cleaned_data['password'])
                return JsonResponse({'message': 'User created successfully', 'user_id': user.id})
            else:
                return JsonResponse({'error': form.errors}, status=400)
        except:
          return JsonResponse({'error': 'Bad Request'}, status=400)
