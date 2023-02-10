class Car:
    def __init__(model, name, horsepower, price):# doubleunderscore and init is used to initialise a class.
        model.name=name #data members
        model.horsepower=horsepower
        model.price=price

    def myfunc(model):
        print(f"{model.name} and the price is {model.price} and the horsepower is {model.horsepower}")
    def __str__(model):# double underscore and space after def
        return"name: "+model.name +",price: " + str(model.price) + ",horsepower: " + str(model.horsepower)

p1 =Car("bently" ,700,160000)
p1.myfunc()
print(p1)
#argument(parameters)