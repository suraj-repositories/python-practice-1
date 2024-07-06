# sort() method = used with lists
# sorted() function = used with iterables

# ----------------------------- sort() method --------------------------------

students = [("Shubham", "F", 60), 
            ("Suraj", "A", 33),
            ("Tushar", "D", 36), 
            ("Praveen","B",20),
            ("Vaibhav", "C", 78)]

# grade = lambda grades : grades[1]
# students.sort(key = grade, reverse=True)

# for i in students:
#     print(i)

age = lambda ages : ages[2]

students.sort(key = age, reverse=True)  # we are passing a function object as an argument


# for i in students:
#     print(i)


# ----------------------------- sorted() function --------------------------------

students = (("Shubham", "F", 60), 
            ("Suraj", "A", 33),
            ("Tushar", "D", 36), 
            ("Praveen", "B", 20),
            ("Vaibhav", "C", 78))

age = lambda ages:ages[1]
sorted_students = sorted(students, key=age)     # you can also use reverse

for i in sorted_students:
    print(i)