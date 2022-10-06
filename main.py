class Vehiculo:
  
  color=None
  ruedas=None
  puertas=None
  
  def __init__(self, color, ruedas, puertas):
    self.color = input("selecciona un color ")
    self.ruedas = input("Cantidad de ruedas? ")
    self.puertas = input("Cantidad de puertas?")

class Coche (Vehiculo):
  
  velocidad=None
  Cilindrada=None
  
  def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
    super().__init__(color, ruedas, puertas)
    self.velocidad=input("velociad máxima? ")
    self.cilindrada=input("cilindrada? ")


#nuevoVehículo= Vehiculo("rojos","cuatro","tres")
nuevoCoche=Coche("rojo","cuatro","tres","5000","4")

print("El nuevo coche es color", 
      nuevoCoche.color,"tiene",
      nuevoCoche.ruedas, "ruedas y", 
      nuevoCoche.puertas,"puertas además su velocidad máxima es de",
      nuevoCoche.velocidad,"y su cilindrada",nuevoCoche.cilindrada)