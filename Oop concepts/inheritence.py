# class car:
#     def __init__(self,windows,doors,engineType):
#         self.windows=windows
#         self.doors=doors
#         self.engineType=engineType

    
#     def drive(self):
#         print(f"Person will drive the {self.engineType} car  ")


# car1 =car(4,5,"Petrol")
# car1.drive()


# class teslaCar(car):
#    def __init__(self,windows,doors,engineType,self_Drive):
#        super().__init__(windows,doors,engineType)
#        self.self_Drive=self_Drive
 
#    def selfDriving(self):
#         print(f"This car supports self driving : {self.self_Drive}  ")
        
       
# tesla1=teslaCar(2,2,"electric",True)
# tesla1.selfDriving()   
       
       
   

# base classs
class vehicle:
    def __init__(self,brand,wheels):
        self.brand=brand
        self.wheels=wheels

    def showInfo(self):
        print(f"car brand is : {self.brand} and have wheels :{self.wheels} ")

    def drive(self):
        print(f"driving a generic car ..")



# single inheritence
class car(vehicle):
    def __init__(self, brand,engineType, wheels,doors,windows):
        super().__init__(brand, wheels)
        self.engineType=engineType
        self.doors=doors
        self.windows=windows

    def drive(slef):
        print(f"car is :{slef.engineType} and made by brand :{slef.brand} ")



class tesla(car):
    def __init__(self, brand, engineType, wheels, doors, windows,slefDrive):
        super().__init__(brand, engineType, wheels, doors, windows)
        self.selfDrive=slefDrive

    def drive(self):
        super().drive()
        if self.selfDrive:
            print("this car supports elf drive ")



# hierarichal inheritence
class bike(vehicle):
    def __init__(self, brand, wheels,cc):
        super().__init__(brand, wheels)
        self.cc=cc

    def drive(self):
         print(f"Riding a {self.cc}cc bike made by {self.brand}.")



class electricBike(bike):
    def __init__(self, brand, wheels, cc,electric):
        super().__init__(brand, wheels, cc)
        self.electric=electric

    def drive(self):
        super().drive()
        if self.electric:
             print(f"Riding an electric bike by {self.brand}.")




print("----- Single Inheritance -----")
car1 = car("Toyota","Petrol", 4, 4,4 )
car1.showInfo()
car1.drive()

print("\n----- Multilevel Inheritance -----")
tesla1 = tesla("Tesla","electric", 4, 4,4 ,True)
tesla1.showInfo()
tesla1.drive()

print("\n----- Hierarchical Inheritance -----")
bike1 = bike("Honda",2, 150)
bike1.showInfo()
bike1.drive()

print("\n----- Multilevel Inheritance -----")
ebike=electricBike("honda",2,250,True)
ebike.drive()





    

    

        