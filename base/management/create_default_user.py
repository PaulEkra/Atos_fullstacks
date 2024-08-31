import os
import django

# Configurer les paramètres Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class CreateDefaultUser:


    def create_default_user(self, username, password):
        if User.objects.filter(username=username).exists():
            print('Default user already exists')
            return
        try:
            user=User.objects.create_user(username)
            user.save()
            user.password=password
            user.set_password(user.password)
            user.save()
            print('Default user created')
        except Exception as e:
            print(f"Default user creation failed : {e}")
