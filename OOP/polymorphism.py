class Person:
    count = 0

    def __init__(self, fname='', lname='', age=18):
        self.fname = fname
        self.lname = lname
        self.age = age
        Person.count += 1

    def print(self):
        print(f'{self.fname} {self.lname} ({self.age} years old)')

    @property
    def full_name(self):
        return f'{self.fname} {self.lname}'

    @classmethod
    def print_count(cls):
        print(f'{cls.count} objects created')

    @staticmethod
    def birth_year(age: int) -> int:
        from datetime import datetime as dt
        year = dt.now().year
        return year - age


class Student(Person):
    def __init__(self, fname='', lname='', age=18, group='', specialization=''):
        super().__init__(fname, lname, age)
        self.group = group
        self.specialization = specialization

    def print(self):
        super().print()
        print(f'Group {self.group}/{self.specialization}')

    @property
    def academic_info(self):
        return f'Group {self.group}, Specialization of {self.specialization}'


if __name__ == '__main__':
    trump = Student('Donald', 'Trump', 22, '051311', 'Computer science')
    trump.print()
    print(trump.full_name)
    print(Student.count)
    Student.print_count()
    print(Student.birth_year(37))
    print(trump.academic_info)