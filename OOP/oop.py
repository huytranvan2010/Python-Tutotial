""" Giới thiệu về class attributes, methods """
# class Dog:
#     # Nếu khai báo attribute ở đây nó sẽ dùng chung cho tất cả instance của class
#     # Thuộc tính lớp
#      species = "Phu Quoc"

#     def __init__(self, name, age):
#         # định nghĩa các attributes trong này (dùng self) thì attributes sẽ
#         # gắn với từng instance riêng biệt khi khởi tạo
#         # Thuộc tính đối tượng
#         self.name = name
#         self.age = age

#     # methods
#     def in_name(self):
#         print("Dog's name is", self.name)

# my_dog = Dog('Ni', 13)
# # thay đổi attribute chung này chỉ có ý nghĩa đối với instance hiện tại
# # Như bên dưới species của your_dog vẫn là "Phu Quoc"
# my_dog.species = 'Anh'
# print(type(my_dog))
# print(my_dog.species)
# print(my_dog.in_name())

# your_dog = Dog('Ha', 13)
# print(your_dog.species)

"""
Tính kế thừa cho phép class con kế thừa các thuộc tính và phương thức từ
các lớp khác đã được định nghĩa
"""
# class Animal:
#     def __init__(self):
#         print("Animal created")

#     def who_am_i(self):
#         print("I am an animal")

#     def eat(self):
#         print("I am eating")

# my_animal = Animal()    # khi chạy nó sẽ in ra "Animal created" luôn vì để trong phần khởi tạo

# my_animal.who_am_i()

# # class kế thừa
# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)   # kế thừa luôn phương thức khởi tạo
#         print("Dog created")

#     # có thể override method
#     def who_am_i(self):
#         print("I am a dog!")

#     # tạo method riêng
#     def action(self):
#         print("I can run!")

# mydog = Dog()

# # kế thừa phương thức
# mydog.eat()

# mydog.who_am_i()

# mydog.action()

""" Tính đa hình - different class objects can share method name
các object của các class khác nhau có thể dùng các method cùng tên nhưng với hành động khác nhau 
Hai hay nhiều lớp có phương thức giống nhau (tên) nhưng có thể thực thi khác nhau """

# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return self.name + " says woof"

# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return self.name + " says meomeo"

# mydog = Dog("Tuni")
# mycat = Cat("Hani")

# print(mydog.speak())    # trả về giá trị thì cần print, nếu trong method có print rồi thì không cần
# print(mycat.speak())

# ## Nhận thấy Cat và Dog đều có cùng tên của method 

# # Có nhiều cách giải thích tính đa hình, thử xem ví dụ sau
# for pet in [mydog, mycat]:
#     # khác class vẫn có thể trùng tên method
#     print(type(pet))
#     print(type(pet.speak))


""" abstract method - method không thực hiện gì, buộc instance của class phải định nghĩa
lại nếu muốn sử dụng """
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         raise NotImplementedError("Subclass must implement this abstract method")

# # myanimal = Animal("Hani")
# # myanimal.speak()    
# # nó báo lỗi trên ngay, do cần cần tạo class kết thừa
# # và định nghĩa lại method đó nếu muốn dùng

# class Dog(Animal):
#     # không định nghĩa constructor __init__ nó sẽ kế thừa nguyên của class mẹ
#     # do vậy khi khởi tạo phải điền đầy đủ attrubute như ở class mẹ ở phần khởi tạo
#     def speak(self):
#         return self.name + " says woof!"

# tuni = Dog("Tuni")
# print(tuni.speak())

# class Dog(Animal):
#     # không định nghĩa constructor __init__ nó sẽ kế thừa nguyên của class mẹ
#     # do vậy khi khởi tạo phải điền đầy đủ attrubute như ở class mẹ ở phần khởi tạo
#     def speak(self):
#         return self.name + " says meomeo!"

# hani = Dog("Hani")
# print(hani.speak())
     

