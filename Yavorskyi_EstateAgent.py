def get_valid_input(input_string, valid_optoins):
    """
    str, tuple -> str


    """
    input_string += "({})".format(", ".join(valid_optoins))
    response = input(input_string)
    while response.lower() not in valid_optoins:
        response = input(input_string)
    return response


class Property:
    """
    Class represents property (building) it`s area, beds baths and other
    options
    """

    def __init__(self, square_feet='', beds='',
                 baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        Property -> None

        Prints info about property
        """
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        Static method which constructs the object of class Property
        :return dict
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter a number of bedrooms: "),
                    baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    """
    Class displays the specific kind of property - apartment
    With available laundries and balconies
    """
    valid_laundries = ('coin', 'ensuite', 'none')
    valid_balconies = ('yes', 'no', 'solarium')

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        Apartment -> None

        Uses the display func from class Property and adds details featured for
        apartment (laundry, balcony)
        """
        super().display()
        print("APARTMENT DETAILS")
        print('laundry: %s' % self.laundry)
        print('has balcony : %s' % self.balcony)

    def prompt_init():
        """
        Static method which uses the parent`s prompt_init and adds to it`s dict
        laundry and balcony info
        """
        parent_init = Property.prompt_init()
        laundry = get_valid_input("What laundry facilitirs does"
                                  "the property have? ",
                                  Apartment.valid_laundries)
        balcony = get_valid_input("Does the property have a balcony?",
                                  Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    """
    Class that represents private house which has same attributes as object of
    class property + garage, fenced, and stories
    """
    valid_garage = ('attached', 'detached', 'none')
    valid_fenced = ('yes', 'no')

    def __init__(self, num_stories='',
                 garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        House -> None

        Uses the display func from class Property and adds details featured for
        house (number of stories, garage, fenced)
        """
        super().display()
        print('HOUSE DETAILS')
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """
        Static method which uses the parent`s prompt_init and adds to it`s dict
        info about fence, garage and number of stories
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)
        num_stories = input("How many stories? ")

        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    """
    Class represents the purchase operation (price of property + taxes)
    """

    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        Purchase -> None

        Prints the info about Purchase
        """
        super().display()
        print(" PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """
        Static method forms the dict with info keys price and taxes
        """
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are estimated taxes? "))

    prompt_init = staticmethod(prompt_init)


class Rental:
    """
    Class that represents rental operation (furniture, featured utilities,
    rent price)
    """

    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        Rental -> None
        Prints the info about rent
        """
        super().display()
        print("RENTAL DETAILS")
        print('rent: {}'.format(self.rent))
        print("estimated utilities: {}".format(
            self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        Static method forms a dict with keys rent(price) utilities and
         furnished
        """
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input(
                "What are the estimated utilities? "),
            furnished=get_valid_input("Is the property furnished? ",
                                      ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    """
    Class represents house rental
    """

    def prompt_init():
        """
        Static method that uses method prompt_init from class House and updates
        it with method prompt init of class Rental.
        :return dict
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    """
    Class represents apartment rental
    """

    def prompt_init():
        """
        Static method that uses method prompt_init from class Apartment
        and updates it with method prompt init of class Rental.
        :return dict
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    """
    Class represents apartment purchase
    """

    def prompt_init():
        """
        Static method that uses method prompt_init from class Apartment
        and updates it with method prompt init of class Purchase.
        :return dict
        """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    """
    Class represents house purchase
    """

    def prompt_init():
        """
        Static method that uses method prompt_init from class House
        and updates it with method prompt init of class Purchase.
        :return dict
        """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class Agent:
    """
    Class represents agent which sales/ gives for a rent property
    """

    def __init__(self):
        self.property_list = []

    def display_properties(self):
        """
        Agent -> None

        Prints all properties using valid display method for each property in
        property_list
        """
        for property in self.property_list:
            property.display()

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def add_property(self):
        """
        Agent -> None

        Allows to construct an object which fits input conditions
        """
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()

        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

    def reset_agent(self):
        """
        Agent -> None
        Resets the properties of agent
        """
        self.property_list = []

    def remove_property(self):
        """
        Agent -> None
        Removes given property
        """
        print("Properties of this agent:")

        for number, prop in enumerate(self.property_list):
            print("Number " + str(number + 1))
            prop.display()
        del self.property_list[
            int(input("Number of property to delete: ")) - 1]
        print("Now the properties are:")
        self.display_properties()