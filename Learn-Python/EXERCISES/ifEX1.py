marks = int(input("Enter your test mark percentage:"))
if marks > 90:
    print("Your grade is A")
if marks > 80 and marks <=90:
    print("Your grade is B")
if marks >= 60 and marks <=80:
    print("Your grade is C")
if marks <60:
    print('Your grade is D')