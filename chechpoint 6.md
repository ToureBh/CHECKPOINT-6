# MEMORIA CHECKPOINT 6

## 1. ¿Es MongoDB una base de datos SQL o NoSQL?

Las bases de datos relacionales o SQL se componen de tablas. Cada tabla es una combinación de filas (o registros) y columnas (o campos), que se encargan de guardar la información. MongoDB es un sistema para la gestión de base de datos no SQL o no relacional, con lo cual no tiene tablas ni filas, ni SQL, este usa colecciones. 
Estas son un conjunto de documentos con una estructura JSON en la que las *claves* equivaldrían a las columnas de las bases de datos SQL.

![Comapartiva](https://cdn-images-1.medium.com/max/1200/1*UP3aK7hbAqYU6j8szceWpg.png)

Las ventajas de MongoDB es que agiliza considerablemente la escalabilidad de las aplicaciones ya que no hay que preocuparse por modificar esquemas o agregar nuevas tablas cuando evoluciona la aplicacion. Además el modelo de datos resulta muy intuitivo gracias a lo facil que resulta leer json. Estas caracterizticas mejoran la experiencia de desarrollo, aceleran el tiempo de comercialización y reducen costes. Además nos permite usar el lenguaje de programación de nuestra eleccion pues cuenta con una gran variedad de drivers oficiales para ello como Java, Ruby, Python, etc.

![distintos workflows](https://www.nisum.com/hubfs/Sql%20vs%20NoSQL.svg#keepProtocol)

MongoDB puede ser usado para cualquier tipo de proyecto de desarrollo de la actualidad como el comercio electronico, juegos aplicaciones móviles, etc. Sin embargo no es recomendado en casos de sistemas de transacciones, ya que no tiene soporte transaccional de manera nativa.


## 2. ¿Qué es una API?
Una API es basicamente la forma en la que se comuican las diferentes aplicaciones en internet así como la comunicación entre unusuario y una aplicación. 

Normalmente un usuario o aplicacion envía una petición a un servidor y este la procesa y envía un código de respuesta o de información. Si la petición es exitosa, la respuesta llevará un código de la familia de los 200, por el contrario si hubiera cualquier error se genera un código que estará en la zona de los 400 o 500. 

![Mensaje de error 400](https://www.pctechguide.com/wp-content/uploads/2015/07/400-Bad-Request.png)

Tras obtener la respuesta, el usuario o la otra aplicación decide si ya tiene toda la información requerida o necesita enviar más peticiones a nuestro servidor.


## 3. ¿Cuáles son los tres verbos de API?
Existen 4 grandes métodos para trabajar con API:
1. GET: Se usa básicamente para obtener información de una base de datos.

2. POST: Con este método creamos información, y guardamos esta información en nuestra base de datos. 

3. PUT: Nos sirve para actualizar la información de la base de datos. 

4. DELETE: Este método lo usamos para borrar información.


## 4. ¿Qué es Postman?
Postman se trta de una herramienta que nos ayuda a hacer pruebas con nuestras API. Nos ofrece los métodos HTTP donde GET, PUT, POST Y DELETE son los más comunes aunque existen más. La barra de direcciones es donde pondremos la URL de la app que queramos testar. También podemos pasar parámetros, modificar los headers, así como probar autentificaciones desde aquí.
![ejemplo](https://voyager.postman.com/illustration/rest-client/rest-client-send-and-save-postman.png)

## 5. ¿Para qué usamos Clases en Python?
Las clases son un concepto en python. De igual manera que existen las variables, las estructuras de datos, los condicionales, o las iteraciones sobre estructuras de datos, tenemos la **programción orientada a objetos**. 

En nuestros programas podemos usar diferentes tipos de datos y pasarlos a funciones para realizar diversas acciones con ellos, esto es bastante sencillo, pero también podemos trabajar con datos más complejos. 

Por ejemplo, si quisieramos trabajar con una persona en su totalidad, es decir, si cogemos aspectos que puedan definir a una persona (de forma muy simplificada) como el nombre, la edad y el color de los ojos, y además sumamos acciones que pueda realizar esa persona como hablar o caminar, nos queda claro que necesitamos algo diferente a una función, ya que con esta podríamos trabajar sobre parámetros individuales, como si fueran cadenas de texto, pero no sobre la persona y las acciones que realiza de forma global. 

Aquí aparece la **programación orientada a objetos**, una herramienta que nos permite definir estos conceptos complejos y trabajar con ellos gracias a las Clases o *class*. Estas son la pieza clave en la programación orientada a objetos y nos definen cuales son las caracteristicas del objeto o concepto que queramos representar. Se trata de un conjunto de variables y funciones que agrupadas dentro de este “paquete” llamado Clase definien al objeto, en nuestroejemplo a la persona. 

Por ejemplo, el nombre, edad y color de ojos serían strings y cuando queramos realizar acciones como correr, o hablar serían los métodos de nuestra clase Persona. Utilizando esta clase Persona ahora podríamos crear tantos objetos como queramos en nuestro programa, así como hacerlos interactuar entre ellos, pasarlos como argumentos a funciones, etc. en definitiva usar una Persona como si fuera un nuevo tipo de dato.

Debe quedar claro que la clase es un concepto, son las diferentes caracteristicas que usamos para definir a la persona como el nombre, la altura y los métodos, sin embargo, si creamos a una persona específica, esta sería un **objeto**. Por esto el nombre de programación orientada a objetos, que se trta de un paradigma de programación en la que no solo utilizamos metodos y variables sino que además podemos crear objetos que interactuan entre ellos. 

Es decir, mi clase persona sería:
```python
class Persona: 
    def __init__(self, nombre, edad, ojos):
        self.nombre = nombre
        self.edad = edad
        self.ojos = ojos
```
Sin embargo, si ahora quisiéramos crear un objeto de esa clase, es decir, en nuestro ejemplo a una persona específica, haremos lo siguiente:
```python
class Persona: 
    def __init__(self, nombre, edad, ojos):
        self.nombre = nombre
        self.edad = edad
        self.ojos = ojos

isabel = Persona("Isabel", "20", "verdes")
```

## 6. ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?

Para crear una clase en Python, primero pondremos class segudido del nombre de nuestra clase con la primera letra en mayusculas, y dos puntos detrás
```python
class Persona:
```
Tras esto, todo lo que viene bajo los dos puntos identado hacia la derecha será lo que defina nuestra clase Persona. 
Lo primero que haremos será definir el método que se encarga de crear una instancia de nuestra clase. El llamado metodo constructor de la clase, porque se usa para construir una instancia. Todos los lenguajes de proramación tienen el suyo propio, y en Python siempre tiene el mismo nombre, es un método especial llamado método __init__. Este tipo de metodos con doble barra baja antes y después del nombre se llaman métodos double underscore o *dunder*. Estos son métodos especiales.

```python
class Persona: 
    def __init__
```

Todos los metodos que defiimos dentro de una clase (inclusido __init__) tienen que tener un primier argumento llamada **self**. Este argumento self hace referencia al objeto especifico que estamos creando. Es decir, nuestra clase es Persona y cuando creamos una instancia de Persona (es decir una persona en específico) esta viene dada por el argumento self para que podamos trabajar con ella. 

```python
class Persona: 
    def __init__(self, nombre, edad, ojos):
```

Además le podemos dar todos los argumentos que queramos para especificar las instancia que vamos a crear de nuestra clase Persona. En nuestro caso, nombre, edad y color de ojos.
Ahora nuestro metodo __init__ va a darle nombre, edad y color de ojos que recibimos como paramero en el constructor al objeto self que representa la instancia específica que vamos a crear.

```python
class Persona: 
    def __init__(self, nombre, edad, ojos):
        self.nombre = nombre
        self.edad = edad
        self.ojos = ojos
```

## 7. ¿Qué es un método dunder?
Los metodos dunder nos permiten ampliar las capacidades de las clases que creamos en python. Son aquellos que comienzan y terminan con dos guiones bajos. 

Estan predefinidos por defercto en cualquier clase, no los definimos nosotros, pero podemos sobreescribirlos. El más conocido y que más usamos es el método __init__, comocido como inicializador o construcor, que define qué es lo que pasa cuando construicomos o creamos un nuevo objeto de una clase.

El método __str__ es el que nos permite definir que es lo que pasa cuando imprimimos un objeto o cuando hacemos el llamado al método str().

```python
class Persona:
  def __init__(self, nombre, edad, ojos):
    self.nombre = nombre
    self.edad = edad
    self.ojos = ojos

  def __str__(self):
    return f"Esta persona se llama {self.nombre} y tiene {self.edad} años"


isabel = Persona('Isabel', "20", "verdes")
print(isabel)
```

Por otro lado, el método __repr__, que es la abreviación de representacion, es similar a __str__ con una diferencia notable, ya que __str__ es una representación informal de nuestro objeto, es lo que nosotros, comos seres humanos quisiéramos ver, la informacion que es conveniente ver cuando imprimimos un objeto. 

En cambio __repr__ es la representación formal del objeto y por lo general se usa cuando queremos pasar la informacion de nuestro objeto a otro método que pueda analizar todos los datos del mismo. Para ello necesitamos que tenga una estructura particular. Así que en este caso haremos lo siguiente:

```python
class Persona:
  def __init__(self, nombre, edad, ojos):
    self.nombre = nombre
    self.edad = edad
    self.ojos = ojos

  def __repr__(self):
    return f"Persona <value: nombre: {self.nombre}, edad: {self.edad}, ojos: {self.ojos}>"


isabel = Persona('Isabel', "20", "verdes")
print(isabel)

```

## 8. ¿Qué es el polimorfismo?
En Python podemos tener clases que hereden de otras clases. 

Por ejemplo, imaginemos que queremos usar nuestra clase Persona para crear a Isabel, pero también queremos crear otra clase de persona que sea Bailarina, ambas tendrán una altura, nombre, caminan, hablan, etc. es decir, ambas tendrán la misma funcionalidad puesto que son personas, sin embargo a mi clase Bailarina podemos añadirle piruetas, o split, lo cual nuestra clase Persona no puede realizar. 

Para ello creamos una clase que define a una persona y ortra clase que define a una persona que sabe bailar, pero si quisieramos hacerlo independientemente tendriamos que repetir muchas cosas, como la altura el nombre y los métodos compartidos. Aquí entra en juego la herencia: tenemos una clase que nos define nuestro concepto de persona y luego crearemos una clase que hereda de la primera que lo especializa. 

Cuando una clase hereda de otra esta recibe todas sus variables y todos sus metodos, es decir, la segunda es exactamente igual que la clase original pero ahora en esta nueva clase podemos modificar algunas partes o añadirle otras, como hacer piruetas o el split en nuestro ejemplo de Bailarina. 

```python
class Persona: 
    def __init__(self, nombre, edad, ojos):
        self.nombre = nombre
        self.edad = edad
        self.ojos = ojos

class Bailarina(Persona):
  def split(self):
    return True
```


El polimorfismo nos dice que en nuestro código, en cualquier parte que tengamos que pasar un objeto de una clase determinada podemos intercambiarlo por otro, siempre y cuando este nuevo objeto sea de una clase que hereda de la inicial.

Esto se debe que si tenemos una función que recibe como parámetro un objeto de clase Persona y le pasamos un objeto de clase Bailarina, es verdad que este último es diferente, pero lo es porque extiende el inicial, tiene más metodos que Persona, pero dentro de nuestra función podemos seguir interactuando con el objeto de clase Bailarina como si fuera Persona, porque todo lo que tiene esta clase Bailarina lo tiene la clase Persona de la que hereda. 

## 9. ¿Qué es un decorador de python?
Normalmente se considera una mala praxis seleccionar elementos de manera indiscriminada de nuestro programa. Ya que generalmente programamos para otros todo debe ser claro y fácilmente comprensible. También puede que haya elementos que no deban ser modificados por los usuarios del programa. 

Para facilitar la comprensión y dejar claro qué elementos son modificables y cuáles no, se emplean los decoraodres de propiedad. Cuando queremos establecer que hay un valor que no queremos que sea sobreescrito o modificado lo ponemros en el metodo __init__ con una barra baja como en el parámetro edad del ejemplo siguiente:

```python
class Persona: 
    def __init__(self, nombre, edad, ojos):
        self.nombre = nombre
        self._edad = edad
        self.ojos = ojos
```
El código no se ve afectado por esta modificación y va a seguir funcionando igual. Esto es sólo una pista para nosotros mismos y para los futuros desarrolladores que puedan trabajar con nuestro código de que ese valor deberia estar protegido.





