class multifunction():
    
    def oddeven():
        num=int(input("enter a number"))
        if (num%2==0):
            msg=print(num," is Even number")
        else:
            msg=print(num," is odd number")
        return msg
    
    def area_perimeter_triangle():
        height1=int(input("enter Height1"))
        height2=int(input("enter Height2"))
        breath=int(input("enter Breath"))
        area=(height1*breath)/2
        perimeter=height1+height2+breath
        print("Height: %d \nHeight: %d  \nBreath: %d" %(height1,height2,breath))
        print("area=",area)
        print("perimeter=",perimeter)
#        return area,perimeter

    def eligibilityformarriage():
        age=int(input("Enter the Age"))
        gender=input("Enter your gender")
        if (age>18 and gender=="Female"):
            print ("your Gender: ",gender)
            print("your age: ",age)
            print("Eligible")
        elif (age>21 and gender=="Male"):
            print("your gender: ",gender)
            print("your age: ",age)
            print(" Eligible")
        else:
            print("Not Eligible")    

            
    def subfields():
        SubfieldsInAI=["Machine Learning","Neural Networks","Vision","Robotics","Sppech Processing","Natural Language Processing"]
        print ("Sub-fields in AI are")
        for subAI in SubfieldsInAI:
            print(subAI)

    def percentage():
        mark1=int(input("Enter mark for subject1"))
        mark2=int(input("Enter mark for subject2"))
        mark3=int(input("Enter mark for subject3"))
        mark4=int(input("Enter mark for subject4"))
        mark5=int(input("Enter mark for subject5"))
        
        print("subject1 :",mark1)
        print("Subject2 :", mark2)
        print("Subject3 :", mark3)
        print("Subject4: ", mark4)
        print("Subject5: ", mark5)
        total=mark1+mark2+mark3+mark4+mark5
        percent=total/5 
            
        print("total: ",total)
        print("Percentage: ",percent )