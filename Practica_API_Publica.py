import json
from pathlib import Path
#habra que instalarla primero
import requests
import os
#direccion API publica que vamos a utilizar
# https://api.covid19api.com/


try:
    def menu():
        os.system('cls')
        print("Selecciona una opcion:")
        print("\t1 - Resumen")
        print("\t2 - Ficha del pais")
        print("\t3 - Obtener el primer dia (Obtener el premer dia de todo el estado)")
        print("\t4 - Listado de todos los casos de un pais  en vivo : ")
        print("\t5 - Salir")
        opcion=int(input("Selecciona una opcion : "))
        return (opcion)
    def Resumen():
        api_address="https://api.covid19api.com/summary"

        resp = requests.get(api_address)
        if resp.status_code==200:#todo correcto
            json_data=json.loads(resp.content)
            print(type(json_data))#fijate que lo que tengo en json_data ahora es un diccionario
            # lo veremos si lo visualizamos
            print(json_data)
            #print("Resumen Cov19 : %s"%json_data['num_items'])
        
        print("Resumen Cov19 : %s"%json_data.get('Global'))
    
    def Pais():
        #Pais=input("Introdroduce el nombre del Pais : ")
        api_address="https://api.covid19api.com/countries"
        
        resp = requests.get(api_address)
        if resp.status_code==200:#todo correcto
            json_data=json.loads(resp.content)
            print("Pais : ",json_data[1]['Country'])
            print("Slug : ",json_data[1]['Slug'])
            print("ISO2 : ",json_data[1]['ISO2'])

    def primer_dia():
        api_address="https://api.covid19api.com/dayone/country/south-africa/status/confirmed"
        Slug=input("Introdece el nombre de la pais : ")#nombre el pais
        resp = requests.get(api_address)
        if resp.status_code==200:#todo correcto
            json_data=json.loads(resp.content)
           # print("Numero de casos : ",len(json_data))
            #al estar ordenador cronologicamente visualizo solo el primero
           # print("Numero de casos recuperados : ",json_data[1]['Province'])
            print("Numero de muertos : ",json_data[1]['Date'])
            print("Numero de casos confirmados : ",json_data[1]['Cases'])

            
    
    def Obtener_por_fechas():
        Country=input("Introduce un pais : ")
        api_address="https://api.covid19api.com/live/country/south-africa"
        resp = requests.get(api_address)
        if resp.status_code==200:#todo correcto
            json_data=json.loads(resp.content)
            print("Numero de cosos confirmados : ",json_data[1]['Confirmed'])
            print("Numero de casos recuperados : ",json_data[1]['Recovered'])
            print("Numero de muertos : ",json_data[1]['Deaths'])
            print("Numero de casos activos : ",json_data[1]['Active'])
            
            #print(json_data)


    while True:
        opcion=menu()
        if opcion==1:
            Resumen()
        elif opcion==2:
            Pais()
        elif opcion==3:
            primer_dia()
        elif opcion==4:
            Obtener_por_fechas()
        elif opcion==5:
            break
 
        input("Pulse una tecla para terminar...")

except:
    print("Ha ocurrido algun error")