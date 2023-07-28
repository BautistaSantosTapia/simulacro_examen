import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:


*A)  Al presionar el botón 'Agregar' se debera cargar el peso* de un articulo, el cual podra ser ingresado en gramos o en onzas 

    La unidad de medida es indicada mediante una lista desplegable.

 Flotantes mayores que cero

Si existe error al validar indicarlo mediante un Alert
Si se cargo correctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

*B) Al precionar el boton mostrar se deberan listar los pesos en gramos, en onzas y su posicion en la lista (por terminal)

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) Al precionar el boton Informar 
    0- Valor (en onzas) y posicion del articulo mas pesado
    1- Valor (en gramos) y posicion del articulo mas liviano
    2- Peso promedio (en onzas) 
    3- Peso promedio (en gramos)
    4- Informar los pesos que superan el promedio (en gramos)
    5- Informar los pesos que NO superan el promedio (en onzas)
    -6- Informar la cantidad de articulos que superan el peso promedio
    -7- Informar la cantidad de articulos que NO superan el peso promedio
    *8- Indicar los pesos repetidos (gramos)
    *9- Indicar los pesos NO repetidos (gramos)


1 gramo son 0.035274 oz
1 oz son 28.3495 gramos
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("RECUPERATORIO EXAMEN INGRESO")

        self.txt_peso_articulo = customtkinter.CTkEntry(master=self, placeholder_text="PESO")
        self.txt_peso_articulo.grid(row=1, padx=20, pady=20)

        self.combobox_tipo_de_peso = customtkinter.CTkComboBox(master=self, values=["Gramos","Onzas"])
        self.combobox_tipo_de_peso.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_pesos = []


    def btn_agregar_on_click(self):
        peso = self.txt_peso_articulo.get()
        tipo = self.combobox_tipo_de_peso.get()
        print(peso)
        print(tipo)
        #bandera_de_puntos = True
        peso_es_valido = False
        cantador_de_puntos = 0

        if peso:
            for letra in peso:
                self.txt_peso_articulo.delete(0,tkinter.END)
                if not letra.isdecimal() and letra != ".":
                    peso_es_valido = False
                    break
                elif letra == ".":
                    cantador_de_puntos = cantador_de_puntos + 1
                    if cantador_de_puntos > 1:
                        peso_es_valido = False
                        break
                else:
                    peso_es_valido = True
                """
                if letra.isdecimal():
                    peso_es_valido = True
                elif bandera_de_puntos and letra == ".":
                    bandera_de_puntos = False
                    peso_es_valido = True
                else:
                    peso_es_valido = False
                    break
                """
                        
            if peso_es_valido == True:

                peso = float(peso)

                if tipo == "Onzas":
                    peso = peso * 28.3495

                if peso <= 0:
                    peso_es_valido = False

                self.lista_pesos.append(peso)

        print(self.lista_pesos)

        if peso_es_valido == True:
            texto = "El peso es valido"
        else:
            texto = "El peso no es valido"

        alert("Practica", texto)
          


    def btn_mostrar_on_click(self):
        self.lista_pesos = [1.2, 3.4, 123.2, 54.3] #/////////////////////// self.lista_pesos.get()
        # gramos
        pesos_en_gramos = "" # aca ya esta en gramos en la lista de pesos

        for peso in self.lista_pesos:
            pesos_en_gramos = pesos_en_gramos + str(peso) + " gramos\n"
        alert("Practica",pesos_en_gramos)

        # onzas
        pesos_en_onzas = [] # aca hay que pasar los pesos de la lista de gramos a onzas y guardarlos en una nueva lista solo de onzas

        for peso in self.lista_pesos:
            peso_onzas = peso / 28.3495
            pesos_en_onzas.append(peso_onzas)

        pesos_en_onzas_str = ""

        for peso in pesos_en_onzas:
            pesos_en_onzas_str = pesos_en_onzas_str + str(peso) + " onzas\n"

        alert("Practica",pesos_en_onzas_str)

        # indices
        lista_indices = []
        indice = 0
        for peso in self.lista_pesos:
            print(f"Peso {peso}, Indice {indice}")
            lista_indices.append(indice)
            indice = indice + 1
        """
        for indice in range(len(self.lista_pesos)):
            print(f"Indice {indice} - Valor {self.lista_pesos[indice]}")

        for indice, peso in enumerate(self.lista_pesos):
            print(f"Indice {indice} - Valor {peso}")
        """
        
        indices_str = ""
        for indice in lista_indices:
            indices_str = indices_str + str(indice) + " indices\n"
        alert("Practica", indices_str)

    def btn_informar_on_click(self):
        #-6- Informar la cantidad de articulos que superan el peso promedio
        #-7- Informar la cantidad de articulos que NO superan el peso promedio
        #*8- Indicar los pesos repetidos (gramos)
        #*9- Indicar los pesos NO repetidos (gramos)

        self.lista_pesos = [1.2, 1.2, 3.4, 54.3, 123.2, 54.3, 1.2]  #/////////////////////// self.lista_pesos.get()
        #8
        pesos_repetidos = []

        for peso in self.lista_pesos:
            print(peso)
            print(self.lista_pesos.count(peso))
            if self.lista_pesos.count(peso) > 1 and pesos_repetidos.count(peso) == 0:
                pesos_repetidos.append(peso)
            """
            if peso not in pesos_repetidos and self.lista_pesos.count(peso) > 1:
                pesos_repetidos.append(peso)


            if self.lista_pesos.count(peso) > 1: # se fija si se repite
                if pesos_repetidos.count(peso) == 0: #se fija si ya esta en la lista
                    pesos_repetidos.append(peso)
            """
        
        alert("Practica", f"Los numeros repetidos son: {pesos_repetidos}")
        #9
        pesos_no_repetidos = []

        for peso in self.lista_pesos:
            print(peso)
            print(self.lista_pesos.count(peso))
            if self.lista_pesos.count(peso) == 1 :#and pesos_no_repetidos.count(peso) == 0
                pesos_no_repetidos.append(peso)
        alert("Practica", f"Los numeros no repetidos son: {pesos_no_repetidos}")

        #6
        suma_peso = 0
        mayores_promedio = []
        for peso in self.lista_pesos:
            suma_peso = suma_peso + peso
        
        if len(self.lista_pesos) > 0:
            promedio_peso = suma_peso / len(self.lista_pesos)
        else:
            alert("Practica", "La lista eta vacia")
        
        for peso in self.lista_pesos:
            if promedio_peso < peso:
                mayores_promedio.append(peso)
        alert("Practica", f"Los numero mayores al promedio son: {mayores_promedio}")
        #7
       
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()