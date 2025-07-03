#Types od Arguments in Python

#positional Arguments
def greet(student,trainer):
    print(f"Hello {student}, your trainer is {trainer}")
    
#keyword Arguments
greet(student="Bhawesh", trainer="Ritvik")
    

# Args

def print_number(*args):
    for i in args:
        print(i)
# This function takes a variable number of arguments and prints each one
print_number(1, 2, 3, 4, 5,4,5,6,3,636,3,636,34,34,53,5,5,356,467,474678,2435,23,346,)  # This will print each number from 1 to z

#kwargs

def print_number(**kwargs):
 for i in kwargs.keys():
     print(i)
     for i in kwargs.values():
         print(i)
     for k,v in kwargs.items():
        print(f"keys{k} : values{v}")
# This function takes a variable number of arguments and prints each one
print_number(trainer="Ritvik" , student1="Hemanth",student2="Bhawesh",student3="sahu",
             student4="pragathi",Grade=True,subject="Python",Marks=9.5) 
# This will print each keyword argument passed to the function

