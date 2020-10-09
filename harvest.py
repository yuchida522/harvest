############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
    

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        
        # Fill in the rest
        self.pairings.append(pairing)
        
    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType("musk",1998,"green",True,True,"Muskmelon")
    muskmelon.add_pairing('mint')
    all_melon_types.append(muskmelon)

    casaba = MelonType("cas",2003,"orange",False,False,"Casaba")
    casaba.add_pairing('mint')
    casaba.add_pairing('strawberries')
    all_melon_types.append(casaba)

    crenshaw = MelonType("cren",1996,"green",False,False,"Crenshaw")
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    y_watermellon = MelonType("yw",2013,"yellow",False,True,"Yellow-Watermellon")
    y_watermellon.add_pairing('ice-cream')
    all_melon_types.append(y_watermellon)
    
    #name = MelonType(code, first_harvest, color, is_seedless, is_bestseller,name)
    # Fill in the rest
    
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name} pairs well with:")
        for pair in melon.pairings:
            print(f"- {pair}") 
            #loop through pairing but how?
            #print(f"- {pairing}")
    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    codes = {}

    for melon in melon_types:
        # for melon.code in melon:
        codes[melon.code] = melon 
    return codes
    # Fill in the rest


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field, harvest_person):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvest_person = harvest_person
    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.field!=3:
            return True

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    
    codes = make_melon_type_lookup(melon_types)
    
    melon_list = []
    # Fill in the rest
    melon1 = Melon(codes["yw"], 8, 7, 2,"Sheila") 
    melon_list.append(melon1)

    melon2 = Melon(codes["yw"], 3, 4, 2,"Sheila")
    melon_list.append(melon2)

    melon3 = Melon(codes["yw"], 9, 8, 3,"Sheila")
    melon_list.append(melon3)

    melon4 = Melon(codes["cas"], 10, 6, 35,"Sheila")
    melon_list.append(melon4)

    melon5 = Melon(codes["cren"], 8, 9, 35,"Michael")
    melon_list.append(melon5)

    melon6 = Melon(codes["cren"], 8, 2, 35,"Michael")
    melon_list.append(melon6)

    melon7 = Melon(codes["cren"], 2, 3, 4,"Michael")
    melon_list.append(melon7)

    melon8 = Melon(codes["musk"], 6, 7, 4,"Michael")
    melon_list.append(melon8)

    melon9 = Melon(codes["yw"], 7, 10, 3,"Sheila")
    melon_list.append(melon9)
    #muskmelon = Melon(melon_type, shape_rating, color_rating, field, harvest_person)
    return melon_list

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 
    for melon in melons:
        if melon.is_sellable():
            print (f"Harvested by {melon.harvest_person} from Field {melon.field} (CAN BE SOLD)")
        else:
            print (f"Harvested by {melon.harvest_person} from Field {melon.field} (NOT SELLABLE)")
        #print{f'Harvested by '}


