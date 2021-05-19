from django.contrib import admin

# Register your models here.
from app.models import NameMaster, Result

@admin.register(NameMaster)
class NameMasterAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("voter_name", "first_vote", "second_vote")