""" Special (magic) method (còn gọi là đunẻ method do dùng 2 dấu gạch dưới
trước tên method) cho phép chúng ta sử dụng các buil in operation trong Python
như length function hay print function với object mình tạo ra """
# mylist = [1, 2, 3]
# print(len(mylist))

# class Sample:
#     pass

# mysample = Sample()
# print("Tra ve object thuoc class nao va vi tri luw: ", mysample)
# # print("Bao loi: ", len(mysample))

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

# book = Book("Python bok", "Huy", 212)

# print(book)     # khi in ra thông báo có object in memory

# """ Nên khi khi gọi hàm print() nó sẽ in ra string thể hiện book 
# Chuyển book về string là biết ngay """
# print(str(book))

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         return f"{self.title} by {self.author}"     # hoặc để string thông thường

#     # tương tự làm với len
#     def __len__(self):
#         return self.pages

#     # thêm del (xóa object)
#     def __del__(self):
#         print("The book has been deleted")  # thông báo khi xóa

# book = Book("Python book", "Huy", 212)
# print(book)    # kết quả đã khác rồi

# print(len(book))

# del book  # xóa object
# # print(book)     # đã xóa rồi không còn nữa

""" Trong OOP thường khi tạo class sẽ thêm doc strings vào ngay sau để hiển thị thông tin về class """

""" Tính đóng gói: quy tắc yêu cầu trạng thái bên trong của đối tượng được bảo vệ
và tránh truy cập từ code bên ngoài (public, protected (trong class đó và class kế thừa), private (trong chính class đó)) """


""" 
Tính đóng gói - public, private, protected 
Hạn chế quyền truy cập vào trạng thái bên trong của đối tượng. Điều này ngăn chặn dữ
liệu bị sửa đổi trực tiếp được gọi là đóng gói. Trong Python chúng ta biểu diễn thuộc
tính private bằng cách sử dụng dấu gạch dưới làm tiến tố '_', '__' 
"""

# class Computer:
#     """ create a COmputer class """
#     def __init__(self):
#         # thuộc tính private ngăn chặn sửa đổi trực tiếp
#         self.__maxprice = 900

#     def sell(self):
#         print("Giá sản phẩm: {}".format(self.__maxprice))

#     def setMaxPrice(self, price):
#         self.__maxprice = price

# c = Computer()
# c.sell()

# # Thay đổi giá trị tiếp thông qua attribute
# # Do đang để private cho thuộc tính nên không thay đổi được
# c.__maxprice = 1000
# c.sell()

# # Phải sử dụng hàm setter để thay đổi giá maxprice
# c.setMaxPrice(1000)
# c.sell()

""" Khởi tạo class computer, sử dụng __init__() để lưu giá bãn tối đa của máy tính
. Nhưng sau khi sử dụng bạn có nhu cầu sửa đổi giá, tuy nhiên không thay đổi theo. Vậy
nên để thay đổi giá trị ta sử dụng hàm setter set MaxPrice()."""

# class Person:
#     """ docs string """
#     count = 0   # class attribute

#     def __init__(self, fname, lname):
#         self.firstname = fname      # instance attribute
#         self.lastname = lname
#         Person.count += 1       # cứ khởi tạo instance thì tăng lên 1

# toi = Person("Huy", "Tran")
# ban = Person("Ni", "Tu")
# print("Class attribute: ", Person.count)
# print("Access through instance: ", toi.count)

# class Person:
#     """ docs string """
#     def __init__(self, fname, lname):
#         self.firstname = fname      # instance attribute
#         self.lastname = lname

# toi = Person("Huy", "Tran")
# toi.new_instance = "Anh"    # tạo bên ngoài chỉ riêng cho đối tượng toi
# print(toi.new_instance)
# ban = Person("Ni", "Ha")
# print(ban.new_instance)     # báo lỗi


# class Person:
#     """ docs string """
#     count = 0   # class attribute

#     def __init__(self, fname, lname):
#         self.firstname = fname      # instance attribute
#         self.lastname = lname
#         Person.count += 1       # cứ khởi tạo instance thì tăng lên 1

