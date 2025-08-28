from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from typing import Optional
import os


class Command(BaseCommand):
    help = 'Creates an admin user with username guilherme.silveira and password 123456'

    def handle(self, *args: tuple, **options: dict) -> None:
        if os.environ.get('DJANGO_ENV') != 'development':
            self.stdout.write(self.style.ERROR(
                'This command can only be run in the development environment.'
            ))
            return

        username = 'guilherme.silveira'
        password = '123456'
        
        # Check if user already exists
        try:
            user = User.objects.get(username=username)
            self.stdout.write(
                self.style.WARNING(f'User {username} already exists')
            )
            
            # Check if user is already staff and superuser
            if user.is_staff and user.is_superuser:
                self.stdout.write(
                    self.style.SUCCESS(f'User {username} is already an admin')
                )
                return
            
            # Make existing user admin
            user.is_staff = True
            user.is_superuser = True
            user.save()
            
            self.stdout.write(
                self.style.SUCCESS(f'User {username} is now an admin')
            )
            
        except User.DoesNotExist:
            # Create new admin user
            user = User.objects.create_user(
                username=username,
                password=password,
                is_staff=True,
                is_superuser=True
            )
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully created admin user {username}'
                )
            )
