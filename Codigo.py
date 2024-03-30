while True:
  print("deseja fazer a conversão de tamperatura?")
  opc = str(input("digite s (sim)) ou n (não) :")) 
  if opc == "n" or opc == "N":
    print("Retornando pra tela inicial")
  elif opc == "s" or opc == "S":
    print('''selecione as opções:
  1 celsius para fahrenheit: 
  2 celsius para kelvin:
  3 kelvin para fahrenheit:
  4 kelvin para celsius:
  5 fahrenheit para celsius: 
  6 fahrenheit para kelvin: ''')
    opção= int(input("digite a opção: "))
    if opção == 1:
        c = int(input("quantos graus em celsius? : "))  
        resp = 1.8 * c + 32
        print("graus em fahrenheit: ",(resp))
       
        
    elif opção == 2:
        c =  int(input("quantos graus em celsius? : "))
        resp = c + 273
        print("graus em kelvin: ", (resp))
        
    elif opção == 3:
        k =  int(input("quantos graus em kelvin? : ")) 
        resp = 1.8 * (k - 273) + 32
        print("graus em fahrenheit: ", (resp))
        
    elif opção == 4:
         k =  int(input("quantos graus em kelvin? : "))
         resp = k - 273
         print("graus em celsius: ",(resp))
      
    elif opção == 5:
        f = int(input("quantos graus em fahrenheit? : "))
        resp = (f - 32) * 5/9 
        print("graus em celsius: ", (resp))
      
    elif opção == 6:
        f = int(input("quantos graus em fahrenheit? : "))
        resp = f - 32 / 18000 + 273.15
        print("graus em kelvin: ", (resp))
      
    else:
        print("selecionar apenas 1 a 6 !")
      