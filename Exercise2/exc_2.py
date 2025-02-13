

class Country:
    def __init__(self, name, pop, language=None, area=None):
        if language is None:
            language = []
        self.__name = name
        self.__population = pop
        # 1c
        self.__area = area
        self.__language = language

    # 1b
    def print_info(self):
        # 1d
        if self.__area is not None:
            print_area = f", the area of the country is {self.__area} km2"
        else:
            print_area = ""

        print(f"In {self.__name} there are {self.__population} "
              f"million inhabitants{print_area}.")

    # 1e
    def add_language(self):
        pass


se = Country("Sweden", 10.5, ["Swedish"], "450,295")
no = Country("Norway", 5.5)
# 1a
ic = Country("Iceland", 0.4) # Not allowed to use "is" (official short)
dk = Country("Denmark", 6.0)


country_list = [ic, dk, se, no]

for country in country_list:
    country.print_info()

# se.print_info()
