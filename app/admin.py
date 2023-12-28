from django.contrib import admin
from app.models import Author, JobPost, Location, Skills

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'salary', 'date')
    list_filter = ('title', 'salary', 'date', 'expiry')
    search_fields = ('title', 'description', 'salary')
    search_help_text = "Search for title, description or salary"
    # fields = (('title', 'salary'), 'description', 'expiry') 
    # exclude = ('title', 'expiry')
    fieldsets = (
        ('Job Info', {
            'fields': (('title', 'salary'), 'description')
        }),
        ('More Info', {
            'classes': ('collapse', 'wide'),
            'fields': ('expiry', 'slug')
        }),
    )
    
admin.site.register(JobPost)
admin.site.register(Author)
admin.site.register(Skills)
admin.site.register(Location)
