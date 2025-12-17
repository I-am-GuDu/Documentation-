from django.contrib import admin
from .models import Submission

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','created_at')
    search_fields = ('name','email','phone')
