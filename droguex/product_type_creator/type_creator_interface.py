from droguex.product_input_interface.input_interface import InputInterface
from droguex.product_data.allowed_data import AllowedData
from droguex.product_data.product_data import ProductData
from droguex.utils.console_cleaner import console_clean


class ProductTypeCreatorInterface:
    __existing_product_types = ProductData.product_types
    __new_product_type = ""
    __QUIT_LOOP = InputInterface.QUIT_LOOP
    __MIN_CHAR_FOR_TYPE = AllowedData.MIN_CHAR_FOR_PRODUCT_TYPE
    __MAX_CHAR_FOR_TYPE = AllowedData.MAX_CHAR_FOR_PRODUCT_TYPE

    def __show_existing_product_types(self):
        print("List of existing product types:")
        for i in self.__existing_product_types:
            print(f"- {i}")

    def __set_new_product_type(self):
        self.__new_product_type = input("Please enter new product type name\n").lower()

    def __validate_existence_of_new_product_type(self):
        if self.__new_product_type in self.__existing_product_types:
            return True
        else:
            return False

    def __verify_type_is_valid(self):
        if self.__MIN_CHAR_FOR_TYPE <= len(self.__new_product_type) <= self.__MAX_CHAR_FOR_TYPE:
            return True
        else:
            return False

    def __save_product_type(self):
        self.__existing_product_types.append(self.__new_product_type)

    def __product_type_creator(self):
        self.__show_existing_product_types()
        self.__set_new_product_type()
        if self.__new_product_type == self.__QUIT_LOOP:
            return False

        if not self.__verify_type_is_valid():
            print("Entered type is not valid.")

        if self.__validate_existence_of_new_product_type():
            print("Entered product type is already existing")

        else:
            print("Entered product type is valid.")

        return True

    def __ask_user_to_save_type(self):
        choice = ""
        print("You entered new product type:\n"
              f"{self.__new_product_type}\n"
              f"{'-' * 30}")

        while choice != "y" or choice != "n":
            choice = input("Do you want to save new product type? y/n ")
            if choice == "y":
                return True
            elif choice == "n" or choice == self.__QUIT_LOOP:
                return False
            else:
                print('Invalid choice. Please enter "y" to save or "n" to cancel')

    @console_clean
    def interface(self):
        while True:
            print(f"{'-' * 30}\n"
                  f'If you want to quit this module, type "{self.__QUIT_LOOP}"\n'
                  f"{'-' * 30}")
            self.__product_type_creator()
            if self.__new_product_type == self.__QUIT_LOOP:
                break

            if self.__ask_user_to_save_type():
                self.__save_product_type()

            choice = input("Do you want to add another product type? y/n ")
            if choice.lower() != 'y' and choice.lower() != 'n':
                choice = input("There is no such option. please enter 'y' or 'n' ")

            match choice.lower():
                case 'y':
                    pass
                case 'n':
                    break
                case _:
                    print("Something went wrong. Quiting module.")
                    break
