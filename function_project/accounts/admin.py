from django.contrib import admin
from .models import(
  Users, UserActivateTokens
)
# Register your models here.
admin.site.register(
  [Users, UserActivateTokens]
)