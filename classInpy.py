from main import my as my_Function , lists as main_list 

class AmbujaCiment : 
    def __init__(self) :
        self._ciement = "Ambuja"     
        self.__power = 100
        self.__slogan = "Ghar ek hi bar banta hai"
        
        # @property
        # def ciement(slef):
        #     return slef.__ciement
        
        
class DrFixit : 
    def __init__(self) -> None:
        self.ciement = "DrFixit"     
        self.power = 90
        self.slogan = "Dr Fixit kare Fix"
    
    def __delattr__(self, __name: str) -> None:
        pass 

class Quick : 
    def __init__(self) -> None:
        # return "Quick kya hai muje nahi pata"
        print("Quick kya hai muje nahi pata")
    
class Wall :
   armor = 0
   height = 0
   def __init__(self , armor= 100 , height=100) -> None:
        self.armor = armor
        self.height = height
        print("I am Constructor")

def main():
    wall = Wall()
    print(f"Constructor without any arguments{wall.armor} , {wall.height}")
    wall2 = Wall(10,10)
    print(f"Constructor with both arguments{wall2.armor} , {wall2.height}")
    wall3 = Wall(10)
    print(f"Constructor with armor value(without height value){wall3.armor} , {wall3.height} ")
    
    quick = Quick()
    print(quick)


main()

# this main is from another file 


my_Function("Form Another file ??? Yehh  babay")

print(main_list)
