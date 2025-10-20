print("i am saim")     #act as cout  

# modules :  package or code written by anyone else but we can use it in our code like (flask , django , numpy)  can be built in or external
# pip   : act as a package manager to install modules    use as (pip install flask)
# repl  : python used to execute things on cmd terminal like calculator (read evaluate print loop)  on terminal first write python the we can print anything and use terminal as calculator directaly

# can print multiple lines 
print('''if i was a king
      name that person
      why everyone is not like me
      
    
      saim
      nidhi
      haider ali cheema
      introvert ansii
        ''')



import pyttsx3
engine = pyttsx3.init()
engine.say('''if i was a king
      name that person
      thousand of numbers
      
    
      saim
      nidhi
      haider ali 
      introvert ansii
        ''')
engine.runAndWait() 
