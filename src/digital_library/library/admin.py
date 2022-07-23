from django.contrib import admin
from .models import (
  Author,
  Publisher,
  Book,
  # BookLog
)

# Register your models here.
admin.site.register((
  Author,
  Publisher
))

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  '''Book Admin'''
  list_display = ('title', 'author', 'language', 'published_date', 'assigned_user_id')
  list_filter = ('language', 'published_date')


# @admin.register(BookLog)
# class BookLogAdmin(admin.ModelAdmin):
#   '''Book Log Admin'''
#   list_display = ('book', 'issued_to_user_id', 'issued_date')
#   list_filter = ('issued_date', 'issued_duration')