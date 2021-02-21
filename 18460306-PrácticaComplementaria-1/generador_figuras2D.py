
import math
def main():
    op = ""
    figuras = []
    while op !="0" :
        
        print("1.-Crear figura \n2.-Listar una clasificacion de figuras\n3.-Listar todas las figuras\n4.-Mostrar suma de todas las areas\n5.-Mostrar suma de todos los perimetros\n6.-Limpiar lista\n0.-Salir")
        op = input("Ingresar una opcion ")
        #opción 1
        if (op == "1"):
            def menu_figuras():
                fig= ""
                print("1.-Cuadrado\n2.-Triangulo\n3.-Circulo")
                fig = input("Ingresa una opcion de figura ")
                diccionario = ""
                
                #Aquí inicia la parte del cuadrado 
                if (fig == "1"):
                    lado = int(input("Ingresa el lado del cuadrado "))
                    def crear_cuadrado(lado):
                        def area_cuadrado(lado):
                            a = lado * lado
                            return a
                        a = area_cuadrado(lado)
                        def perimetro_cuadrado(lado):
                           p= lado * 4
                           return p
                        p = perimetro_cuadrado(lado)
                        dic ={"Tipo":"Cuadrado","Area":a,"Perimetro":p}
                        return dic 
                    diccionario = crear_cuadrado(lado)
                #Aqui inicia la parte del triangulo
                if ( fig == "2"):
                    lado_a = int(input("Ingresa el primer lado "))
                    lado_b = int(input("Ingresa el segundo lado "))
                    lado_c = int(input("Ingresa el tercer lado "))
                    def crear_triangulo(lado_a,lado_b,lado_c):
                        tip= ""
                        a = 0
                        p = 0
                        if(lado_a == lado_b and lado_b == lado_c):
                            tip = "Triangulo Equilatero"
                            def area_trianguloEquilatero(lado_a):
                                altura = (math.sqrt(3) * lado_a) / 2
                                a = (altura * lado_a)/2
                                return a
                            a= area_trianguloEquilatero(lado_a)
                            def perimetro_trianguloEquilatero(lado_a):
                                p = lado_a * 3
                                return p
                            p= perimetro_trianguloEquilatero

                        if((lado_a != lado_b and lado_a == lado_c) or (lado_a != lado_c and lado_a == lado_b) or (lado_a != lado_b and lado_b == lado_c)):
                            tip = "Triangulo Isosceles"
                            def area_trianguloIsosceles(lado_a, lado_b, lado_c):
                                a=0
                                if (lado_a != lado_b and lado_a == lado_c):
                                   altura = math.sqrt(lado_a * lado_a - (lado_b * lado_b / 4))
                                   a = (lado_b * altura)/2
                                elif (lado_a != lado_c and lado_a == lado_b):
                                    altura = math.sqrt(lado_a * lado_a - (lado_c * lado_c / 4))
                                    a = (lado_c * altura)/2
                                elif(lado_a != lado_b and lado_b == lado_c):
                                    altura = math.sqrt(lado_b * lado_b - (lado_a * lado_a / 4))
                                    a = (lado_a * altura)/2
                                return a
                            a= area_trianguloIsosceles(lado_a,lado_b,lado_c)
                            def perimetro_trianguloIsosceles(lado_a,lado_b,lado_c):
                                p = lado_a + lado_b + lado_c
                                return p
                            p= perimetro_trianguloIsosceles(lado_a,lado_b,lado_c)
                        if(lado_a != lado_b and lado_a != lado_c and lado_b != lado_c):
                            tip = "Triangulo Escaleno"
                            def area_trianguloEscaleno(lado_a,lado_b,lado_c):
                                sp = (lado_a + lado_b + lado_c) /2
                                a = math.sqrt(sp * (sp - lado_a) * (sp - lado_b) * (sp - lado_c))
                                return a
                            a = area_trianguloEscaleno(lado_a,lado_b,lado_c)
                            def perimetro_trianguloEscaleno(lado_a,lado_b,lado_c):
                                p = lado_a + lado_b + lado_c
                                return p
                            p = perimetro_trianguloEscaleno(lado_a,lado_b,lado_c)
                        dic ={"Tipo":tip,"Area":a,"Perimetro":p}
                        return dic
                    diccionario = crear_triangulo(lado_a,lado_b,lado_c)
                #Aqui inicia el circulo 
                if(fig == "3"):
                    radio = int(input("Ingresa el radio del circulo "))
                    def crear_circulo(radio):
                        def area_circulo(radio):
                            a = math.pi * radio * radio
                            return a
                        a = area_circulo(radio)
                        def perimetro_circulo(radio):
                            p = 2 * math.pi * radio
                            return p
                        p = perimetro_circulo(radio)
                        dic = {"Tipo":"Circulo","Area":a,"Perimetro":p}
                        return dic
                    diccionario= crear_circulo(radio)
                return diccionario
            agregar = menu_figuras()
            figuras.append(agregar)
        #Opción 2
        if (op == "2"):
            clasificar = input("Ingresa la categoria a buscar ")
            def listar_clasificacion(clasificar):
                count= 0
                if(clasificar == "Cuadrado" or clasificar == "cuadrado"):
                    for i in figuras:
                        if i.get('Tipo') == "Cuadrado":
                            count = count + 1
                            print(i)
                    if (count ==0):
                        print("La clasificación del Cuadrado está vacía")
                elif(clasificar == "Circulo" or clasificar == "circulo"):
                    for i in figuras:
                        if i.get('Tipo') == "Circulo":
                            count = count + 1
                            print(i)
                    if (count == 0):
                        print("La clasificación del Circulo está vacía")
                elif(clasificar == "Triangulo" or clasificar == "triangulo"):
                    trian = input("Que tipo de triangulo desea buscar? Equilatero, Isosceles o Escaleno: ")
                    if(trian == "Equilatero" or trian == "equilatero"):
                        for i in figuras:
                            if i.get('Tipo') == "Triangulo Equilatero":
                                count = count + 1
                                print(i)
                        if (count == 0):
                            print("La clasificación de Triangulo Equilatero está vacía")
                    elif(trian == "Isosceles" or trian =="isosceles"):
                        for i in figuras:
                            if i.get('Tipo') == "Triangulo Isosceles":
                                count = count + 1
                                print(i)
                        if (count == 0):
                            print("La clasificación de Triangulo Isosceles está vacía")
                    elif(trian == "Escaleno" or trian == "escaleno"):
                        for i in figuras:
                            if i.get('Tipo') == "Triangulo Escaleno":
                                count = count + 1
                                print(i)
                        if (count == 0):
                            print("La clasificación de Triangulo Escaleno está vacía")
                    else:
                        print("Ese tipo de triangulo no existe")
                else:
                    print("No existe esa categoria")
            listar_clasificacion(clasificar)
        #opción 3
        if (op == "3"):
            for i in figuras:
                print(i)
        if (op == "4"):
            def sumador_areas():
                conCuadrado=0
                conCirculo=0
                conTrianEqui=0
                conTrianIsos=0
                conTrianEsca=0
                for i in figuras:
                    if i.get('Tipo') == "Cuadrado":
                        conCuadrado = conCuadrado + int(i.get('Area'))
                    if i.get('Tipo') == "Circulo":
                        conCirculo = conCirculo + int(i.get('Area'))
                    if i.get('Tipo') == "Triangulo Equilatero":
                        conTrianEqui = conTrianEqui + int(i.get('Area'))
                    if i.get('Tipo') == "Triangulo Isosceles":
                        conTrianIsos = conTrianIsos + int(i.get('Area'))
                    if i.get('Tipo') == "Triangulo Escaleno":
                        conTrianEsca = conTrianEsca + int(i.get('Area'))
                print(f"La suma del area de los Cuadrados es: {conCuadrado}")
                print(f"La suma del area de los Triangulos Equilateros es: {conTrianEqui}")
                print(f"La suma del area de los Triangulos Isosceles es: {conTrianIsos}")
                print(f"La suma del area de los Triangulos Escalenos es: {conTrianEsca}")
                print(f"La suma del area de los circulos es: {conCirculo}")
            sumador_areas()
        if (op == "5"):
            def sumador_perimetros():
                perCuadrado = 0
                perCirculo = 0
                perTrianEqui = 0
                perTrianIsos = 0
                perTrianEsca = 0
                for i in figuras:
                    if i.get('Tipo') == "Cuadrado":
                        perCuadrado = perCuadrado + int(i.get('Perimetro'))
                    if i.get('Tipo') == "Circulo":
                        perCirculo = perCirculo + int(i.get('Perimetro'))
                    if i.get('Tipo') == "Triangulo Equilatero":
                        perTrianEqui = perTrianEqui + int(i.get('Perimetro'))
                    if i.get('Tipo') == "Triangulo Isosceles":
                        perTrianIsos = perTrianIsos + int(i.get('Perimetro'))
                    if i.get('Tipo') == "Triangulo Escaleno":
                        perTrianEsca = perTrianEsca + int(i.get('Perimetro'))
                print(f"La suma del perimetro de los Cuadrados es: {perCuadrado}")
                print(f"La suma del perimetro de los Triangulos Equilateros es: {perTrianEqui}")
                print(f"La suma del perimetro de los Triangulos Isosceles es: {perTrianIsos}")
                print(f"La suma del perimetro de los Triangulos Escalenos es: {perTrianEsca}")
                print(f"La suma del perimetro de los circulos es: {perCirculo}")
            sumador_perimetros()
        if (op == "6"):
            figuras.clear()
            print("La lista a quedado vacía")
        if (op == "0"):
            break
main()