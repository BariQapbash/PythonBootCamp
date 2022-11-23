
def maxNum(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return  num1
    elif num2>num1 and num2>=num3:
        return num2
    else:
        return num3

print(maxNum(400,50,6))

def compareString (str1,str2,str3):
    if str1 == str2 or str2 == str3 or str1 == str3:
        return print("there is some word equal to other")
    else:
        return print("there is no word equal to others")

compareString("Bari","Filora","Bari")