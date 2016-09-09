print("Hello and welcome to calc.")
start=true
num1=input("Put in first number.")
num2=input("Type second number.")
oper=raw_input("type operator")
if(start=true):
if (oper.lower()=="+") : 
    ans=num1+num2
elif(oper.lower()=="-"):
    ans=num1-num2
elif(oper.lower()=="/"):
    ans=num1/num2
elif(oper.lower()=="*"):
    ans=num1*num2
else:
    print("you dun derped")
print('{} is da answer'.format(ans))
again=raw_input("Dost thou wish to calculate repeatedly?")
if(again.lower()=="no"):
    print("Thank you for abandoning me")
    start=false
elif(again.lower()=="yes"):
    start=true
else:
    print("noobface")