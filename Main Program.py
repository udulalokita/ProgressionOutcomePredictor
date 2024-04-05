#assigning variables
pass_credit = 0
defer_credit = 0
fail_credit = 0
outcome_1='Progress'
outcome_2='Progress(module trailer)'
outcome_3='Module retriever'
outcome_4='Exclude'
list1 = []
output = ''

#main program
def begin():
    
    done=False
    while not done:
        try:
     
            pass_credit=int(input('Please enter your credits at PASS:'))
            if pass_credit not in [0,20,40,60,80,100,120]:
                  print('Out of range')
                  print()
                  
           
            defer_credit=int(input('Please enter your credit at DEFER:')) 
            if defer_credit not in [0,20,40,60,80,100,120]:
                    print('Out of range')
                    print()

                    
            
            fail_credit=int(input('Please enter your credit at FAIL:')) 
            if fail_credit not in [0,20,40,60,80,100,120]:
                    print('Out of range')
                    print()


             
            if (pass_credit+defer_credit+fail_credit) != 120:
                            output = 'Total incorrect'
                            done=True
                            print('Total incorrect')
                            print()

                        
            if pass_credit==120 and defer_credit==0 and fail_credit==0:
                            output = 'Progress'
                            print(output)
                            done=True
                            outcome_count.append(outcome_1)
                            print()


            elif pass_credit==100 and defer_credit<=20 and fail_credit<=20:
                            output = 'Progress (module trailer)'
                            print(output)
                            done=True
                            outcome_count.append(outcome_2)
                            print()


            elif pass_credit<=80 and defer_credit<=120 and fail_credit<=60 :
                            output = 'Module retriever'
                            print(output)
                            print()

                            done=True
                            outcome_count.append(outcome_3)

            elif pass_credit<=40 and defer_credit<=40 and fail_credit>=80 : 
                            output = 'Exclude'
                            print(output)
                            done=True
                            outcome_count.append(outcome_4)

            results = output + " -" + str(pass_credit) + "," + str(defer_credit) + "," + str(fail_credit)
            list1.append(results)


        except ValueError:
                print('Integer required.')


print()
outcome_count=[]
begin()
print()


print("Would you like to enter another set of data? ")
ask_input=input("(Enter 'y' for yes or 'q' to quit and view results):")
ask_input=ask_input.lower()
    
print()

while ask_input=='y':
    begin()
    
    print()
    print("Would you like to enter another set of data? ")
    ask_input=input("(Enter 'y' for yes or 'q' to quit and view results):")
    ask_input=ask_input.lower()
    print()

#histogram
else:
    if ask_input=='q':

        print("-" * 40)
        print('Histogram')
        
        progress=outcome_count.count(outcome_1)
        print('Progress',progress,' :','*'*progress)
           
        trailer=outcome_count.count(outcome_2)
        print('Trailer',trailer,'  :','*'*trailer)
        
        retriever=outcome_count.count(outcome_3)
        print('Retriever',retriever,':','*'*retriever)
        
        exclude=outcome_count.count(outcome_4)
        print('Exclude',exclude,'  :','*'*exclude)
        print()
        
        total=progress+trailer+retriever+exclude
        print(total,'outcomes in total.')

        print("-" * 40)

#making the list & saving into text file
        print()
        print("Part 2:")
        fo = open("save_text.txt","w")
        for c in list1:
            print(c)
            fo.write(c + "\n")
        fo.close()

#asking user whether requires to retrieve saved data in the text file
        print()
        choice = input("Enter 'y' for yes for retrieve data from text file or 'q' to quit : ")
        print()
        choice = choice.upper()

#retrieving data from text file
        if choice =="Y":
                print("data retrieved from text file :")
                print()
                fo = open("save_text.txt","r")
                data = fo.read()
                print(data)
                fo.close()
            
                
#ending the program
        elif choice == "Q":
                print("End of the program")
                exit()

        
            

    
