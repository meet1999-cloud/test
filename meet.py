"""
    online Candidate Voting
"""
username = ("Enter a username :")
n1 = str(input())
age = ("Enter your age :")
n2 = int(input())
if age <= 18:
    print("You can,t vote")
elif age ==18:
    print("You should have a voter id card")
else:
    print("You can vote")
print("Please Choose anyone of them")
choice = {"BJP" : 1, "MNS" : 2, "CONG" : 3, "AAP" : 4}
for i in choice:
    if choice == 1:
        break
    if choice == 2:
        break
    if choice == 3:
        break



