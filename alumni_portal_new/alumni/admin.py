from django.urls import path
from django.contrib import admin
from django.shortcuts import render, redirect
from .models import Alumni  # Import the correct model name

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Event
@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ('user','batch', 'department', 'position', 'company', 'contact')
    search_fields = ('user__username', 'batch', 'company')
    list_filter = ('batch', 'department', 'company')



admin.site.site_header = "Alumni Portal Admin"
admin.site.index_title = "Admin Dashboard"
admin.site.site_title = "Alumni Portal"

from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect

def admin_home_redirect(request):
    return redirect('/admin/dashboard/')

urlpatterns = [
    path("dashboard/", admin_home_redirect),
]

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
