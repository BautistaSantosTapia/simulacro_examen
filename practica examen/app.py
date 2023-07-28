# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
#El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con algunos pokemones de prueba.

A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Psiquico, Electrico)
    * Poder de ataque (validar que sea mayor a 50 y menor a 200)
B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 
y mostrar los informe del punto C.

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 1- Tome el ultimo numero de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)

    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 9.
    
    Informe 3- Tome la suma de los ultimos dos numeros de su DNI personal, en caso de ser un numero par, tomara el numero par 
    mas chico que su ultimo digito del DNI (en caso de que su ultimo digito sea 2, resolvera el ejercicio 8). En caso contrario, si es impar, 
    tomara el numero impar posterior (en caso de que su ultimo digito sea 9, resolvera el ejercicio 1)
    En caso de que el numero sea el mismo obtenido en el informe 2, realizara el siguiente informe en la lista.
    
    
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
C) NOMBRE TIPO PODER ATAQUE
    #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
    #! 1) - Cantidad de pokemones de tipo Electrico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
    #! 2) - Nombre y Poder del pokemon de tipo electrico con el poder mas alto.
    #! 3) - Nombre y Poder del pokemon de tipo psiquico con el poder mas bajo.*
    #! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
    #! 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea. *
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea. *
    #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
    #! 9) - el promedio de poder de todos los pokemones de tipo Electrico.
   
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex 🎮", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        self.image = tk.PhotoImage(file='Logo_UTN_App.png')
        
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        # Cargar aca los pokemones
        self.lista_nombre_pokemones = []#"Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Jigglypuff", "Psyduck", "Eevee", "Gengar", "Mewtwo", "Vaporeon"
        self.lista_poder_pokemones = []#80, 150, 70, 90, 60, 100, 75, 120, 180, 95
        self.lista_tipo_pokemones = []#"eléctrico", "fuego", "planta", "agua", "normal", "agua", "normal", "fantasma", "psíquico", "agua"


    def btn_mostrar_informe_1(self):
        nombre_pokemones = ""
        lista_indices_nombres = []
        index = 0
        for nombre in self.lista_nombre_pokemones:
            print(nombre)
            print(index)
            nombre_pokemones = nombre_pokemones + f" Nombre: {nombre} Indice: {index}\n"
            lista_indices_nombres.append(index)
            index = index + 1
        alert("Simulacro 1", nombre_pokemones)

    
    def btn_mostrar_informe_2(self):
        #! 6) - tipo de los pokemones del tipo que mas pokemones posea. 
        #! 7) - tipo de los pokemones del tipo que menos pokemones posea.
        contador_agua = 0
        contador_electrico = 0
        contador_psiquico = 0

        for tipo in self.lista_tipo_pokemones:
            if tipo == "AGUA":
                contador_agua = contador_agua + 1
            elif tipo == "PSIQUICO":
                contador_psiquico = contador_psiquico + 1
            elif tipo == "ELECTRICO":
                contador_electrico = contador_electrico + 1

        if contador_agua > contador_electrico and contador_agua > contador_psiquico:
            texto_mas = f"Tiene mas pokemones el tipo agua con {contador_agua}"
        elif contador_electrico > contador_psiquico:
            texto_mas = f"Tiene mas pokemones el tipo electrico con {contador_electrico}"
        elif contador_psiquico != contador_agua and contador_psiquico != contador_electrico:
            texto_mas = f"Tiene mas pokemones el tipo psiquico con {contador_psiquico}"
        else:
            texto_mas = "Hay empate por los que tienen mas"

        if contador_agua < contador_electrico and contador_agua < contador_psiquico:
            texto_menos = f"Tiene menos pokemones el tipo agua con {contador_agua}"
        elif contador_electrico < contador_psiquico:
            texto_menos = f"Tiene menos pokemones el tipo electrico con {contador_electrico}"
        elif contador_psiquico != contador_agua and contador_psiquico != contador_electrico:
            texto_menos = f"Tiene menos pokemones el tipo psiquico con {contador_psiquico}"
        else:
            texto_menos = "Hay empate por los que tienen menos"

        alert("Simulacro 2",texto_mas + " y " + texto_menos)
    
    def btn_mostrar_informe_3(self):
        pass
    
    def btn_cargar_pokedex_on_click(self):
        #! 3) - Nombre y Poder del pokemon de tipo psiquico con el poder mas bajo.
        bandera_poder = True
        poder_minimo = 0
        nombre_minimo = 0
        for pokemon in range(10):

            nombre = prompt("Simulacro", "Ingrese el nombre")
            while (nombre == None or nombre == "") or not nombre.isalpha() or len(nombre) < 2:
                nombre = prompt("Simulacro", "Ingrese el nombre correctamente")

            tipo = prompt("Simulacro", "Ingrese el tipo (Agua / Psiquico / Electrico)")
            tipo = tipo.upper()
            while tipo == None or (tipo != "AGUA" and tipo != "PSIQUICO" and tipo != "ELECTRICO"):
                tipo = prompt("Simulacro", "Ingrese el tipo correctamente (Agua / Psiquico / Electrico)")
                tipo = tipo.upper()

            poder = prompt("Simulacro", "Ingrese el poder")
            while poder == None or not poder.isdigit() or int(poder) < 50 or int(poder) > 200:
                poder = prompt("Simulacro", "Ingrese el poder correctamente")
            poder = int(poder)



            if tipo == "PSIQUICO":
                if bandera_poder == True:
                    poder_minimo = poder
                    nombre_minimo = nombre
                    bandera_poder == False
                elif poder < poder_minimo:
                    poder_minimo = poder
                    nombre_minimo = nombre

                    print(poder)
                print(poder_minimo)

            self.lista_nombre_pokemones.append(nombre)
            self.lista_poder_pokemones.append(poder)
            self.lista_tipo_pokemones.append(tipo)


        print(self.lista_nombre_pokemones)
        print(self.lista_tipo_pokemones)
        print(self.lista_poder_pokemones)

        alert("Simulacro","carga completada")

    
if __name__ == "__main__":
    app = App()
    app.mainloop()