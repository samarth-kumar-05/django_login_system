# users/backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CustomUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print(f'Authenticating with username: {username}')

        UserModel = get_user_model()
        user = get_user_model().objects.get(username=username)
        print('here '+str(user.check_password(password)))
        print(user.password)


        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            try:
                user = UserModel.objects.get(username=username)
                print(f'User  found with username: {username}')
            except UserModel.DoesNotExist:
                print(f'User not found with username: {username}')

                return None
            
        if user.is_active :
            print(f'active status successful for username: {username}')
        else:
             print(f'active status failed for username: {username}')
            

        if user.check_password(password):
            print(f'check_password parameters - username: {username}, password: {password}')

            print(f'Authentication successful for username: {username}')
            return user
        else:
            print(f'check_password parameters - username: {username}, password: {password}')
            print(f'Authentication failed for username: {username}')
            return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
