#https://coderbyte.com/results/rashi174:Letter%20Changes:Python3

def LetterChanges(str1):
#str1='hello*3'
  list1=[]
  for item in str1:
      if item.isalpha():
          new_ord=ord(item)+1
          x=chr(new_ord)
          if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
              x=x.upper()
              list1.append(x)
          else:
              list1.append(x)
      else:
          list1.append(item)
  return "".join(list1)
print(LetterChanges(input()))