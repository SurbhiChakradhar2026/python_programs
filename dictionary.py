from collections import Counter
#car = input("Enter the string value :")
car = "aaaavvfdsfdsfgdgdx"
count_occurenc = Counter(car)
for keys,values in count_occurenc.items() : 
     print(f"{keys}{values}",end="")
               
      






