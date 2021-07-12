#variables

x = input("x: ")
y = input("y: ")
course = "this is python course"

print ("The course is :" + course.upper())

z = float(x)+float(y)
b = z // float(x)
if float(x)>float(y):
    print ("value of z: ",str(z))
    print ("value of b: ", str(b))
elif float(x)<float(y):
    print ("the condition failed")
    birth_year = input ("please enter your birth year: ")
    age = 2021 - int(birth_year)
    print("your age is", str(age))
else:
    print ("x is same as y")
    Arr = ["rahul","devansh","monika"]
    print(len(Arr))
    Arr.insert(0,"hello")
    print ("rahul" in Arr)
    
    for item in Arr:
        print(item+"*")
        for number in range(5,10,2):
            print (number)

   # numb = (1,2,3,4)
   # t = numb.count
    

    