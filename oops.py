# class Shape:
#     def __init__(Self,type):
#          self.type= type

    


# class Rectangle(Shape):
#     def __init__(self,length,width,type):
#         self.length=length
#         self.width=width
#         super().__init__(type)

#     def show(self):
#         print(self.width)
#         print(self.length)
#         print(self.type)

# class coloredREctangle(Rectangle):
#     def __init__(self,color,length,width,type):
#         self.color=color
#         super().__init(length,width)
#         # print(f"Area of trangale={self.length}*{self.width}")

# obj=coloredREctangle()
# obj.cal(10,20)




class Student:
    def __init__(self,name):
        self.name=name

class Exam(Student):
    def __init__(self,name,marks1,marks2,marks3):
         self.marks1=marks1
         self.marks2=marks2
         self.marks3=marks3
         super().__init__(name)
        
class Result(Exam):
       def __init__(self,name,marks1,marks2,marks3):
        super().__init__(name,marks1,marks2,marks3)

       def cal_total(self):
        return self.marks1+self.marks2+self.marks3
        
        
        
       def cal_avg(self):
        total=self.cal_total()
        return total/3

       def grade(self):
         avg=self.cal_avg()
         if avg >=90:
                print("A")
         elif 90>= avg >=75:
                print("B")
         elif 75>= avg  >=50:
                print("C")
         else:
          print("fail")

          print(self.cal_total)
         print(avg)

obj=Result("sourabh",78,98,78)
obj.grade()



    

