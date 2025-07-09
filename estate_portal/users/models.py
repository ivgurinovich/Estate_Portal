from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.exceptions import ObjectDoesNotExist


class Role(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class CustomUserManager(UserManager):

    @staticmethod
    def _resolve_role(value):

        if isinstance(value, Role):
            return value
        try:
            return Role.objects.get(id=value)
        except (ValueError, Role.DoesNotExist):
            return Role.objects.create(name=value)

    def create_user(self, username, password, **extra_fields):
        extra_fields['role'] = self._resolve_role(extra_fields.get('role'))
        return super().create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields["role"] = self._resolve_role(value="owner")
        extra_fields["is_superuser"] = True
        extra_fields["is_staff"] = True

        return super().create_superuser(username=username, password=password, **extra_fields)


class User(AbstractUser):
    role = models.ForeignKey(Role, null=False, blank=False, on_delete=models.PROTECT)

    REQUIRED_FIELDS = ["role", "email"]

    objects = CustomUserManager()

    def is_seeker(self):
        return self.role.name == "seeker"

    def is_owner(self):
        return self.role.name == "owner"