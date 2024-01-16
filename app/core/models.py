'''
Database models
'''

from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class CategoryItems(models.Model):
    # category_item_id = models.AutoField(primary_key= True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    
    class Meta:
       managed = False
       unique_together = ('category', 'item')
       db_table = 'category_items'
       


class Category(models.Model):
    """categories table model"""
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    category_name_id = models.IntegerField(unique=True, null=False)
    category_rank = models.IntegerField(unique = True, null=False)
    category_image_url = models.CharField(
    max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    items = models.ManyToManyField('Item', through='CategoryItems')

    class Meta:
        managed = False
        db_table = 'categories'


class FoodType(models.Model):
    """food_type model"""
    food_type_id = models.AutoField(primary_key=True)
    food_type_name = models.CharField(unique=True, null=False, max_length=100)

    class Meta:
        managed = False
        db_table = 'food_type'


class Item(models.Model):
    """Item table model"""
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(unique=True, null=False, max_length=100)
    item_description = models.CharField(max_length=100, null=True, blank=True)
    item_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False)
    item_type = models.ForeignKey(
        FoodType, on_delete=models.SET_NULL, null=True)
    item_image_url = models.CharField(
        max_length=255, null=True, blank=True)
    cgst = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    sgst = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    is_active = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, through='CategoryItems')

    class Meta:
        managed = False
        db_table = 'items'
