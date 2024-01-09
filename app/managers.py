from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self,username,email,password=None,**extra_fields):

        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):

        # extra_fields.setdefault('is_active', True)
        # extra_fields.setdefault("is_staff",True)
        # extra_fields.setdefault("is_superuser",True)

        # return self.create_user(email, username, password, **extra_fields)
        user = self.create_user(username, email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user