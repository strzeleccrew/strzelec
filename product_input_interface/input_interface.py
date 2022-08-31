from product_input_interface.allowed_products import WarehouseProducts


class InputInterface:

    def __init__(self):
        self.WAREHOUSE = WarehouseProducts()
        self.QUIT_LOOP = "quit"

    @staticmethod
    def __user_input_product_name():
        return input("Please enter product name: ")

    @staticmethod
    def __user_quantity_of_product():
        return input("Please enter quantity: ")

    @staticmethod
    def __user_input_product_type():
        return input("Please enter product type:")

    def __get_product_type(self):
        while True:
            self.WAREHOUSE.print_allowed_product_types()
            product_type = self.__user_input_product_type()
            if product_type.lower() == self.QUIT_LOOP:
                return self.QUIT_LOOP

            product_type_is_valid = self.WAREHOUSE.check_product_type(product_type.lower())
            if product_type_is_valid:
                return product_type

    def __get_product_name(self):
        while True:
            product_name = self.__user_input_product_name()
            if product_name.lower() == self.QUIT_LOOP:
                return self.QUIT_LOOP

            product_name_is_valid = self.WAREHOUSE.check_product_name_length(product_name)
            if product_name_is_valid:
                return product_name

    def __get_product_quantity(self):
        quantity = self.__user_quantity_of_product()
        if quantity == self.QUIT_LOOP:
            return self.QUIT_LOOP

        if int(quantity) == 0:
            print("You cant add 0 quantity")
        else:
            return int(quantity)

    def __get_product_dict(self):
        product_type = self.__get_product_type()
        if product_type == self.QUIT_LOOP:
            return None

        product_name = self.__get_product_name()
        if product_name == self.QUIT_LOOP:
            return None

        product_quantity = self.__get_product_quantity()
        if product_quantity == self.QUIT_LOOP:
            return None

        return {"type": product_type, "name": product_name, "quantity": product_quantity}

    def warehouse_interface(self):
        print('You can quit by typing "quit"')
        product = self.__get_product_dict()
        if not product:
            return None

        print("\n"
              "Summary: \n"
              f"Product type: {product['type']}\n"
              f"Product name: {product['name']}\n"
              f"Product quantity: {product['quantity'].__str__()}\n")
