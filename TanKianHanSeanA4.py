#!/usr/bin/env python
# coding: utf-8

# In[1]:


# name Tan Kian Han Sean
#student number 10200997
#subject code CSIT110

#Error checking 1
#Check for invalid menu choice selection.
#The program will check if the user had entered 1 2 or 3 in the main menu selection.
#If an invalid choice is enter, the user is asked to re-enter the choice again.
#program notify repeated SKU that entered again for insertion.
#if wrong choice is made then program go to Main menu.
# if user wants to delete with invalid SKU number then program notify for invalid SKU number

import csv
#store 4 columns of codes.csv into 4 lists
CATEGORY=[]
CATEGORY_CODE=[]
SUB_CATEGORY=[]
SUB_CATEGORY_CODE=[]
#store 6 columns of data.csv into 2 lists and one record is saving on parallel indexes.

SKU=[]
PRODUCT_ID=[]
NAME=[]
data_category=[]
data_sub_category=[]
data_stock_level=[]
def Read_data_into_lists():#function to read codes.csv and data.csv into lists
    #print("===============================================")
    filePath="codes.csv"
    #print("===============================================")
    with open(filePath) as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            CATEGORY.append(row['CATEGORY'])
            CATEGORY_CODE.append(row['CATEGORY_CODE'])
            SUB_CATEGORY.append(row['SUB-CATEGORY'])
            SUB_CATEGORY_CODE.append(row['SUB-CATEGORY_CODE'])
    filePath="data.csv"
    #print("===============================================")
    with open(filePath) as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            
            SKU.append(row['SKU'])
            PRODUCT_ID.append(row['PRODUCT ID'])
            NAME.append(row['NAME'])
            data_category.append(row['CATEGORY'])
            data_sub_category.append(row['SUB-CATEGORY'])
            data_stock_level.append(row['STOCK LEVEL'])
            
