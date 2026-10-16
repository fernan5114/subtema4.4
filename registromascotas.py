import os
nombre_mascotas=[""]*3 # pupi
edad_mascotas=[0]*3    #  3
def insertar():
    for i in range(len(nombre_mascotas)): # .Length en C#
        nombre_mascotas[i]= input(f"ingrese nombre mascota: ")
        edad_mascotas[i]=int(input(f"ingrese edad mascota: "))
def mostrar():
    for i in range(len(nombre_mascotas)): # .Length en C#
        print(f"nombre: {nombre_mascotas[i]} , edad: {edad_mascotas[i]}")

def eliminar(nombreAborrar):
    for i in range(len(nombre_mascotas)):     
        if nombre_mascotas[i] == nombreAborrar:   #encontre a la mascota que quiero borrar
           for j in range(i,len(nombre_mascotas)-1): #penultimo registro
                #desplazando los elementos hacia la izquierda
            nombre_mascotas[j] = nombre_mascotas[j+1]
            edad_mascotas[j] = edad_mascotas[j+1]

            #dejar en blanco la ultima ubicacion
            nombre_mascotas[-1] = ""
            edad_mascotas[-1] = 0
            print(f"mascota eliminada {nombre_mascotas[i]}")
            return #detener la busqueda de mascotas con el mismo nombre OPCIONAL

def Ordenar (): #burbuja
    for i in range (len(nombre_mascotas)):
        for j in range (len(nombre_mascotas)-1): #penultimo elemento y compararlo con el ultimo
                mascota1 = nombre_mascotas[j] #mascota = zeus 
                mascota2 = nombre_mascotas[j+1] #mascota = luly

                # z(122)    >  l(108)
        if mascota1[0] > mascota2[0]: #true 
            temporal = nombre_mascotas[j] #temporal = zeus 
            nombre_mascotas[j] = nombre_mascotas[j+1]
            nombre_mascotas[j+1]=temporal

            # nombre_mascotas [j] [zeus, luly, braco] ASCI

    
                             # 122(z) ,108 (l) ,98 (b)
    print("Mascotas ordenadas!!")  

def main():
    global nombre_mascotas, edad_mascotas #para modificar las listas declaradas fuera del arreglo
    #arreglos paralelos ambas listas deben tener la misma longitud = 3
    nombre_mascotas=[""]*3  #iniciar la lista vacia para cadenas de longitud 3
    edad_mascotas=[0]*3  #iniciar la lista vacia para numeros enteros de longitud 3
    opcion=0
    while opcion != 5:   ## opcion distinto a 4  (true)
        os.system ('cls' if os.name=='nt' else 'clear')  #limpiar la consola
        print("[1] Insertar mascota (nombre | edad)")
        print("[2] Mostrar mascotas (nombre | edad)")
        print("[3] Eliminar mascotas por nombre (en ambos vectores)")
        print("[4] ordenar mascotas alfabeticamente ")
        print("[5] Salir")    
        opcion = int(input("elija una opcion: "))
        if opcion==1:
           insertar()
        elif opcion==2:
            mostrar()
        elif opcion==3:
            mascotaaborrar = input("ingrese mascota a borrar: ")
            eliminar(mascotaaborrar)
        elif opcion==4:
           Ordenar()
           mostrar()
        elif opcion==5:
            print("saliendo...")
        else: print("opcion invalida")
        if opcion !=5: input("presione para continuar..") #espere a la interaccion del usuario para recargar el menu
main()
