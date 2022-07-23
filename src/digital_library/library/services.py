from .models import Book
from .constants import Languages

def create_book(title, language, author, published_date, publisher=None, assigned_user=None):
  try:
    if not language:
      raise ValueError('language can not be an empty str or of None type')
    if language not in Languages.LANGUAGE_LIST:
      raise ValueError(f'{language} language is not supported')
    book = Book.objects.create(title=title, language=language, author=author, published_date=published_date, publisher=publisher, assigned_user=assigned_user)
  except ValueError as e:
    print("LIBRARY_SERVICES_CREATE_BOOK_VALUE_ERROR")
    print(e)
    return False
  except Exception as e:
    print("LIBRARY_SERVICES_CREATE_BOOK_ERROR")
    print(e)
    return False


if __name__ == '__main__':
  create_book('aaa', None, None, None)
  pass