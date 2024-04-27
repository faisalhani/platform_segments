from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group, Permission

class CustomUser(AbstractUser):
    # Add your custom fields here

    class Meta:
        permissions = [
            ("my_custom_permission", "My custom permission")
        ]
        default_permissions = ()

    # Provide custom related names for the groups and user_permissions fields
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')
