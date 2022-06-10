"""
    online Candidate Voting
"""
user_name = input("Please enter username: ")
age = int(input("Please enter age: "))
print("User Name", user_name)
print("Age", age)
if age < 18:
    print("You can,t vote")
    exit()
elif age == 18:
    print("You should have a voter id card")
else:
    print("You can vote")
choice = {"BJP" : 1, "MNS" : 2, "CONG" : 3, "AAP" : 4}
user = int(input(f"Please Choose anyone of them {choice}"))
print("user", user)
if user == 1:
    print("you choose BJP")
elif user == 2:
    print("you choose MNS")
elif user == 3:
    print("you choose CONG")
elif user == 2:
    print("you choose AAP")
print("Thank you for choosing")




