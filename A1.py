#Hannah Chua 6276325 CSIT110-L02 
import csv

filePath= "data.csv"
with open (filePath) as csvfile:
   reader = csv.DictReader(csvfile)
   sku = input("Enter SKU:")
   while (sku == ' '):
       print ("Empty input, please enter again")
       sku = input("Enter SKU:")
   for row in reader:
         if sku == row['SKU']:
              new_string = "=================" *4
              print ("{0:<10}{1:<30}\n".format("ROW","NAME"))
              print("{0:<10}{1:<30}\n".format(row['ROW'], row['NAME']))
              print (new_string)
              print ("Details")
              print (new_string)
              print ("{0:<15}{1:<30}\n".format("PRODUCT ID: ", row['PRODUCT ID']))
              print ("{0:<15}{1:<30}\n".format("CATEGORY: ", row['CATEGORY']))
              print ("{0:<15}{1:<30}\n".format("SUB-CATEGORY: ", row['SUB-CATEGORY']))
              print ("{0:<15}{1:<30}\n".format("STOCK LEVEL: ", row['STOCK LEVEL']))
              
   if sku != row['SKU']:
       print ("No inventory record found")

          


                               
                  
