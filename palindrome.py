num=int(input("Enter the input"))
original=num
return=0
while num<0:
  digit=num%10
  reverse=reverse * 10+digit
  num=num//10
if original==reverse:
  print("It is Palindrome")
else:
  print("Its not Palindrome")
  
  
