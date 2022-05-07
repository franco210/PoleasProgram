def armado_listas():
    '''Destinado a cargar desde archivo una lista de datos'''
    nombre_archRE = input("Ingrese el nombre del archivo de lectura (sin extension):" )
    archivoRE = open(nombre_archRE+".txt","r")                      
    lista=[]
    archivoRE.readline() #TITULO
    dato = float(archivoRE.readline())
    while dato != 0: #USO MARCA DE FIN
        lista.append(dato)
        dato = float(archivoRE.readline())
    
    archivoRE.close()
    return lista
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def matrizcero(n,m):
    '''Función destinada a crear la matriz con sus respectivas filas y columnas'''
    matriz = []
    for i in range(n):
        matriz.append([0]*m)
    return matriz
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def cargadatos(matriz,n,m,listDE,listDS):
    '''Función destinada a cargar los datos a la matriz anteriormente creada'''
    for c in range(n):
        k = listDE[c]
        for j in range(m):
            i = float(k/listDS[j])
            matriz[c][j]=round(i,2)
    return matriz
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def promedio(matriz,cf,cc):
    '''Función destinada a calcular el promedio de relacion de transmición por fila de una matriz'''
    sumafilas=[]
    prom=[]
    for i in range(cf): #fila
        suma=0
        for j in range(cc): #columna
            suma += matriz[i][j]
        sumafilas.append(suma)
            
    for x in range(len(sumafilas)):
        prom.append(round(sumafilas[x]/cc,2))
    return prom
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ordenporinsercion(prom,listDE): #LISTA A ORDENAR= PROM ; LISTA ASOCIADA= LISTADE  
    '''Función destinada a ordenar mediante el metodo de inserción de mayor a menor los datos de la lista PROM, con arrastre de la lista asociada LISTDE(diametros de polea motriz)'''
    for i in range(1,len(prom)):
        aux1=prom[i]
        aux2=listDE[i] #ASOCIADA
        j=i-1
        while j>=0 and aux1>prom[j]:
            prom[j+1]=prom[j]
            listDE[j+1]=listDE[j] #ASOCIADA
            j=j-1
        prom[j+1]=aux1
        listDE[j+1]=aux2
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
def maximo_matriz(matriz,cf,cc):
    '''Función destinada a buscar el valor maximo en la tabla de relación de transmición y también encontrar la posición de esta'''
    max=matriz[0][0]
    li=[]
    lj=[]
    for i in range(cf):
        for j in range(cc):
            if matriz[i][j]>max:
                max=matriz[i][j]
                li=[i]
                lj=[j]
            elif matriz[i][j]==max:
                li.append(i)
                lj.append(j)
    return max, li, lj
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def busbin(lista,valor):
    '''Función destinada a buscar un valor dentro de una lista a través de el metodo de busqueda binaria'''
    i=0
    s=len(lista)-1
    pm=(i+s)//2 #calcula posición media
    while i<=s and lista[pm]!=valor:
        if valor>lista[pm]:
            i=pm+1
        else:
            s=pm-1
        pm=(i+s)//2
    if i>s:
        pm=-1
    return pm
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def calculo(de,ds,d,ne):
    """Destinado a calcular la longitud de la correa y la velocidad tangencial"""
    pi = 3.14
    long = pi * (de+ds) / 2 + 2 * (d**2 + (de-ds)**2 /4)**0.5
    vt =  (pi * de * ne) / 60000
    return long,vt
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def sdpoleas(): 
    print(("*** Sistemas de Poleas ***").center(140))
    print(("Programa destinado a realizar cálculos de transmisión de movimiento por poleas de diferentes sistemas.").center(140))
    print("\n\nRecordar que el archivo de texto debe estar en la misma carpeta que el programa .py.\nPrimero procesar la lista con los datos de las poleas motrices y luego la lista con los datos de las poleas conducidas.")
    print("Recuerde utilizar un cero como marca de fin, al final de los datos en el archivo de texto.\n")
    #ARMADO DE LISTAS FUNDAMENTALES
    print("Lista con diametros de poleas motrices")
    listDE = armado_listas()  #LISTA CON DIAMETROS DE POLEAS MOTRICES
    listDE.sort()
    print("\nLista con diametros de poleas conducidas")
    listDS = armado_listas()  #LISTA CON DIAMETROS DE POLEAS CONDUCIDAS
    listDS.sort()
    #ARMADO DE MATRIZ
    n = len(listDE)   #FILAS
    m = len(listDS)  #COLUMNAS
    matriz = matrizcero(n,m)
    matriz = cargadatos(matriz,n,m,listDE,listDS)
    #MENU
    x=("\n 1 - Lista de poleas  \n 2 - Tabla de relacion de transmición de poleas  \n 3 - Relación promedio - Mayor relación  \n 4 - Consulta de rpm, velocidad tangencial y longitud de correa  \n 5 - SALIR ")
    print("\n")
    print(("-Menú de opciones principal-").center(140))
    print(x)
    opc = int(input("Ingrese la opción deseada:"))
    while opc != 5:
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        if opc==1:
            print(("\n***Lista de poleas***").center(110))
            print("\nListado de diametros de poleas mostrices en (mm)") #ÐE
            for i in listDE:
                print(i)
            
            print("Listado de diametros de poleas conducidas en (mm)") #DS
            for p in listDS:
                print(p)
            
            print("\n")
            print(("-Menú de opciones principal-").center(140))
            print(x)
            opc = int(input("Ingrese la opción deseada:"))
            
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        if opc==2:
            print("\n")
            print(("***Tabla de relación de transmicion de poleas***").center(110))
            print("Poleas conducidas (mm)",end="")
            for i in range(m):
                print((str(listDS[i])).rjust(10), end="")
            print("\n")
            print((("Poleas motrices (mm)").rjust(22)), end="")
            print("\n")
            for i in range(n):
                print(((str(listDE[i])).rjust(22)),end="")
                for j in range(m):
                    print((str(matriz[i][j])).rjust(10), end="")
                print("\n")
            
            print("\n")
            print(("-Menú de opciones principal-").center(140))
            print(x)
            opc = int(input("Ingrese la opción deseada:"))    
            
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        if opc==3:
            print("\n")
            #LLAMADO A FUNCIÓN QUE NOS DEVUELVE LA LISTA DE LOS PROMEDIOS i DE LAS FILAS
            listapromedio = promedio(matriz,n,m)
            #COPIA DE LA LISTA ORIGINAL PARA NO PERDER LOS DATOS LUEGO DEL ORDEN POR INSERCIÓN
            listapromedio1=listapromedio.copy() 
            print(("***Relación promedio - Mayor relación***").center(110))
            print("\n")
            print(("-SubMenú de opciones-").center(140))
            print("a -- Relación de transmisión promedio ")
            print("b -- Mayor relación e transmisión ")
            print("c -- Volver al menú principal ")
            des = input("\nIngresar la opción desesada:")
            while des!= 'c':
                if des=='a':
                    print("\n         -Promedios-")
                    print("Lista     Promedio     Diametro P MOTRIZ")     
                    for i in range(len(listapromedio)):
                        print(str([i]).rjust(5),str(listapromedio[i]).rjust(12),str(listDE[i]).rjust(21))
                    
                    print("\n   -Promedios ordenados de mayor a menor utilizando metodo de inserción:")
                    listDE1=listDE.copy() #COPIA DE LA LISTA ORIGINAL PARA NO PERDER LOS DATOS LUEGO DEL ORDEN POR INSERCIÓN
                    ordenporinsercion(listapromedio1,listDE1) #CON ARRASTRE DE LA LISTA DE POLEAS MOTRICES
                    print("Promedio     Diametro P MOTRIZ")
                    for i in range(len(listapromedio1)):
                        print(str(listapromedio1[i]).rjust(8),str(listDE1[i]).rjust(21))
                    
                    print("\nPara volver al menú principal presione c, de lo contrario, ingrese otra opción.")
                    des = input("\nIngrese la opción deseada:")
                elif des=='b':
                    #LLAMADO A LA FUNCION QUE NOS DEVUELVE EL VALOR MAXIMO
                    valormaximo = maximo_matriz(matriz,n,m)
                    print("La mayor relación de transmición es:", valormaximo[0])
                    mayoresDE=[]
                    mayoresDS=[]
                    for i in range(len(valormaximo[1])):
                        mayoresDE.append(listDE[valormaximo[1][i]])
                        mayoresDS.append(listDS[valormaximo[2][i]])
                    
                    print("El/los mayores diametros motrices son:",mayoresDE,"mm")
                    print("El/los mayores diametros conducidos son:",mayoresDS,"mm")
                    
                    
                    print("\nPara volver al menú principal presione c, de lo contrario, ingrese otra opción.")
                    des = input("\nIngrese la opción deseada:")    
                else:
                    print("\nLa opción ingresada no existe, por favor intentelo nuevamente, si desea salir del submenú presione c")
                    des = input("\nIngrese la opción desesada:")
            if des=='c':
                print("\n")
                print(("-Menú de opciones principal-").center(140))
                print(x)
                opc = int(input("Ingrese la opción deseada:"))    
                
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        if opc==4:
            print("\n")
            print(("***Consulta de rpm, velocidad tangencial y longitud de correa***").center(110))
            print("\n")
            de=float(input("Ingrese el diametro de la polea motriz:"))
            while de!=0:
                RESDE = busbin(listDE,de)
                while RESDE == -1:
                    de=float(input("ERROR. Ingresar el diametro de la polea motriz:"))
                    RESDE = busbin(listDE,de)
                ds=float(input("Ingrese el diametro de la polea conducida:"))
                RESDS = busbin(listDS,ds)
                while RESDS == -1:
                    ds=float(input("ERROR. Ingresar el diametro de la polea conducida:"))
                    RESDS = busbin(listDS,ds)
                ne=float(input("Ingresar rpm motriz:"))
                d=float(input("Ingresar distancia en mm entre los centros de las poleas:"))
                long,vt = calculo(de,ds,d,ne)
                print("\n- **Datos del sistema consultado**")
                print("Diametro polea motriz:", de,"mm")
                print("Diametro polea conducida:", ds ,"mm")
                print("Distancia entre ejes:",d ,"mm")
                print("Longitud de la correa:",round(long,2),"mm")
                print("Velocidad tangencial:",round(vt,2),"m/seg")
                #BUSQUEDA DE RELACIÓN DE TRANSMICIÓN EN LA MATRIZ
                posde = int(listDE.index(de))
                posds = int(listDS.index(ds))
                rel = matriz[posde][posds]
                ns = rel * ne
                print("RPM polea conducida:",ns,"rpm")
                if de==ds:
                    print("Relación de transmisión: CONSTANTE ; mantiene la velocidad" )
                elif de>ds:
                    print("Relación de transmisión: MULTIPLICADOR ; aumenta la velocidad" )
                else: #DE<DS
                    print("Relación de transmisión: REDUCTOR ; reduce la velocidad")
                print("\n")
                cen=input("¿Desea realizar otra consulta sobre otro sistema? (s/n):")
                if cen=='s':
                    de=int(input("\nIngrese el diametro de la polea motriz:"))
                else:
                    de=0
            else:
                print("\n")
                print(("-Menú de opciones principal-").center(140))
                print(x)
                opc = int(input("Ingrese la opción deseada:"))    
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------

    else:
        print("\n")
        print(("Gracias por utilizar 'Sistemas de Poleas'\n").center(140))
    input("\nPresione enter para cerrar el programa")
    
sdpoleas()