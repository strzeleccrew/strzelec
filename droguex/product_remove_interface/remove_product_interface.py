from droguex.utils.console_cleaner import console_clean
from droguex.product_data.allowed_data_settings import AllowedDataSettings
from droguex.product_data.product_data import ProductData


class ProductRemoveInterface:
    __QUIT = AllowedDataSettings.QUIT_COMMAND
    __product_id_to_delete = 0

    def __init__(self):
        self.__PRODUCT_DATA = ProductData()

    def __set_product_id_to_delete(self, product_id):
        self.__product_id_to_delete = product_id
        print(f"I have set product id {self.__product_id_to_delete}")

    def __user_input_id(self) -> str:
        return input("Please enter ID of product you want to delete: ")

    def __ask_user_for_id(self) -> int | None:
        ERROR_MESSAGE = "You need to input natural number greater than 0."
        while True:
            quantity = self.__user_input_id()
            try:
                if quantity.lower() == self.__QUIT:
                    return None

            except ValueError:
                pass

            try:
                if int(quantity) < 0:
                    print(ERROR_MESSAGE)

                else:
                    return int(quantity)

            except ValueError as e:
                print(f"{ERROR_MESSAGE} {e}")

    def __delete_product(self):
        self.__PRODUCT_DATA.remove_product_by_id(self.__product_id_to_delete)

    def __no_product_with_id(self):
        print(f"There is no such product with id {self.__product_id_to_delete}")

    @console_clean
    def __ask_user_to_delete(self) -> bool:
        print("You want to delete product from memory:")
        self.__PRODUCT_DATA.show_product_by_id(self.__product_id_to_delete)

        user_answer = input("Do you want to delete this product? y/n ").lower()
        if user_answer != 'y' and user_answer != 'n' and user_answer != self.__QUIT:
            while user_answer != 'y' and user_answer != 'n' and user_answer == self.__QUIT:
                user_answer = input("There is no such option? type 'y' to delete or 'n' to cancel ").lower()

        match user_answer:
            case 'y':
                return True
            case 'n':
                return False
            case self.__QUIT:
                return False
            case _:
                return False

    @console_clean
    def interface(self):
        print(f'You can quit by typing "{self.__QUIT}"\n'
              f'{"-" * 30}')
        self.__set_product_id_to_delete(self.__ask_user_for_id())
        if not self.__PRODUCT_DATA.is_product_in_memory_by_id(self.__product_id_to_delete):
            self.__no_product_with_id()
            return None

        if self.__ask_user_to_delete():
            self.__delete_product()
