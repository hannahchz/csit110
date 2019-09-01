#Hannah Chua 6276325 CSIT110-L02 
import csv

#isInstance returns true or false
def checkType(a_list, typ):
    return all(isinstance(element, typ) for element in a_list)

def sumthis(list1):
    total = 0
    for i in list1: 
        if isinstance(i, int)==True: 
           total += i 
    return total

#convert list elements to integers
def numbers(list2):
    for i in range(0, len(list2)): 
        list2[i] = int(list2[i]) 
    return list2

def switch_demo(argument):
    switcher = {
        0: "J", #char
        1: "Z",
        2: "I",
        3: "H",
        4: "G",
        5: "F",
        6: "E",
        7: "D",
        8: "C",
        9: "B",
        10: "A",
    }
    return switcher.get(argument, "Invalid last letter, should be A-J/Z")

sku_list = []
multiply_list = [2, 7, 6, 5, 4, 3, 2 ]
num_list = []
mysum = 0 
def isValidSKUFormat(sku):
        sku_list = list(sku) #convert string to list of char
        eight_element = sku_list.pop()  #char
        #try except ValueError:
        #print(eight_element)
        #print(sku_list)
        if (eight_element != " "): #in excel file 123456D has len = 8, because last char is a whitespace. Could have changed if condition to len(sku) !=7 if this was not the case
           numbers(sku_list)
           num_list = map(lambda x,y:x*y,sku_list,multiply_list)
           num_list1 = list(map(int,num_list))
           #map object python 3.0
           mysum = sumthis(num_list1) #row 1 : 89 
           #print(mysum)
           index_no = mysum % 11
           correct_eight_element = switch_demo(index_no)
           if (eight_element != correct_eight_element):
                return "Invalid last letter, last letter should be " + str(correct_eight_element)
           else: 
                return "SKU is in valid format"
        else:
           return "Should have 7 leading integers"

def isValidSKUFormat_2():
    reader = csv.DictReader(open("data.csv"))
    print('{0:<10}{1:^15}{2:<40}'.format('SKU      | ', ' PRODUCT ID      |',' Invalid reason')) 
    for row in reader:
        print('{0:<10}{1:^20}{2:<40}'.format(row['SKU'], row['PRODUCT ID'],isValidSKUFormat(row['SKU'])))

isValidSKUFormat_2()

#Question 3
#Valid Test Cases:
#    Argument         Expected Result   Actual Result    Reason
#                     Invalid           Invalid         Missing SKU
#    2222222C         True              True            First seven digit is integer and last digit is from A-J,Z
#Invalid Test Cases:
#    Argument         Expected Result   Actual Result    Reason
#    12345J           Invalid           Invalid          First seven digits are integer
#    12345678J        Invalid           Invalid          Length should be 8
#    12345678         Invalid           Invalid          Last Character is not Letter
#    1234567P         Invalid           Invalid          Last Character is Letter from A-J,Z


  
