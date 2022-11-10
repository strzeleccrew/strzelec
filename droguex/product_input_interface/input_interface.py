from droguex.product_data.product import Product
from droguex.product_data.product_data import ProductData
from droguex.product_input_interface.allowed_products import AllowedProducts
from droguex.utils.console_cleaner import console_clean
from droguex.product_data.product_purpose import ProductPurpose


class InputInterface:
    QUIT_LOOP = "quit"

    def __init__(self):
        self.__WAREHOUSE_PRODUCTS = AllowedProducts()
        self.__PURPOSE = [i.value for i in ProductPurpose]

    @staticmethod
    def __user_input_product_name():
        return input("Please enter product name: ")

    @staticmethod
    def __user_quantity_of_product():
        return input("Please enter quantity: ")

    @staticmethod
    def __user_input_product_type():
        return input("Please enter product type: ")

    def __user_input_product_description(self):
        return input("Please enter description for the product: ")

    def __user_input_product_purpose(self):
        return input("Please enter purpose for the product: ")

    def __is_product_purpose_valid(self, product_purpose):
        return True if product_purpose in self.__PURPOSE else False

    def __get_product_purpose(self):
        print(f"Allowed purpose:")
        for i in self.__PURPOSE:
            print(f"- {i}")

        purpose = self.__user_input_product_purpose()
        if purpose == self.QUIT_LOOP:
            return None

        if self.__is_product_purpose_valid(purpose):
            return purpose

    def __get_product_type(self):
        while True:
            self.__WAREHOUSE_PRODUCTS.print_allowed_product_types()
            product_type = self.__user_input_product_type()
            if product_type.lower() == self.QUIT_LOOP:
                return self.QUIT_LOOP

            product_type_is_valid = self.__WAREHOUSE_PRODUCTS.is_product_type_allowed(product_type.lower())
            if product_type_is_valid:
                return product_type
            else:
                print("Product type was not valid. Please enter valid type\n")

    def __get_product_name(self):
        while True:
            product_name = self.__user_input_product_name()
            if product_name.lower() == self.QUIT_LOOP:
                return self.QUIT_LOOP

            product_name_is_valid = self.__WAREHOUSE_PRODUCTS.check_product_name_length(product_name)
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

    def __get_id_for_product(self):
        ProductData.id += 1
        return ProductData.id

    def __get_product_info(self):
        product_type = self.__get_product_type()

        def quit_loop():
            return None, None, None, None, None

        if product_type == self.QUIT_LOOP:
            return quit_loop()

        product_name = self.__get_product_name()
        if product_name == self.QUIT_LOOP:
            return quit_loop()

        product_quantity = self.__get_product_quantity()
        if product_quantity == self.QUIT_LOOP:
            return quit_loop()

        product_decription = self.__user_input_product_description()
        if product_decription == self.QUIT_LOOP:
            return quit_loop()

        product_purpose = self.__get_product_purpose()
        if product_purpose == self.QUIT_LOOP:
            return quit_loop()

        return product_type, \
               product_name, \
               product_quantity, \
               product_decription, \
               self.__get_id_for_product(), \
               product_purpose

    @console_clean
    def __show_summary(self, product_type,
                       product_name,
                       product_quantity,
                       product_description,
                       product_id,
                       product_purpose):
        print("\n"
              "Summary: \n"
              f"Product type: {product_type}\n"
              f"Product name: {product_name}\n"
              f"Product quantity: {product_quantity.__str__()}\n"
              f"Product description: {product_description.__str__()}\n"
              f"Product id: {product_id.__str__()}\n"
              f"Product purpose: {product_purpose.__str__()}\n"
              )

    @console_clean
    def warehouse_interface(self):
        print(f'You can quit by typing "{self.QUIT_LOOP}"\n')
        product_type, \
        product_name, \
        product_quantity, \
        product_decription, \
        product_id, \
        product_purpose = self.__get_product_info()

        if not product_type:
            return None
        self.__show_summary(product_type,
                            product_name,
                            product_quantity,
                            product_decription,
                            product_id,
                            product_purpose)

        save_choice = input("Do you want to save this product? y/n ")
        if save_choice != 'y' and save_choice != 'n':
            while True:
                save_choice = input("There is no such option, please enter 'y' or 'n' ")

        match save_choice:
            case 'y':
                ProductData.product_objects.append(
                    Product(product_name, product_purpose, product_type, product_decription, product_id))
            case 'n':
                print("Product will not be saved")
            case _:
                print("Something went wrong!")
