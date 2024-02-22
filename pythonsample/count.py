sent=input("enter the sentance")
v=("AEIOUaeiou")
count=0
for i in sent:
    for j in v:
        if i==j:
            count=count+1
print("total count of vowelse is:",count)