def save_files():#saves final lists of SKU and PRODUCT_ID into data.csv
    filePath = "data.csv"        
    with open(filePath, 'w', newline='') as csvfile:
        fieldnames = ['ROW','SKU', 'PRODUCT ID','NAME','CATEGORY','SUB-CATEGORY','STOCK LEVEL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        i=0
        while i<len(SKU):#loop to go to each index and saves
            writer.writerow({'ROW':i+1,'SKU': SKU[i],'PRODUCT ID': PRODUCT_ID[i],'NAME':NAME[i],'CATEGORY':data_category[i],'SUB-CATEGORY':data_sub_category[i],'STOCK LEVEL':data_stock_level[i]})#saving line by line
            i=i+1

def display_and_runs_program():#control flow of program
    print("================================================")
    print("Welcome to Inventory Management System")
    
    while (True):#main loop that runs until user wants
        print("================================================")
        print("1: Insert a new item")#displaying menu
        print("2: Delete an item")
        print("3: Save data to file and exit")
        choice=input("Enter choice:")#user enter choice
        if choice=="":
            continue
        elif choice=="1":#if user picks 1
            print("================================================")
            print("Insert a new item")
            print("================================================")
            
            while(True):#checks that user press enter button means empty string
                sku_input=input("Enter SKU:")
                if len(sku_input)!=0:
                    break
            i=0
            checking_sku=True
            while i<len(SKU):#checking that SKU is already exist or not
                if sku_input==SKU[i]:
                    print("SKU is already exist,Please try again with new SKU.")
                    checking_sku=False
                    break
                i=i+1
            if checking_sku==False:
                continue
            print("Choose a Category:")#displaying category menu
            print("1:Technology")
            print("2:Furniture")
            print("3:Office Supplies")
            while(True):
                category_input=input("Enter a Category:")
                if len(category_input)!=0:
                    break
            input_validate=""
            category_code=""
            input_validate_sub=""
            if category_input=="1":
                          input_validate="Technology"
                          CATEGORY_CODE="TEC"
                          
                          
            elif category_input=="2":
                          input_validate="Furniture"
                          CATEGORY_CODE="FUR"
            elif category_input=="3":
                          input_validate="Office Supplies"
                          CATEGORY_CODE="OFF"
            else: 
                print("Wrong Category")
                continue
            i=0
            sub_input=""
            while i<len(CATEGORY):
                if input_validate==CATEGORY[i]:
                    if input_validate=="Technology":
                        print("\nChoose a Sub Catgory:")
                        print("1:Accessories")
                        print("2:Phones")
                        print("3:Copier")
                        print("4:Machines")
                        while(True):
                            sub_input=input("Enter a Sub Category:")
                            if len(sub_input)!=0:
                                break
                        
                        if sub_input=="1":
                            input_validate_sub='Accessories'
                            sub_input="AC"
                        elif sub_input=="2":
                            input_validate_sub='Phones'
                            sub_input="PH"
                        elif sub_input=="3":
                            input_validate_sub='Copier'
                            sub_input="CO"
                        elif sub_input=="4":
                            input_validate_sub='Machines'
                            sub_input="MA"
                        else:
                            print("Wrong Sub Category")
                            break
                        
                        while(True):
                            #checking length of product id is equal to 8 other wise takes input again
                            product_id_input=input("\nEnter product ID:")
                            if len(product_id_input)==8:
                                break
                                
                        while(True):#checks that user press enter button means empty string
                            product_name_input=input("\nEnter product name:")
                            if len(product_name_input)!=0:
                                break    
                        while(True):#checks that user press enter button means empty string
                            stock_level_input=input("\nEnter stock level:")
                            if len(stock_level_input)!=0:
                                break
                        SKU.append(sku_input)
                        PRODUCT_ID.append(CATEGORY_CODE+"-"+sub_input+"-"+product_id_input)
                        NAME.append(product_name_input)
                        data_stock_level.append(stock_level_input)
                        data_category.append(input_validate)
                        data_sub_category.append(input_validate_sub)
                        #print(sku_input, CATEGORY_CODE+"-"+sub_input+"-"+product_id_input)
                        print("\nNew item inserted")
                        break
                    elif input_validate=="Furniture":
                        print("\nChoose a Sub Catgory:")
                        print("1:Chairs")
                        print("2:Tables")
                        print("3:Bookcase")
                        while(True):#checks that user press enter button means empty string
                            sub_input=input("Enter a Sub Category:")
                            if len(sub_input)!=0:
                                break
                        if sub_input=="1":
                            sub_input="CH"
                            input_validate_sub='Chairs'
                        elif sub_input=="2":
                            input_validate_sub='Tables'
                            sub_input="TA"
                        elif sub_input=="3":
                            input_validate_sub='Bookcase'
                            sub_input="BO"
                        else:
                            print("Wrong Sub Category")
                            break
                        while(True):#checks that user press enter button means empty string
                            product_id_input=input("\nEnter product ID:")
                            if len(product_id_input)==8:
                                break
                                
                        while(True):#checks that user press enter button means empty string
                            product_name_input=input("\nEnter product name:")
                            if len(product_name_input)!=0:
                                break    
                        while(True):#checks that user press enter button means empty string
                            stock_level_input=input("\nEnter stock level:")
                            if len(stock_level_input)!=0:
                                break
                        SKU.append(sku_input)
                        PRODUCT_ID.append(CATEGORY_CODE+"-"+sub_input+"-"+product_id_input)
                        NAME.append(product_name_input)
                        data_stock_level.append(stock_level_input)
                        data_category.append(input_validate)
                        data_sub_category.append(input_validate_sub)
                        #print(sku_input, CATEGORY_CODE+"-"+sub_input+"-"+product_id_input)
                        print("\nNew item inserted")
                        break
                    elif input_validate=="Office Supplies":
                        print("\nChoose a Sub Catgory:")
                        print("1:Appliances")
                        print("2:Stationery")
                        print("3:Binders")
                        while(True):#checks that user press enter button means empty string
                            sub_input=input("Enter a Sub Category:")
                            if len(sub_input)!=0:
                                break
                        if sub_input=="1":
                            sub_input="AP"
                            input_validate_sub='Appliance'
                        elif sub_input=="2":
                            input_validate_sub='Stationery'
                            sub_input="ST"
                        elif sub_input=="3":
                            input_validate_sub='Binders'
                            sub_input="BI"
                        else:
                            print("Wrong Sub Category")
                            break
                        while(True):
                            product_id_input=input("\nEnter product ID:")
                            if len(product_id_input)==8:
                                break
                                
                        while(True):#checks that user press enter button means empty string
                            product_name_input=input("\nEnter product name:")
                            if len(product_name_input)!=0:
                                break    
                        while(True):#checks that user press enter button means empty string
                            stock_level_input=input("\nEnter stock level:")
                            if len(stock_level_input)!=0:
                                break
                        SKU.append(sku_input)
                        PRODUCT_ID.append(CATEGORY_CODE+"-"+sub_input+"-"+product_id_input)
                        
                        NAME.append(product_name_input)
                        data_stock_level.append(stock_level_input)
                        data_category.append(input_validate)
                        data_sub_category.append(input_validate_sub)
                        #print(sku_input, CATEGORY_CODE+"-"+sub_input+"-"+product_id_input)
                        print("\nNew item inserted")
                        break
                    #print("================================================")
                i=i+1
            
        
        elif choice=="2":
            print("================================================")
            print("Delete an item")
            print("================================================")
            while(True):##checks that user press enter button means empty string
                sku_delete=input("Enter sku to delete:")
                if len(sku_delete)!=0:
                    break
            i=0
            go=True#############
            while i<len(SKU):#loop on list and delete Item
                if SKU[i]==sku_delete:
                    SKU.pop(i)
                    PRODUCT_ID.pop(i)
                    NAME.pop(i)
                    data_stock_level.pop(i)
                    data_category.pop(i)
                    data_sub_category.pop(i)
                    print("Item deleted")
                    go=False
                    break
                i=i+1
            if go==True:#if no SKu exist then this if executes
                print("No Such SKU exists.")
        elif choice=="3":#saving files
            print("================================================")
            print("Save file")
            save_files()#calling function
            print("================================================")
            print("File saved")
            print("================================================")
            print("================================================")
            print("Thank you for using Inventory Management System")
            print("================================================")
            break
        else:
            print("Wrong input")
            
    
Read_data_into_lists()
display_and_runs_program()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




