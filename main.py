class Jugador_de_Futbol:

  def __init__(self,
               nombre,
               edad,
               posicion,
               equipo,
               pais,
               numero_camiseta,
               estadisticas=None,
               premios=None):
    self.nombre = nombre
    self.edad = edad
    self.posicion = posicion
    self.equipo = equipo
    self.pais = pais
    self.numero_camiseta = numero_camiseta
    self.estadisticas = {"Goles": 0, "Partidos": 0}
    self.premios = []

  def actualizar_informacion(self):
    self.nombre = input("Nuevo nombre: ")
    self.edad = input("Nueva edad: ")
    self.posicion = input("Nueva posición: ")
    self.equipo = input("Nuevo equipo: ")
    self.pais = input("Nuevo país: ")
    self.numero_camiseta = input("Nuevo número de camiseta: ")
    self.estadisticas["Goles"] = int(input("Cuantos goles hizo: "))
    self.estadisticas["Partidos"] = int(input("Cuantos partidos jugo: "))

  def calcular_promedio_goles(self):
    total_goles = self.estadisticas["Goles"]
    return total_goles / self.estadisticas["Partidos"]

  def es_goleador(self):
    if self.estadisticas["Partidos"] == 0:
      return 0
    else:
      return self.estadisticas["Goles"] / self.estadisticas["Partidos"]

  def agregar_premio(self, premio):
    self.premios.append(premio)

  def eliminar_premio(self, premio):
    if premio in self.premios:
      self.premios.remove(premio)


def menu(jugadores):
  print("Bienvenido al sistema de Jugadores de Fútbol")
  while True:
    print("1. Crear un nuevo jugador de fútbol")
    print("2. Mostrar la información de un jugador existente")
    print("3. Actualizar la información de un jugador existente")
    print("4. Calcular el promedio de goles por partido de un jugador")
    print("5. Verificar si un jugador es un goleador")
    print("6. Agregar un premio o reconocimiento a un jugador")
    print("7. Eliminar un premio o reconocimiento de un jugador")
    print("8. Salir")

    option = input("Seleccione una opción: ")

    if option == "1":
      nombre = input("Nombre del jugador: ")
      edad = input("Edad del jugador: ")
      posicion = input("Posición del jugador: ")
      equipo = input("Equipo del jugador: ")
      pais = input("País del jugador: ")
      numero_camiseta = input("Número de camiseta del jugador: ")
      goles = int(input("Cuantos goles hizo: "))
      partidos = int(input("Cuantos partidos jugo: "))
      jugador = Jugador_de_Futbol(nombre,
                                  edad,
                                  posicion,
                                  equipo,
                                  pais,
                                  numero_camiseta,
                                  estadisticas={
                                      "Goles": goles,
                                      "Partidos": partidos
                                  })
      jugadores.append(jugador)
      print("Jugador creado exitosamente.")
    elif option == "2":
      nombre = input("Ingrese el nombre del jugador: ")
      found = False
      for jugador in jugadores:
        if jugador.nombre == nombre:
          print("Nombre:", jugador.nombre)
          print("Edad:", jugador.edad)
          print("Posición:", jugador.posicion)
          print("Equipo:", jugador.equipo)
          print("País:", jugador.pais)
          print("Número de camiseta:", jugador.numero_camiseta)
          print("Premios:", jugador.premios)
          found = True
          break
      if not found:
        print("Jugador no encontrado.")
    elif option == "3":
      nombre = input("Ingrese el nombre del jugador a actualizar: ")
      for jugador in jugadores:
        if jugador.nombre == nombre:
          jugador.actualizar_informacion()
          print("Información actualizada exitosamente.")
          break
      else:
        print("Jugador no encontrado.")
    elif option == "4":
      nombre = input("Ingrese el nombre del jugador: ")
      for jugador in jugadores:
        if jugador.nombre == nombre:
          promedio_goles = jugador.calcular_promedio_goles()
          print("El promedio de goles por partido de", jugador.nombre, "es:",
                promedio_goles)
          break
      else:
        print("Jugador no encontrado.")
    elif option == "5":
      nombre = input("Ingrese el nombre del jugador: ")
      for jugador in jugadores:
        if jugador.nombre == nombre:
          if jugador.es_goleador():
            print(jugador.nombre, "es un goleador.")
          else:
            print(jugador.nombre, "no es un goleador.")
          break
      else:
        print("Jugador no encontrado.")
    elif option == "6":
      nombre = input("Ingrese el nombre del jugador: ")
      premio = input("Ingrese el premio o reconocimiento a agregar: ")
      for jugador in jugadores:
        if jugador.nombre == nombre:
          jugador.agregar_premio(premio)
          print("Premio agregado exitosamente.")
          break
      else:
        print("Jugador no encontrado.")
    elif option == "7":
      nombre = input("Ingrese el nombre del jugador: ")
      premio = input("Ingrese el premio o reconocimiento a eliminar: ")
      for jugador in jugadores:
        if jugador.nombre == nombre:
          if premio in jugador.premios:
            jugador.eliminar_premio(premio)
            print("Premio eliminado exitosamente.")
          else:
            print("Premio no encontrado.")
          break
      else:
        print("Jugador no encontrado.")
    elif option == "8":
      print("Gracias por usar el sistema de Jugadores de Fútbol")
      break
    else:
      print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
  jugadores = []
  menu(jugadores)
