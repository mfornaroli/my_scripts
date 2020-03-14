class cat:
    tongue = "pink"
    def __init__(self, color, legs):        # primo argomento di un metodo. se scrivessi pippo al posto di self, sarebbe uguale.
        self.color = color                  # metodo = funzione in classe. self >> punta all'oggetto stesso...
        self.legs = legs

    def meow(self):
        print("miao lol")


felix = cat("ginger", 4)
print(felix.color)
print(felix.legs)
felix.meow()
print(felix.tongue)
print(cat.tongue)


class human:
    def basic_human_function(self):
        print("we sure like to breathe")

class student (human):                  # inheritance example ...
    def __init__(self, age, height):
        self.age = age
        self.height = height

class engineer (student):               # double inheritance ...
    def complain(self):
        print("maaaan i hate this exam session")


gianluca = engineer(21, 183)
print(gianluca.height)
gianluca.complain()
gianluca.basic_human_function()

# magic methods, basically we can re-define certain operators ... amazing
class vector2D:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
    def __add__ (self,other):
        return vector2D(self.x + other.x, self.y + other.y)

first = vector2D(5,7)
second = vector2D(3,9)
result = first + second
print(result.x)
print(result.y)


class horny_human:
    def __init__(self, gender):
        self.gender = gender
    def __add__ (self, other):
        if self.gender == "male" and other.gender == "female":
            print("abbiamo un bambino!")
        else:
            print("niente riproduzione qui fratello ...")

enrico = horny_human("male")
luisa = horny_human("female")
enrico + luisa


class Pizza:                                    # definiamo classe: pizza
  def __init__(self, toppings):
    self.toppings = toppings

  @staticmethod                                 # a questa classe e' associata una funziona, che prendera' un input ... non e' obbligatoria questa linea
  def validate_topping(topping):                # questa funzione cosa fara'?
    if topping == "pineapple":
      raise ValueError("No pineapples!")
    else:
      return True                               # dunque la funzione, associata alla classe Pizza, ci dice se il topping che gli passiamo e' valido oppure no ...

# ingredients = ["cheese", "onions", "spam"]                  # con ciclo for, proviamo funzione su tutti i topping!
# if all(Pizza.validate_topping(i) for i in ingredients):
#   pizza = Pizza(ingredients)
#
# ingredients = ["cheese", "onions", "pineapple"]
# if all(Pizza.validate_topping(i) for i in ingredients):
#   pizza = Pizza(ingredients)