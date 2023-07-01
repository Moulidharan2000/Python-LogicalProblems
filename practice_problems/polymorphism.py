class India:
    def capital(self):
        print("\nNew Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


# polymorphism using class methods
ind_obj = India()
usa_obj = USA()
for country in (ind_obj, usa_obj):
    country.capital()
    country.language()
    country.type()


# polymorphism using function and objects
def func(obj):
    obj.capital()
    obj.language()
    obj.type()


obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)


class Birds:

    def intro(self):
        print("\nThere are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot")


class Sparrow(Birds):

    def flight(self):
        print("Sparrow can fly")


class Ostrich(Birds):

    def flight(self):
        print("Ostrich cannot fly")


birds_obj = Birds()
sparrow_obj = Sparrow()
ostrich_obj = Ostrich()

birds_obj.intro()
birds_obj.flight()

sparrow_obj.flight()

ostrich_obj.flight()

