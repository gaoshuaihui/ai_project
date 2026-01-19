class Book:
    """图书类"""

    def __init__(self, title, author, isbn):
        """
        初始化图书
        :param title: 书名
        :param author: 作者
        :param isbn: ISBN编号
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False  # 默认未借出

    def borrow_book(self):
        """借书操作"""
        if self.is_borrowed:
            print(f"《{self.title}》已被借出")
            return False
        else:
            self.is_borrowed = True
            print(f"成功借阅《{self.title}》")
            return True

    def return_book(self):
        """还书操作"""
        if not self.is_borrowed:
            print(f"《{self.title}》未被借出")
            return False
        else:
            self.is_borrowed = False
            print(f"成功归还《{self.title}》")
            return True


class Library:
    """图书馆管理类"""

    def __init__(self):
        """初始化图书馆，创建空的图书列表"""
        self.books = []

    def add_book(self, book):
        """
        添加图书到图书馆
        :param book: Book对象
        """
        self.books.append(book)
        print(f"已添加图书: 《{book.title}》 by {book.author}")

    def find_book_by_title(self, title):
        """
        根据书名查找图书
        :param title: 书名
        :return: 找到的Book对象，如果不存在返回None
        """
        for book in self.books:
            if book.title == title:
                return book
        print(f"未找到书名为《{title}》的图书")
        return None

    def borrow_book(self, title):
        """
        借阅图书
        :param title: 书名
        """
        book = self.find_book_by_title(title)
        if book:
            book.borrow_book()

    def return_book(self, title):
        """
        归还图书
        :param title: 书名
        """
        book = self.find_book_by_title(title)
        if book:
            book.return_book()


# 使用示例
if __name__ == "__main__":
    # 创建图书馆实例
    library = Library()

    # 添加图书
    book1 = Book("Python编程从入门到实践", "Eric Matthes", "978-7-115-46302-6")
    book2 = Book("算法图解", "Aditya Bhargava", "978-7-115-44765-1")
    book3 = Book("深入理解计算机系统", "Randal E. Bryant", "978-7-111-59586-7")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # 借阅图书
    library.borrow_book("Python编程从入门到实践")
    library.borrow_book("算法图解")

    # 再次尝试借阅已借出的图书
    library.borrow_book("Python编程从入门到实践")
    # 归还图书
    library.return_book("Python编程从入门到实践")

    # 尝试借阅不存在的图书
    library.borrow_book("不存在的书")