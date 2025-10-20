# method overriding (inheritence)

class animal():
    def speak(self):
        return "sound of the animal "
    
    
class dog(animal):
    def speak(self):
        return "wow wow "
    

class cat(animal):
    def speak(self,name):
        p_sound=super().speak()
        return f"{name} says Meow Meow and {p_sound} "

    
      

a=animal()
print(a.speak())

d=dog()
print(d.speak())

c=cat()
print(c.speak("bella"))

# why use polymorphism 
l=[animal(),dog(),cat()]
for a in l:
    print(a.speak()  if not isinstance(a, cat) else a.speak("Bella"))
      