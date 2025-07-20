import pytest
from library import Library

@pytest.fixture
def lib():
    l = Library()
    l.addbooks(1, "The Alchemist", "Paulo Coelho")
    l.addbooks(2, "1984", "George Orwell")
    return l


def test_add_books():
    lib = Library()
    assert lib.addbooks(1, "Dune", "Frank Herbert") == "'Dune' added to the library."
    assert "already exists" in lib.addbooks(1, "Duplicate", "Nobody")


def test_list_books(lib):
    listing = lib.listbooks()
    assert "The Alchemist" in listing
    assert "1984" in listing
    assert "Available" in listing


def test_borrow_books(lib):
    assert lib.borrowbooks(1) == "Borrowed"
    assert lib.books[0].is_borrowed is True

    assert "already borrowed" in lib.borrowbooks(1)

    assert "not found" in lib.borrowbooks(999)


def test_return_books(lib):
    lib.borrowbooks(2)
    assert lib.returnbooks(2) == "Returned"
    assert lib.books[1].is_borrowed is False

    assert "was not borrowed" in lib.returnbooks(1)


    assert "not found" in lib.returnbooks(999)
