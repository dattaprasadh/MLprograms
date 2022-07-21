# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

print("number of shoes")
X = int(input())# number of shoes
sizes=list(map(int, input().split()))
print("number of customer")
n=int(input())
sizes=Counter(sizes)
pr=0

for i in range (n):
    sz,pz=map(int,input().split())
    
