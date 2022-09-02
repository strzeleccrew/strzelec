from product_input_interface.allowed_products import WarehouseProducts


class InputInterface:

    def __init__(self):
        self.WAREHOUSE_PRODUCTS = WarehouseProducts()
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
            self.WAREHOUSE_PRODUCTS.print_allowed_product_types()
            product_type = self.__user_input_product_type()
            if product_type.lower() == self.QUIT_LOOP:
                return self.QUIT_LOOP

            product_type_is_valid = self.WAREHOUSE_PRODUCTS.is_product_type_allowed(product_type.lower())
            if product_type_is_valid:
                return product_type
            else:
                print("Product type was not valid. Please enter valid type\n")

    def __get_product_name(self):
        while True:
            product_name = self.__user_input_product_name()
            if product_name.lower() == self.QUIT_LOOP:
                return self.QUIT_LOOP

            product_name_is_valid = self.WAREHOUSE_PRODUCTS.check_product_name_length(product_name)
            if product_name_is_valid:
                return product_name

    def __get_product_quantity(self):
        ERROR_MESSAGE = "You need to input natural number greater than 0."
        while True:
            quantity = self.__user_quantity_of_product()
            if quantity == self.QUIT_LOOP:
                return self.QUIT_LOOP

            try:
                if int(quantity) == 0 \
                        or int(quantity) < 0:
                    print(ERROR_MESSAGE)

                else:
                    return int(quantity)

            except ValueError as e:
                print(f"{ERROR_MESSAGE} {e}")

    def __get_product_info(self):
        product_type = self.__get_product_type()
        if product_type == self.QUIT_LOOP:
            return None, None, None

        product_name = self.__get_product_name()
        if product_name == self.QUIT_LOOP:
            return None, None, None

        product_quantity = self.__get_product_quantity()
        if product_quantity == self.QUIT_LOOP:
            return None, None, None

        return product_type, product_name, product_quantity

    def warehouse_interface(self):
        print(f'You can quit by typing "{self.QUIT_LOOP}"\n')
        product_type, product_name, product_quantity = self.__get_product_info()
        if not product_type:
            return None

        print("\n"
              "Summary: \n"
              f"Product type: {product_type}\n"
              f"Product name: {product_name}\n"
              f"Product quantity: {product_quantity.__str__()}\n")
