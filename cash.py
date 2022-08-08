# cash.py
'''
Please read Readme.md
Class CashRegister has the following methods:

1. purchase_item() - acctepts object RetaiItem as an argument and add it to the internal list.
2. get_total() - returns total cost of all objects from the internal list in the class CashRegister.
3. show_items() - displays data of all objects RetailItem stored in internal list of class CashRegister.
4. clear() - removes content of internal list of objects in the class CashRegister.
'''
# to save list of objects to the file
import pickle

class CashRegister:
    def __init__(self):
        # initialize the attributes  
        self.objectRetailItem = ''
        self.totalCost = 0
        
        try:
            inputFile = open('list.dat', 'rb')
            self.objectList = pickle.load(inputFile)
            inputFile.close()
        # if the file doesn't exist
        except FileNotFoundError: 
            self.objectList = []
            
        # initializing totalCosts
        # if not self.objectList == '':
        #     self.totalCost = 0
            
        #     for cost in self.objectList:
        #         self.totalCost += cost.get_price()

        # else:
       
    # setters
    #
    def purchaseItem(self, objectRetailItem):
        
        self.objectRetailItem = objectRetailItem
        # add object to the list
        self.objectList.append(self.objectRetailItem)
        # saving list to the file
        outputFile = open('list.dat', 'wb')
        pickle.dump(self.objectList, outputFile)
    
    # getters
    #
    
    #returns internal list of all objects
    def listObjects(self):
        return self.objectList
    
    # returns total cost of all products/ objects from the list
    def get_total(self):

        # iterate through the list with the all created objects
        for item in self.objectList:
            self.totalCost += (item.get_price()*item.get_quantity())
    
        return self.totalCost

    # display data of all objects
    def showItems(self):
        # display object's data from __str(self)__
        for data in self.objectList:
            print(data)
    
    # clear interanl list saved in the file list.dat
    def clear(self):
        self.objectList = []
        outputFile = open('list.dat','wb')
        pickle.dump(self.objectList, outputFile)
        
        
        
        
            
        
    
    