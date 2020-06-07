print("Practicing conditionals by using student grades with 'and' & 'or' operator followed by error handling")

data_valid = False
while data_valid == False:
      grade1 = input("Type in the grade of 1st test: ")
      try:
          grade1 = float(grade1)
      except:
             print("Invalid Entry. Only numbers and decimals(.) are accepted.")
             continue


      if grade1 < 0 or grade1 > 10:
          print("Grade should be between 0 and 10")
          continue
      else:
         data_valid = True


data_valid = False
while data_valid == False:
      grade2 = input("Type in the grade of 2nd test: ")
      try:
              grade2 = float(grade2)
      except:
             print("Invalid Entry. Only numbers and decimals(.) are accepted.")
             continue

      if grade2 < 0 or grade2 > 10:
          print("Grade should be between 0 and 10")
          continue
      else:
         data_valid = True




data_valid = False
while data_valid == False:
      total_classes = input("Type in the total number of classes: ")
      try:
        total_classes = int(total_classes)
      except:
              print("Invalid Entry")
              continue

      if total_classes <= 0:
          print("The number of classes cant be zero or less")
          continue
      else:
         data_valid = True





data_valid = False

while data_valid == False:
      absences = input("Type in the number of absences: ")
      try:
          absences = int(absences)
      except:
              print("Invalid Entry")
              continue


      if absences < 0 or absences > total_classes:
          print("The number of absences cant be less than 0 or greater than the number of total classes")
          continue
      else:
         data_valid = True




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

