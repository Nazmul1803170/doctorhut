from django.contrib.auth.base_user import BaseUserManager



class UserManager(BaseUserManager):
    use_in_migrations = True



    def create_user(self, email,password=None, **extra_fields):
        if not email:
            raise ValueError('Email is require')

        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password, **extra_feilds):
        extra_feilds.setdefault('is_staff', True)
        extra_feilds.setdefault('is_superuser', True)
        extra_feilds.setdefault('is_active', True)

        if extra_feilds.get('is_staff') is not True:
            raise ValueError('jhbasdh')

        return self.create_user(email, password, **extra_feilds)