# library/services/book_service.py

from library.models import Book, BorrowHistory
from django.shortcuts import get_object_or_404
from library.exceptions import BookNotFound, BookHasNoBorrowHistory

def get_all_books():
    return Book.objects.all()

def get_book_by_id(book_id: int) -> Book:
    try:
        return Book.objects.get(id=book_id)
    except Book.DoesNotExist: # (1점)
        raise BookNotFound(f"ID {book_id}에 해당하는 책이 없습니다.") # (1점)

def get_borrow_history_for_book(book: Book):
    histories = book.borrow_history.order_by('-borrowed_at')
    if not histories.exists(): # (1점)
        raise BookHasNoBorrowHistory(f"'{book.title}' 도서에는 대출 이력이 없습니다.") # (1점)
    return histories
