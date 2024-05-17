class Usuario:
  def __init__(self, nombre_usuario, contraseña):
      self.nombre_usuario = nombre_usuario
      self.contraseña = contraseña

  def __str__(self):
    return f"{self.nombre_usuario}, {self.contraseña}"

margarita = Usuario("Margarita1999", "1234567ABC")

print(margarita)
