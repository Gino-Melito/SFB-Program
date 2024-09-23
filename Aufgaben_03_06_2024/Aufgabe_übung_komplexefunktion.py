def parameter_funktion(param1=None,param2=None,param3=None):
    
    if param1==None:
        param1 = "Standardwert für param1"
    if param2==None:
        param2 = 100
    if param3==None:
        param3 = [1,2,3]
    print(param1,param2,param3)



parameter_funktion()
parameter_funktion(param1="meine Variabeln",param2=50 )
parameter_funktion(param3=[300,50,100])
parameter_funktion("text",199,[50,20,1])
parameter_funktion()



