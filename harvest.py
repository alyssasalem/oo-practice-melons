############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)
        

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    # instance Muskmelon
    musk = MelonType(
        "musk",
        1998,
        "green",
        True,
        True,
        "muskmelon"
    )
    # add musk pairing
    musk.add_pairing("mint")
    # append musk
    all_melon_types.append(musk)
    # instantiate Casaba
    cas = MelonType(
        "cas",
        2003,
        "orange",
        True,
        False,
        "casaba"
    )
    # add musk pairing
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    # append musk
    all_melon_types.append(cas)
    # instantiate Crenshaw
    cren = MelonType(
        "cren",
        1996,
        "green",
        True,
        False,
        "crenshaw"
    )
    # add musk pairing
    cren.add_pairing("prosciutto")
    # append musk
    all_melon_types.append(cren)
    # instantiate Yellow Watermelon
    yw = MelonType(
        "yw",
        2013,
        "yellow",
        True,
        True,
        "yellow watermelon"
    )
    # add musk pairing
    yw.add_pairing("ice cream")
    # append musk
    all_melon_types.append(yw)
 

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        # gets the object from the melon name (self.name)
        print(f"{melon.name} pairs with ")
        for pairing in melon.pairings:
            print(f"- {pairing}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    # create empty melons dict
    melons_dict = {}
    for melon in melon_types:
        melons_dict[melon.code] = melon

    
    return melons_dict
    

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape, color, field, staff):
        self.melon_type = melon_type
        self.shape = shape
        self.color = color
        self.field = field
        self.staff = staff

    def is_sellable(self):
        if self.shape > 5 and self.color > 5 and self.field != 3:
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    all_melons = []

    melon_1 = Melon(melon_types["yw"], 8, 7, 2, "Sheila")
    melon_2 = Melon(melon_types["yw"], 3, 4, 2, "Sheila")
    melon_3 = Melon(melon_types["yw"], 9, 8, 3, "Sheila")
    melon_4 = Melon(melon_types["cas"], 10, 6, 35, "Sheila")
    melon_5 = Melon(melon_types["cren"], 8, 9, 35, "Michael")
    melon_6 = Melon(melon_types["cren"], 8, 2, 35, "Michael")
    melon_7 = Melon(melon_types["cren"], 2, 3, 4, "Michael")
    melon_8 = Melon(melon_types["musk"], 6, 7, 4, "Michael")
    melon_9 = Melon(melon_types["yw"], 7, 10, 3, "Sheila")

    all_melons.append(melon_1)
    all_melons.append(melon_2)
    all_melons.append(melon_3)
    all_melons.append(melon_4)
    all_melons.append(melon_5)
    all_melons.append(melon_6)
    all_melons.append(melon_7)
    all_melons.append(melon_8)
    all_melons.append(melon_9)

    return all_melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest



#### Testing area:

melon_types = make_melon_types()

print_pairing_info(melon_types)

dict_melon_types = make_melon_type_lookup(melon_types)

make_melons(dict_melon_types)