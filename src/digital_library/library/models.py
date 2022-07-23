from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from .constants import Languages


# Create your models here.

class Author(models.Model):
  '''Author Model'''
  
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(blank=True)
  
  def __str__(self):
    return self.get_full_name()
  
  def get_full_name(self):
    return f"{self.first_name} {self.last_name}"



class Publisher(models.Model):
  '''Publisher Model'''
  
  name = models.CharField(max_length=60)
  
  def __str__(self):
    return self.name



class Book(models.Model):
  '''Book Model'''
  
  title = models.CharField(
    max_length=60,
    db_index=True,
    help_text=_("Required. 60 characters or fewer.")
  )
  language = models.CharField(
    max_length=20,
    db_index=True,
    choices=Languages.LANGUAGE_CHOICES,
    default=Languages.ENGLISH,
    help_text=_("The language in which the book is written.")
  )
  author = models.ForeignKey(
    to=Author,
    on_delete=models.CASCADE
  )
  publisher = models.ForeignKey(
    to=Publisher,
    on_delete=models.SET_NULL,
    db_index=True,
    null=True,
    blank=True,
    help_text=_("The publisher by whom this book was published.")
  )
  published_date = models.DateField(
    db_index=True,
    help_text=_("The date on which this book was published by publisher.")
  )
  assigned_user = models.ForeignKey(
    to=get_user_model(),
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    verbose_name=_('assigned to'),
    help_text=_("The user whom this book was assigned.")
  )
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  
  def __str__(self):
    return f"{self.title} - {self.author.get_full_name()}"



# class BookLog(models.Model):
#   '''Book Log'''
  
#   MAX_ISSUE_DURATION_AT_ONCE = 3
#   MAX_SUCCESSIVE_REISSUE_LIMIT = 3
#   MIN_TIME_LIMIT_FOR_REISSUE = 1
  
#   book = models.OneToOneField(
#     to=Book,
#     on_delete=models.CASCADE,
#     help_text=_("Related book id")
#   )
#   issued_to_user = models.OneToOneField(
#     to=get_user_model(),
#     on_delete=models.SET_NULL,
#     null=True,
#     verbose_name=_('issued to'),
#     help_text=_("The user whom this book was assigned.")
#   )
#   issued_duration = models.DurationField(
#     default=timedelta(days=MAX_ISSUE_DURATION_AT_ONCE),
#     editable=False
#   )
#   issued_date = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)
  
  
#   class Meta:
#     verbose_name = _('book log entry')
#     verbose_name_plural = _('book log entries')
#     db_table = 'library_books_logs'
#     ordering = ['-issued_date']
  
#   def __str__(self):
#     return f"{self.book.title} issued by {self.issued_to_user}"
  
#   def get_return_datetime(self):
#     '''
#       Returns a datetime object which indicates the return datetime of the book
      
#       Returns None if error occurs
#     '''
#     try:
#       return self.issued_date + self.issued_duration
#     except Exception as e:
#       print("LIBRARY_MODELS_BOOKLOG_GET_RETURN_DATETIME_ERROR")
#       print(e)
#       return None
  
#   def is_timelimit_exceeded(self):
#     '''
#       Returns True if the time duration after issuing the book to the user, exceeded.
      
#       Returns False otherwise
      
#       Returns None if error occurs
#     '''
#     try:
#       return self.get_return_datetime > timezone.now()
#     except Exception as e:
#       print("LIBRARY_MODELS_BOOKLOG_IS_TIMELIMIT_EXCEEDED_ERROR")
#       print(e)
#       return None
  
#   def get_remaining_duration(self):
#     '''
#       Returns a datetime.timedelta object which shows the remaining duration since the book was issued by the user
      
#       Returns a datetime.timedelta object with value 0 if the time limit is exceeded.
      
#       Returns -1 if error occurs
#     '''
#     try:
#       if not self.is_timelimit_exceeded():
#         return self.get_return_datetime() - timezone.now()
#       return timedelta()
#     except Exception as e:
#       print("LIBRARY_MODELS_BOOKLOG_GET_REMAINING_DURATION_ERROR")
#       print(e)
#       return -1
  
#   def is_reissuable(self):
#     '''
#     Returns True if a user can make a successive issue of the same book
    
#     Returns False otherwise.
    
#     Returns None if error occurs.
#     '''
    
#     # 1. Check if the maximum limit for re-issue exceeded 
#     # 2. Can only re-issue if the remaining duration is not more than 24hrs. 
    
#     try:
#       return self.issued_duration < timedelta(days=self.MAX_ISSUE_DURATION_AT_ONCE*self.MAX_SUCCESSIVE_REISSUE_LIMIT) and self.get_remaining_duration() < timedelta(days=self.MIN_TIME_LIMIT_FOR_REISSUE)
#     except Exception as e:
#       print("LIBRARY_MODELS_BOOKLOG_CAN_REISSUE_ERROR")
#       print(e)
#       return None
  
#   def reissue(self):
#     '''
#     Returns True if issue_duration updated successfully
    
#     Returns False otherwise
    
#     Returns None if error occurs
#     '''
#     try:
#       if self.is_reissuable():
#         self.issued_duration += timedelta(days=self.MAX_ISSUE_DURATION_AT_ONCE)
#         return True
#       return False
#     except Exception as e:
#       print("LIBRARY_MODELS_BOOKLOG_REISSUE_ERROR")
#       print(e)
#       return None
  
#   def reissue_and_save(self):
#     '''
#     Returns True if re-issued and saved successfully
    
#     Returns False otherwise
    
#     Returns None if error occurs
#     '''
#     try:
#       if self.reissue():
#         self.save()
#         return True
#       return False
#     except Exception as e:
#       print("LIBRARY_MODELS_BOOKLOG_REISSUE_AND_SAVE_ERROR")
#       print(e)
#       return None
