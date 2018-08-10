from apps.user.models import UserModel
from apps.core.models import SubCategoryModel
from apps.core.models import OrganizationModel
from apps.core.models import RegionModel
from django.contrib.gis.db import models


class PostModel(models.Model):
    POST_TYPE_CHOICES = (
        ('offer', 'Offer'),
        ('required', 'Required'),
    )
    sub_category = models.ForeignKey(
        SubCategoryModel, related_name='sub_category_posts')
    region = models.ForeignKey(RegionModel, related_name='region_posts')
    location = models.PointField()  # address from google maps
    organization = models.ForeignKey(
        OrganizationModel, related_name='organization_posts')
    posted_by = models.ForeignKey(UserModel, related_name='user_posts')
    posted_at = models.DateTimeField(auto_now_add=True)
    post_type = models.CharField(max_length=255, choices=POST_TYPE_CHOICES)

    class Meta:
        db_table = 'post'
