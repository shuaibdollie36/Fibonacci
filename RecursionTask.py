terms = int(input("How many terms: "))
#Terms
b1, b2 = 0, 1
count = 0
#check if valid
if terms <= 0:
  print ("Enter a postive integer")
elif terms == 1:
  print ("Sequence Fibonacci",terms,":")
  print(b1)
else:
  print ("Sequence Fibonacci:")
  while count < terms:
      print(b1, end=" ")
      nth = b1 + b2
      b1 = b2
      b2 = nth
      count += 1