#     # tạo class method chú ý có @classmethod trước khi định nghĩa
#     @classmethod
#     def show_count(cls):
#         print("Có {} người trong class".format(cls.count))

# toi = Person("Huy", "Tran")
# ban = Person("Ni", "Tu")

# Person.show_count()

# class Person:
#     """ docs string """
#     def __init__(self, fname, lname):
#         self.firstname = fname      # instance attribute
#         self.lastname = lname

#     @staticmethod
#     def calculate_birth_year(age):
#         import datetime
#         year = datetime.datetime.now().year
#         return year - age

# toi = Person("anh", 'em')
# print(toi.calculate_birth_year(20))
# print("The birth year: ", Person.calculate_birth_year(30))

# class Person:

#     def __init__(self, fname, lname, age):
#         # private attribute __a
#         self.__fname = fname
#         self.__lname = lname
#         self.__age = age

#     # getter method để truy cập giá trị của attribute __age
#     def get_age(self):
#         return self.__age
#     # setter method để thay đổi giá trị cảu attribute __age
#     def set_age(self, age):
#         if age > 0 :
#             self.__age = age

#     def get_fname(self):
#         return self.__fname

#     def set_fname(self, fname):
#         if fname.isalpha():
#             self.__fname = fname
    
#     def get_lname(self):
#         return self.__lname

#     def set_lname(self, lname):
#         if lname.isalpha():
#             self.__lname = lname
        
# toi = Person("Huy", "Tran", 30)
# print(toi.get_age())

# toi.set_age(25)
# print(toi.get_age())


# class Person:

#     def __init__(self, fname: str = '', lname: str = '', age: int = 23):
#         # private attribute __a
#         self.__fname = fname
#         self.__lname = lname
#         self.__age = age

#     # getter method để truy cập giá trị của attribute __age
#     def get_age(self):
#         return self.__age
#     # setter method để thay đổi giá trị cảu attribute __age
#     def set_age(self, age):
#         if age > 0 :
#             self.__age = age

#     def get_fname(self):
#         return self.__fname

#     def set_fname(self, fname):
#         if fname.isalpha():
#             self.__fname = fname
    
#     def get_lname(self):
#         return self.__lname

#     def set_lname(self, lname):
#         if lname.isalpha():
#             self.__lname = lname
    
#     def get_name(self):
#         return self.__fname + self.__lname
        
#     first_name = property(get_fname, set_fname)
#     last_name = property(get_lname, set_lname)
#     full_name = property(get_name)
#     age = property(get_age, set_age)

# toi = Person()
# toi.first_name = "Huy"
# toi.last_name = "Tran"
# toi.age = 30

# print(toi.full_name, toi.age)


# class Person:

#     def __init__(self, fname: str = '', lname: str = '', age: int = 23):
#         # private attribute __a
#         self.__fname = fname
#         self.__lname = lname
#         self.__age = age

#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, age):
#         if age > 0 :
#             self.__age = age

#     @property
#     def first_name(self):
#         return self.__fname
#     @first_name.setter
#     def first_name(self, fname):
#         if fname.isalpha():
#             self.__fname = fname
    
#     @property
#     def last_name(self):
#         return self.__lname
#     @last_name.setter
#     def last_name(self, lname):
#         if lname.isalpha():
#             self.__lname = lname
    
#     @property
#     def full_name(self):
#         return self.__fname + self.__lname
        

# toi = Person()
# toi.first_name = "Huy"
# toi.last_name = "Tran"
# toi.age = 30

# print(toi.full_name, toi.age)

# class Person:
#     """ docs string """
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#         self._protected = True 
#         self.__private = True

#     def printname(self):
#         print(self.firstname + self.lastname)

# class Student(Person):
#     # def __init__(self, fname, lname, grade):
#     #     super().__init__(fname, lname)
#     #     self.grade = grade
#     pass

# x = Student("Mike", "Olsen")
# print(x._protected)
# print(x.__private)


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof"

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meomeo"

mydog = Dog("Tuni")
mycat = Cat("Hani")

print(mydog.speak())   
print(mycat.speak())