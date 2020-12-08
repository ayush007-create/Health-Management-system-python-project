import datetime
x=datetime.datetime.now()
print("***welcome to your health management system***")
name=input("who are you : ")
if name.lower()=="rohan":
    activity = input("Okay!great so what are you looking for food or exercise : ")
    action = input("So you want to add something or retrieve something : ")
    if activity.lower()=="food":
        if action.lower()=="add":
            file1=open("rohan_food.txt","a")
            print("you can now write your food plan\n")
            file1.write(str([str(x)])+":"+input("Enter what you ate : ")+"\n")
            print("Written successfully!!")
            file1.close()
        elif action.lower()=="retrieve":
            print("So here is your food plan\n")
            file1=open("rohan_food.txt","r")
            print(file1.read())
            file1.close()
    elif activity.lower()=="exercise":
        if action.lower()=="add":
            file2=open("rohan_exercise.txt","a")
            print("you can now write your exercise plan\n")
            file2.write(str([str(x)])+":"+input("Enter what you did : ")+"\n")
            print("written successfully!!")
            file2.close()
        elif action.lower()=="retrieve":
            file2=open("rohan_exercise.txt","r")
            print("So here is your exercise plan\n")
            print(file2.read())
            file2.close()
elif name.lower()=="harry":
    activity = input("Okay!great so what are you looking for food or exercise : ")
    action = input("So you want to add something or retrieve something : ")
    if activity.lower()=="food":
        if action.lower()=="add":
            file3=open("harry_food.txt","a")
            print("you can now write your food plan\n")
            file3.write(str([str(x)])+":"+input("Enter what you ate : ")+"\n")
            print("written successfully!!")
            file3.close()
        elif action.lower()=="retrieve":
            file3=open("harry_food.txt","r")
            print("So here is your food plan\n")
            print(file3.read())
            file3.close()
    elif activity.lower()=="exercise":
        if action.lower()=="add":
            file4=open("harry_exercise.txt","a")
            print("you can now write your exercise plan\n")
            file4.write(str([str(x)])+":"+input("Enter what you did : ")+"\n")
            print("written successfully!!")
            file4.close()
        elif action.lower()=="retrieve":
            file4=open("harry_exercise.txt","r")
            print("So here is your exercise plan\n")
            print(file4.read())
            file4.close()
elif name.lower()=="hamad":
    activity = input("Okay!great so what are you looking for food or exercise : ")
    action = input("So you want to add something or retrieve something : ")
    if activity.lower()=="food":
        if action.lower()=="add":
            file5=open("hamad_food.txt","a")
            print("you can write now your food plan\n")
            file5.write(str([str(x)])+":"+input("Enter what you ate : ")+"\n")
            print("written successfully!!")
            file5.close()
        elif action.lower()=="retrieve":
            file5=open("hamad_food.txt","r")
            print("So here is your food plan\n")
            print(file5.read())
            file5.close()
    elif activity.lower()=="exercise":
        if action.lower()=="add":
            file6=open("hamad_exercise.txt","a")
            print("you can now write your exercise plan\n")
            file6.write(str([str(x)])+":"+input("Enter what yoy did : ")+"\n")
            print("written successfully!!")
            file6.close()
        elif action.lower()=="retrieve":
            file6=open("hamad_exercise.txt","r")
            print("So here is your exercise plan\n")
            print(file6.read())
            file6.close()
else:
    print("Sorry you are not in records\n")
print("Thanks for visiting\n")
print("****Stay healthy,Stay fit*****")
