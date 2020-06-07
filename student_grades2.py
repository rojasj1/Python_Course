print("Practicing conditionals by using student grades with 'and' operator")

grade1 = float ( input("Type in the grade of 1st test: "))
grade2 = float ( input("Type in the grade of 2nd test: "))
absences = int ( input("Type in the number of absences: "))
total_classes = int ( input("Type in the total number of classes: "))

avg_grade = (grade1 + grade2)/2
attendance = (total_classes - absences)/total_classes

print("Average grade: ",round(avg_grade,2))
print("Attendance: ",str(round((attendance * 100),2))+'%')

if(avg_grade >= 6 and attendance >= 0.8):
      print("Student was approved.")

elif(avg_grade < 6 and attendance < 0.8):
      print("Student has failed due to a grade lower than 6.0 and an attendance rate lower than 80%.")       

elif(attendance >= 0.8):
     print("Student has failed due to a grade lower than 6.0.")

else:              
     print("Student has failed due to an attendance rate lower than 80%.")

