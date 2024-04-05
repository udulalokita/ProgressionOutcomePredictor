# assigning variables
dictionary = {}
ask_input = "y"
progression = []



while ask_input == "y":
    print()
    student_id = input("Enter Student ID: ")
    
    try:
        pass_credit = int(input("Enter the number of credits at PASS: "))
        if pass_credit not in [0,20,40,60,80,100,120]:
            print("Out of range")
            print()
            continue

        defer_credit = int(input("Enter the number of credits at DEFER: "))
        if defer_credit not in [0,20,40,60,80,100,120]:
            print("Out of range")
            print()
            continue

        fail_credit = int(input("Enter the number of credits at FAIL: "))
        if fail_credit not in [0,20,40,60,80,100,120]:
            print("Out of range")
            print()
            continue

    except creditError:
        print("Integer required")
        continue

    if (pass_credit+defer_credit+fail_credit) != 120:
        output = 'Total incorrect'
        print("Total incorrect")
        print()
        continue

    elif pass_credit==100 and defer_credit<=20 and fail_credit<=20:
        output1 = 'Progress (module trailer)'
        print(output1)
        print()

    elif pass_credit<=80 and defer_credit<=120 and fail_credit<=60 :
        output1 = "Module retriever"
        print(output1)
        print()

    elif pass_credit<=40 and defer_credit<=40 and fail_credit>=80 :
        output1 = "Exclude"
        print(output1)
        print()

    else:
        output1 = "Progress"


    progression.append([student_id, output1, pass_credit, defer_credit, fail_credit])
    dictionary[student_id]= output1,pass_credit,defer_credit,fail_credit

    print()
    print("Would you like to enter another set of data?")
    ask_input = input("Enter 'y' for yes or 'q' to quit and view results: ")
    ask_input.lower()
    
    if ask_input == "q":
        print()
        print("End of the program.")
        break

print("-" * 40)
print()
print("Part 4:")

for key,credit in dictionary.items():
    print(f"{key}: {credit[0]} - {credit[1]}, {credit[2]}, {credit[3]} ",end=" ")

