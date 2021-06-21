class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:


x = Person("John", "Doe")
x.printname()

""" Tạo class kế thừa từ class Person """


class Student(Person):
    pass    # khi ko muốn add thêm attribute hay methods nào, kế thừa toàn bộ base class


x = Student("Mike", "Olsen")
x.printname()


class Student(Person):
    def __init__(self, fname, lname):
        # có self ở đây để còn lưu attribute cho object
        Person.__init__(self, fname, lname)


x = Student("John", "Doe")
x.printname()

# thêm attribute
class Student(Person):
    def __init__(self, fname, lname, age):
        # có self ở đây để còn lưu attribute cho object
        # Phải dùng self không sẽ báo lỗi
        Person.__init__(self, fname, lname)
        self.age = age

    def printage(self):
        print(self.age)


x = Student("John", "Doe", 15)
x.printname()
x.printage()

# sử dụng super() function sẽ làm cho class con kế thừa tất cả phương thức và thuộc tính của class cha
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        # sử dụng super sẽ không cần tên của class cha, ở đây ko cần dùng self

anh = Student("Huy", "Tran")
anh.printname()