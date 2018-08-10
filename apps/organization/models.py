from django.db import models

from apps.user.models import UserModel


class OrganizationModel(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKeyField(
        UserModel, related_name='user_organizations')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'organization'
