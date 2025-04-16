marks = int(input("enter marks = "))
if (marks >= 90 and marks<=100):
    Grade = "A"
elif(marks >=80 and marks >= 70):
    Grade = "B"
elif(marks>=70 and marks >= 30):
    Grade = "C"
else:
    Grade = "D"
    
print("grade is ", Grade)
    