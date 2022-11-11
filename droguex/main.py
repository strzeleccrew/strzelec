from droguex.product_input_interface.input_interface import InputInterface
from droguex.product_type_creator.type_creator_interface import ProductTypeCreatorInterface
from droguex.product_data.product_data import ProductData


class Main:
    __ADD_CHOICE = '1'
    __CREATE_NEW_TYPE_CHOICE = '2'
    __SHOW_WEREHOUSE_CHOICE = '3'
    __EXIT_CHOICE = '0'

    def __init__(self):
        self.__interface = InputInterface()
        self.__product_creator_interface = ProductTypeCreatorInterface()
        self.__product_data = ProductData()

    def main_menu(self):
        while True:

            print(
                f"Hello user. Choose what you want to do:\n"
                f"{self.__ADD_CHOICE}. Add new product\n"
                f"{self.__CREATE_NEW_TYPE_CHOICE}. Create new product type\n"
                f"{self.__SHOW_WEREHOUSE_CHOICE}. Show products in werehouse\n"
                f"{self.__EXIT_CHOICE}. Quit\n"
            )
            choice = input("Enter choice: ")
            match choice:
                case self.__ADD_CHOICE:
                    self.__interface.warehouse_interface()
                case self.__CREATE_NEW_TYPE_CHOICE:
                    self.__product_creator_interface.interface()
                case self.__SHOW_WEREHOUSE_CHOICE:
                    self.__product_data.show_products_in_werehouse()
                case self.__EXIT_CHOICE:
                    break
                case _:
                    print("There is no such choice. Please enter valid choice")


if __name__ == '__main__':
    Main().main_menu()
