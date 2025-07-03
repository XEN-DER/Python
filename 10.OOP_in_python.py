'''Object oriented programming in Python
=====================================
features of OOP
we can create classes and objects
1. Interitance (reusability of code)
2. Encapsulation (hiding the data)
3. Polymorphism (same function name with different implementation)
4. Abstraction (hiding the complexity of code)

#Class in python
'''

class Student:
    #condtructor is a function of class which is called immedietly after creating object (automatically)
    def __init__(self,student_name,usn_no,course):
        self.student_name = student_name
        self.usn_no = usn_no
        self.course = course

    def print_details(self):
        print(f'''name = {self.student_name} usn_no = {self.usn_no} course = {self.course}''')
        
#creating object of class
student1 = Student("Bhawesh", "1RV18CS001", "Python")
student2 = Student("Hemanth", "1RV18CS002", "Python")
student3 = Student("Sahu", "1RV18CS003", "Python")
#accessing the attributes of class
print(student1.student_name)
print(student1.usn_no)
print(student1.course)
print(student2.student_name)
print(student2.usn_no)
print(student2.course)
print(student3.student_name)
print(student3.usn_no)
print(student3.course)
#calling the method of class
student1.print_details()
student2.print_details()
student3.print_details()


'''
Task
Create a class laptop with attributes like processor, ram , gpu , brand

print details

(extra)
change_processor
change_ram
change_gpu
change_brand
'''
class laptop(Student):
    def __init__(self, student_name, usn_no, course, processor, ram, gpu, brand):
        super().__init__(student_name, usn_no, course)
        self.processor = processor
        self.ram = ram
        self.gpu = gpu
        self.brand = brand

LOQ= laptop("Bhawesh", "1RV18CS001", "Python", "Intel i5", "8GB", "NVIDIA GTX 1650", "Dell")
LOQ.print_details()
print(f'''Processor: {LOQ.processor}, RAM: {LOQ.ram}, GPU: {LOQ.gpu}, Brand: {LOQ.brand}''')