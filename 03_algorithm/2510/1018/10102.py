v = int(input())
vote = input()

a_count = vote.count("A")
b_count = vote.count("B")

if(a_count > b_count): print("A")
elif(b_count > a_count): print("B")
else: print("Tie")