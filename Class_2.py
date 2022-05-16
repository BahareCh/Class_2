#This code ask for name and grade and save them with the ability to delete and update the data 
My_Dictionary={}

while True:
    
    name= input ( "Enter your name")
    grade= int( input ( "Enter your grade"))
    if grade>100:
        print (" wrong value")
    else: 
        A= int(input(" if you want to add name write 0, if you want to search write 1"))
        Delete_upload= (input ("if you want to delete write D"))
         
    if Delete_upload == "D":
        My_Dictionary.pop(name)
         
         

               #add name
    if A==0:
            My_Dictionary[name] = grade
            print (My_Dictionary)         
                       #search name
            
    if A==1:
                        #print (My_Dictionary[name])
            Searching_name = input ("Search a name")
            print (My_Dictionary.keys)
            

          
    
    
