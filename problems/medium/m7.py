def student_record_menu():
    students = {}  # Dictionary to store student records

    while True:
        print("\n1. Add Student Record")
        print("2. Display All Records")
        print("3. Search Student by Roll Number")
        print("4. Delete Student Record")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            roll = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            marks = input("Enter Marks: ")
            students[name] = (roll, marks)  
        elif choice == 2:
            for details in students.keys():
                print(details," : roll no",students[details][0],"mark ",students[details][1])  
        elif choice == 3:
            roll = input("Enter Roll Number to Search: ")
            for i in students.values():
                if roll in i[0] or [1]:
                    print( next( j for j in students.keys() if students[j][0] == roll))
                else:
                    print("Record not Found")   
        elif choice == 4:
            roll =input("Enter Roll Number to Delete: ")
            a=""
            for i in students:
                
                if students[i][0]==roll:
                    a+=i
                else:
                    print("record not found")
            del students[a]
            print(students)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid Choice")
student_record_menu()
