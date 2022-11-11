from droguex.product_data.allowed_data_settings import AllowedDataSettings
from droguex.product_data.product_data import ProductData
from droguex.utils.console_cleaner import console_clean


class ProductTypeCreatorInterface:
    __existing_product_types = ProductData.product_types
    __new_product_type = ""
    __QUIT = AllowedDataSettings.QUIT_COMMAND
    __MIN_CHAR_FOR_TYPE = AllowedDataSettings.MIN_CHAR_FOR_PRODUCT_TYPE
    __MAX_CHAR_FOR_TYPE = AllowedDataSettings.MAX_CHAR_FOR_PRODUCT_TYPE

    def __user_input_new_product_type(self) -> str:
        return input("Please enter new product type name\n").lower()

    def __get_existing_product_types_formatted(self) -> str:
        return "".join(f"-{i}\n" for i in self.__existing_product_types)

    def __show_existing_product_types(self):
        print("List of existing product types:\n"
              f"{self.__get_existing_product_types_formatted()}")

    def __set_new_product_type(self):
        self.__new_product_type = self.__user_input_new_product_type()

    def __validate_existence_of_new_product_type(self):
        return True if self.__new_product_type in self.__existing_product_types else False

    def __verify_type_is_valid(self):
        return True if self.__MIN_CHAR_FOR_TYPE <= len(self.__new_product_type) <= self.__MAX_CHAR_FOR_TYPE else False

    def __save_product_type(self):
        self.__existing_product_types.append(self.__new_product_type)

    def __product_type_creator(self):
        while True:
            self.__show_existing_product_types()
            self.__set_new_product_type()

            if self.__new_product_type == self.__QUIT:
                break

            if not self.__verify_type_is_valid():
                print("Entered type is not valid.")

            if self.__validate_existence_of_new_product_type():
                print("Entered product type is already existing")

            else:
                print("Entered product type is valid.")
                break

    def __ask_user_to_save_type(self) -> bool:
        choice = ""
        print("You entered new product type:\n"
              f"{self.__new_product_type}\n"
              f"{'-' * 30}")

        while choice != "y" or choice != "n" or choice != self.__QUIT:
            choice = input("Do you want to save new product type? y/n ").lower()
            match choice:
                case 'y':
                    return True
                case 'n':
                    return False
                case self.__QUIT:
                    return False
                case _:
                    print('Invalid choice. Please enter "y" to save or "n" to cancel')

    @console_clean
    def interface(self):
        while True:
            print(f"{'-' * 30}\n"
                  f'If you want to quit this module, type "{self.__QUIT}"\n'
                  f"{'-' * 30}")
            self.__product_type_creator()
            if self.__new_product_type == self.__QUIT:
                break

            if self.__ask_user_to_save_type():
                self.__save_product_type()

            choice = input("Do you want to add another product type? y/n ").lower()
            while choice != 'y' and choice != 'n' and choice != self.__QUIT:
                choice = input("There is no such option. please enter 'y' or 'n' ").lower()

            match choice:
                case 'y':
                    pass
                case 'n':
                    break
                case self.__QUIT:
                    break
                case _:
                    print("Something went wrong. Quiting module.")
                    break
