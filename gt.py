message = "hello dave, goog night"
message[::-1]
print(message[::-1])

message = "dave yah, good afternoon"
message[10]
print(message[:10]+"...")

# lists allow dupplicates
names = [ "Dvid", "Mercy", "Emma"]
names2 = ["Muwanguzi", "Benja", "Julius"]
names.extend(names2)
names

print("WELCOME STUDENT")
students = ["henry", "denze"]

print("\n---MENU---")
print("1. Add student")
print("2. list of students")
print("3. delete student")
print("4. exit")
choice = input("your choice 1-4: ")

if choice=="1":
    print("add student.Type 'q' to stop)")
    while True:
        name = input("Enter student name: ")
        if name.lower() == 'q':
            break
        students.append(name)
        print(name,"added!")
elif choice=="2":
    print("List of students:")
    for student in students:
        print(student)
elif choice=="3":
    print("Delete student")
    name = input("Enter student name to delete: ")
    if name in students:
        students.remove(name)
        print(name,"deleted!")
    else:
        print(name,"not found!")
elif choice=="4":
    print("Goodbye!")
else:
    print("Invalid choice. Please select 1-4.")



words = ['abc', 'xyz', 'abc', '1221']
count=0
for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        count = count + 1 # add 1 to count
        print(word, "matches") 

print("\nTotal count:", count)

