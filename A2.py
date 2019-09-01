import csv
from statistics import mean 

resT = [] #nonlocal
resF = []
resOS = []
aboveavglist = [] #list
def display_item_stock_level_above_certain_amount():
    reader = csv.DictReader(open("data.csv"))
    inputthreshold = int(input("Enter amount : ")) 
    for row in reader:
    
      if (int(row['STOCK LEVEL']) > inputthreshold):
         aboveavglist.append(row['PRODUCT ID'])
         aboveavglist.append(row['NAME'])
         aboveavglist.append(row['STOCK LEVEL'])
    return aboveavglist

def display_categories_average():
    reader = csv.DictReader(open("data.csv"))
    for row in reader:

      if row['CATEGORY'] == "Technology":
         resT.append(int(row['STOCK LEVEL']))
         avgT = mean(resT) 
      elif row['CATEGORY'] == "Furniture":
         resF.append(int(row['STOCK LEVEL']))
         avgF = mean(resF)     
      else:
         resOS.append(int(row['STOCK LEVEL']))
         avgOS = mean(resOS)
    return avgT, avgF, avgOS

def menu():
   print(s)
   print("Welcome to Inventory System")
   print(s)
   print("1: Display category average level")
   print("2: Display item stock level above certain amount")
   print("0: Exit")

#print(resT)   
#print(avgT)
#print(second_dict)
#print(aboveavglist)
#print(row["CATEGORY"])
s = "==================================================="
n = 0
while (n < 7):
   menu()
   print(s)
   userinput = int(input("Enter choice: "))
   if userinput == 1:
      avgT, avgF, avgOS = display_categories_average()
      print(s)
      print("Display category average level")
      print(s)
      print("Technology : {0}".format(avgT)) 
      print("Furniture : {0}".format(avgF)) 
      print("Office Supplies : {0}".format(avgOS))
      continue
   elif userinput == 2:
      print(s)
      # getting length of list
      display_item_stock_level_above_certain_amount()
      length = len(aboveavglist) 
      # Iterating the index 
      # same as 'for i in range(len(list))' 
      for i in range(length): 
          print(aboveavglist[i]) 
      aboveavglist.clear() 
      continue
   elif userinput > 2:
      print("Invalid choice, please enter again")
      continue
   else: 
      print(s)
      print("Thank you for using Inventory Query System")
      break #consistent indentation 