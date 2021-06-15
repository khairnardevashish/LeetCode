# Method to find is possible or not
def isFLoyd(num):
    count = 0
    for i in range(1,num+1):
        for j in range (1,i+1):
            count += 1
        if(count==num):
            return(True)
        elif(count>num):
            return(False)

#input
num = int(input("Enter number:"))


if(isFLoyd(num)):
    print("Yes we can.")
else:
    print("No, we can’t")