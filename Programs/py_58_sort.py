# sort() method = used with lists
# sorted() function = used with iterables
 
# sort() method ---------------------------------------------------------------
students_1 = ["shubham", "suraj", "Tushar", "Praveen", "Saurabh", "Nanshu"]

students_1.sort()
# students_1.sort(reverse=True)

for i in students_1:
    print(i)

# sorted() function -----------------------------------------------------------
students_2 = ("Abhishek", "vaibhav", "Vansh", "Abhay", "Vivek")

sorted_students = sorted(students_2)
# sorted_students = sorted(students_2, reverse=True)

for i in sorted_students:
    print(i)