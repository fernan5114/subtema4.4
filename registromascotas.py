import os
nombre_mascotas=[""]*3 # pupi
edad_mascotas=[0]*3      # 3

def insentar():
    for i in range(len(nombre_mascotas)):   #   .Length en C#
           nombre_mascotas[i]= input(f"ingrese nombre de la mascota: ")
           edad_mascotas[i]=int(input(f"ingrese edad mascotas: "))
def mostrar():
    for i in range(len(nombre_mascotas)):   #   .Length en C#
        print(f"nombre: {nombre_mascotas[i]}, edad: {edad_mascotas[i]}")

def eliminar(nombreAborrar):
    for i in range(len(nombre_mascotas)):
         if nombre_mascotas[i] == nombreAborrar: #encotre a la mascota que quiero borrar
            for j in range(i,len(nombre_mascotas)-1): #penultimo registro
                    # #deplanzamiento los le elementos hacia la izquieda
                nombre_mascotas[j] = nombre_mascotas[j+1]
                edad_mascotas[j] = edad_mascotas[j+1]

            #dejar en blanco la ultima ubicacion
            nombre_mascotas[-1] = ""
            edad_mascotas[-1] = 0
            print(f"mascota eliminada {nombre_mascotas[i]}")
            return #detener la busqueda de mascotas con el mismo nombre OPCIONAL

def main():
    global nombre_mascotas, edad_mascotas #para modificar las listas declaras fuera del arreglo
    #arreglar paralelos ambas listas debe tener la misma longitud = 3
    nombre_mascotas=[""]*3  #iniciar la lista vacia para cadenas de longitud 3
    edad_mascotas=[]*3    #iniciar la lista vacia para numeros enteros de longitud 3

    opcion = 0
    while opcion != 4:   ## ocpion distinto a 4(trure)
        os.system ('cls' if os.name=='nt' else 'clear') #limpiar la consola 
        print("[1] Insertar mascota (nombre | edad)")
        print("[2] Mostrar mascotas (nombre | edad)")
        print("[3] Eliminar mascotas por nombre (en ambos vectores)")
        print("[4] Ordenar macotas alfabeticamente")
        print("[5] Salir")
        opcion = int(input("elija una opcion: "))
        if opcion==1:
           insentar()
        elif opcion==2:
            mostrar()
        elif opcion==3:
            macotasaborrar = input("ingrese mascotas a borra : ")
            eliminar(macotasaborrar)
        elif opcion==4:
                    # ordenarMacotitas()
        elif opcion==5:
            print("saliendo..")
        else: print("opcion invalida")
        if opcion !=5: input("presiona para continuar..") #espere a la interacion del usuario para recargar el menu
main()