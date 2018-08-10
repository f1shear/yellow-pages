from django.db import models


class CountryModel(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'country'


class RegionModel(models.Model):
    country = models.ForeignKey(CountryModel, related_name='regions')
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'region'


class CategoryModel(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'category'


class SubCategoryModel(models.Model):
    category = models.ForeignKey(CategoryModel, related_name='sub_categories')
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'sub_category'
