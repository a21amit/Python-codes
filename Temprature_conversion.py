#defining a function.
def converter():
    #asking for temp.
    temp= float(input(' What\'s the temprature in Kelvin: '))
    c=273-temp
    print('Temprature in celsius is '+ str(c)+'°C')
    #converting C - F
    f=((c*9)/5)+32 
    print('Temprature in Fahrenhit is ' +str(f )+'°F')

#calling a function.       
converter()
