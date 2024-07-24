file = open("india.txt","r")
content  = file.read()
content = content.lower()
count = content.count('india')
print("occurance of India in india.txt",count)


print("<---------------------------------------------------------------------------------------->")

file=open("story.txt",'r')
lines=file.readlines()
file.close()
count=0
lines_starting_with_t = []
for line in lines:
    if line.startswith('T'):
        count+=1
        lines_starting_with_t.append(line.strip())
    
print(f"Number of lines starting with 'T': {count}")
for line in lines_starting_with_t:
  print(line)



print("<---------------------------------------------------------------------------------------->")
# enter  studants rollno,name and marks till the user wants


import pickle


with open('stu.dat', 'wb') as file:
    while True:
        
        rollno = input("Enter student roll number: ")
        name = input("Enter student name: ")
        marks = float(input("Enter student marks: "))

        student_data = {
            'rollno': rollno,
            'name': name,
            'marks': marks
        }

    
        pickle.dump(student_data, file)

        
        another = input("Do you want to enter another student's data? (yes/no): ").strip().lower()
        if another != 'yes':
            break

print("Data has been written to stu.dat")
