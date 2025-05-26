# library/tests/test_services.py

import pytest
from library.services.book_service import get_book_by_id, get_borrow_history_for_book
from library.exceptions import BookNotFound, BookHasNoBorrowHistory
from django.contrib.auth.models import User
from library.models import Book, BorrowHistory

@pytest.mark.django_db
def test_get_book_by_id_success():
    # Given
    book = Book.objects.create(title='Test Book', author='Tester', isbn='1234567890123')  # (1점)

    # When
    result = get_book_by_id(book.id)  # (1점)

    # Then
    assert result == book  # (1점)
    assert result.title == 'Test Book'  # (1점)

@pytest.mark.django_db
def test_get_book_by_id_not_found():
    # When & Then
    with pytest.raises(BookNotFound) as exc_info:  # (1점)
        get_book_by_id(9999)  # (1점)

    assert "ID 9999에 해당하는 책이 없습니다." in str(exc_info.value)

@pytest.mark.django_db
def test_get_borrow_history_for_book_success():
    # Given
    user = User.objects.create(username='testuser')  # (1점)
    book = Book.objects.create(title='Test Book', author='Tester', isbn='1234567890123')  # (1점)
    BorrowHistory.objects.create(book=book, user=user)  # (1점)

    # When
    histories = get_borrow_history_for_book(book)  # (1점)

    # Then
    assert histories.count() == 1  # (1점)
    assert histories.first().user == user  # (1점)

@pytest.mark.django_db
def test_get_borrow_history_for_book_no_history():
    # Given
    book = Book.objects.create(title='Empty Book', author='Nobody', isbn='9999999999999')  # (1점)

    # When & Then
    with pytest.raises(BookHasNoBorrowHistory) as exc_info:  # (1점)
        get_borrow_history_for_book(book)  # (1점)

    assert f"'{book.title}' 도서에는 대출 이력이 없습니다." == str(exc_info.value)
