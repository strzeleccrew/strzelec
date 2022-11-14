from droguex.product_data.allowed_data_settings import AllowedDataSettings
from droguex.product_data.product_data import ProductData
from droguex.product_input_interface.allowed_products import AllowedProducts
from droguex.utils.console_cleaner import console_clean


class InputInterface:
    __QUIT = AllowedDataSettings.QUIT_COMMAND

    def __init__(self):
        self.__WAREHOUSE_ALLOWED_PRODUCTS = AllowedProducts()
        self.__PRODUCT_DATA = ProductData()

    @staticmethod
    def __user_input_product_name() -> str:
        return input("Please enter product name: ")

    @staticmethod
    def __user_input_quantity_of_product() -> str:
        return input("Please enter quantity: ")

    @staticmethod
    def __user_input_product_type() -> str:
        return input("Please enter product type: ")

    @staticmethod
    def __user_input_product_description() -> str:
        return input("Please enter description for the product: ")

    @staticmethod
    def __user_input_product_purpose() -> str:
        return input("Please enter purpose for the product: ")

    def __get_product_purpose(self) -> str:
        while True:
            self.__WAREHOUSE_ALLOWED_PRODUCTS.print_allowed_product_purpose()
            purpose = self.__user_input_product_purpose()
            if purpose.lower() == self.__QUIT:
                return self.__QUIT

            if self.__WAREHOUSE_ALLOWED_PRODUCTS.is_product_purpose_valid(purpose):
                return purpose
            else:
                print("Product purpose was not valid. Please enter valid purpose\n")

    def __get_product_type(self) -> str:
        while True:
            self.__WAREHOUSE_ALLOWED_PRODUCTS.print_allowed_product_types()
            product_type = self.__user_input_product_type()
            if product_type.lower() == self.__QUIT:
                return self.__QUIT

            product_type_is_valid = self.__WAREHOUSE_ALLOWED_PRODUCTS.is_product_type_allowed(product_type)
            if product_type_is_valid:
                return product_type
            else:
                print("Product type was not valid. Please enter valid type\n")

    def __get_product_name(self):
        while True:
            product_name = self.__user_input_product_name()
            if product_name.lower() == self.__QUIT:
                return self.__QUIT

            product_name_is_valid = self.__WAREHOUSE_ALLOWED_PRODUCTS.is_product_name_length_valid(product_name)
            if product_name_is_valid:
                return product_name

    def __get_product_quantity(self):
        ERROR_MESSAGE = "You need to input natural number greater than 0."
        while True:
            quantity = self.__user_input_quantity_of_product()
            try:
                if quantity.lower() == self.__QUIT:
                    return self.__QUIT
            except ValueError:
                pass

            try:
                if int(quantity) == 0 \
                        or int(quantity) < 0:
                    print(ERROR_MESSAGE)

                else:
                    return int(quantity)

            except ValueError as e:
                print(f"{ERROR_MESSAGE} {e}")

    def __get_product_info(self) -> None | tuple[str, str, str, str, str | int]:
        product_type = self.__get_product_type()
        if product_type == self.__QUIT:
            return None

        product_name = self.__get_product_name()
        if product_name == self.__QUIT:
            return None

        product_quantity = self.__get_product_quantity()
        if product_quantity == self.__QUIT:
            return None

        product_description = self.__user_input_product_description()
        if product_description == self.__QUIT:
            return None

        product_purpose = self.__get_product_purpose()
        if product_purpose == self.__QUIT:
            return None

        return product_name, product_description, product_type, product_purpose, product_quantity

    @console_clean
    def __show_summary(self,
                       product_name,
                       product_description,
                       product_type,
                       product_purpose,
                       product_quantity):
        print("\n"
              "Summary: \n"
              f"Product name: {product_name}\n"
              f"Product description: {product_description.__str__()}\n"
              f"Product type: {product_type}\n"
              f"Product purpose: {product_purpose.__str__()}\n"
              f"Product quantity: {product_quantity.__str__()}\n"
              )

    @console_clean
    def warehouse_interface(self):
        print(f'You can quit by typing "{self.__QUIT}"\n')
        product_temp = self.__get_product_info()
        if not product_temp:
            return None

        self.__show_summary(*product_temp)

        save_choice = input("Do you want to save this product? y/n ").lower()
        if save_choice != 'y' and save_choice != 'n':
            while save_choice == 'y' or save_choice == 'n' or save_choice != self.__QUIT:
                save_choice = input("There is no such option, please enter 'y' or 'n' ").lower()

        match save_choice:
            case 'y':
                self.__PRODUCT_DATA.add_new_product_to_memory(product_temp)
            case 'n':
                print("Product will not be saved")
            case self.__QUIT:
                print("Product will not be saved")
            case _:
                print("Something went wrong!")
