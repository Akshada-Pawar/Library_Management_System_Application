import unittest
import Library

class TestLibrary(unittest.TestCase):

    def test1(self):
        result = Library.add_book(Python, C, C++, JAVA)
        self.assertEqual(result,Python, C, C++, JAVA)

    def test2(self):
        result = :ibrary.display_books(Python, C, C++, JAVA)
        self.assertEqual(result, Python, C, C++, JAVA)

    def test3(self):
        result = Library.lend_book(C++)
        self.assertEqual(result, C++)

    def test4(self):
        result = Student.borrow_book(Akshada,C,library)
        self.assertEqual(result,Akshada,C)

    def test5(self):
        result = Student.return_book(Akshada, C,library)
        self.assertEqual(result, Akshada, C)

    def test6(self):
        result = Student.students_with_books(name,books)
        self.assertEqual(result,name,books)

if __name__ == '__main__':
    unittest.main()