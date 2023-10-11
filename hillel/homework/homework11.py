class Person:
    __name: str = "no name"
    __age: int = 18

    def __init__(self, name: str = None, age: int = None) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"Name: {self.__name}; age: {self.__age}"

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        if 2 < len(name) < 20:
            self.__name = name
        else:
            print("Incorrect name!")

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age) -> None:
        if 17 <= age <= 100:
            self.__age = age
        else:
            print("Incorrect age!")

    def show_info(self) -> None:
        print(f"Name - {self.__name}, age - {self.__age}")

    def say_hello(self):
        print(f"Hello! My name is {self.__name}.")


class Subject:
    __name: str = "no name"

    def __init__(self, name: str = None) -> None:
        self.name = name

    def __repr__(self) -> str:
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if 2 < len(name) < 20:
            self.__name = name
        else:
            print("Incorrect name subject!")


class Teacher(Person):
    __subject: Subject = None

    def __init__(self, name, age, subject: Subject):
        super().__init__(name, age)
        self.subject = subject

    def __repr__(self) -> str:
        return super().__repr__() + f"; Subject: {self.__subject}"

    @property
    def subject(self) -> Subject:
        return self.__subject

    @subject.setter
    def subject(self, subject) -> None:
        self.__subject = subject

    def say_hello(self) -> None:
        super().say_hello()
        print(f"I teach {self.__subject}.")

    def show_info(self) -> None:
        super().show_info()
        print(f"Subject: {self.__subject}")


class Student(Person):
    __academy: str = "no academy"
    __group: str = "no group"

    def __init__(self, name, age, academy, group):
        super().__init__(name, age)
        self.academy = academy
        self.group = group

    def __repr__(self) -> str:
        return super().__repr__() + f"; Academy: {self.__academy}; Group: {self.__group}"

    @property
    def academy(self) -> str:
        return self.__academy

    @academy.setter
    def academy(self, academy) -> None:
        if 2 < len(academy) < 100:
            self.__academy = academy
        else:
            print("Incorrect name academy!")

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group) -> None:
        if 2 < len(group) < 20:
            self.__group = group
        else:
            print("Incorrect name group!")

    def say_hello(self) -> None:
        super().say_hello()
        print(f"I'm studying in {self.__academy} academy. My group is {self.__group}")

    def show_info(self) -> None:
        super().show_info()
        print(f"Academy: {self.__academy}; Group: {self.__group}")


class Aspirant(Student, Person):

    __specialization = "no specialization"

    def __init__(self, name, age, academy, group, specialization):
        Student.__init__(self, name, age, academy, group)
        Person.__init__(self, name, age)
        self.specialization = specialization

    @property
    def specialization(self) -> str:
        return self.__specialization

    @specialization.setter
    def specialization(self, specialization):
        if 4 < len(specialization) < 20:
            self.__specialization = specialization
        else:
            print("Incorrect name specialization!")

    def say_hello(self) -> None:
        super().say_hello()
        print(f"My aspirant specialization is {self.__specialization}")


class Academy:
    __name: str = "no name"
    __address: str = "no address"
    __students: list[Student] = list()
    __teachers: list[Teacher] = list()
    __count_students: int = 0
    __count_teachers: int = 0

    def __init__(self, name: str = None, address: str = None) -> None:
        self.name = name
        self.address = address

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        if 3 <= len(name) < 100:
            self.__name = name
        else:
            print("Incorrect name!")

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address) -> None:
        if 3 <= len(address) < 100:
            self.__address = address
        else:
            print("Incorrect address!")

    @property
    def students(self) -> list[Student]:
        return self.__students

    @property
    def teachers(self) -> list[Teacher]:
        return self.__teachers

    @property
    def count_students(self) -> int:
        return self.__count_students

    @property
    def count_teachers(self) -> int:
        return self.__count_teachers

    def add_student(self, student: Student = None) -> None:
        self.__students.append(student)
        self.__count_students += 1

    def add_teacher(self, teacher: Teacher = None) -> None:
        self.__teachers.append(teacher)
        self.__count_teachers += 1

    def show_info(self):
        print(f"Academy: {self.__name}, address: {self.__address}, count students {self.__count_students}")


person_1 = Person("David", 17)
person_1.say_hello()

student_1 = Student("Tom", 19, "NTU DP", "Group 1")
student_2 = Student("Jack", 20, "NTU DP", "Group 2")
student_1.say_hello()

academy_1 = Academy("NTU DP", "Dnipro, av. Dmytra Yavornytskoho, 19")
academy_1.show_info()

academy_1.add_student(student_1)
academy_1.add_student(student_2)
academy_1.show_info()
print(academy_1.students)

subject_1 = Subject("Mathematics")
subject_2 = Subject("Geography")

print(subject_1)
print(subject_2)

teacher_1 = Teacher("Olga Petrivna", 40, subject_2)
teacher_2 = Teacher("Valeriy Semenovych", 51, subject_1)
teacher_1.show_info()

academy_1.add_teacher(teacher_1)
academy_1.add_teacher(teacher_2)

print(academy_1.count_teachers)
print(academy_1.teachers)

aspirant_1 = Aspirant("Vladislav", 23, "NTU DP", "Asp-3", "Economic")
aspirant_1.say_hello()


