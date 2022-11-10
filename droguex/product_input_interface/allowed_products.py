from droguex.product_data.allowed_data import AllowedData
from droguex.product_data.product_data import ProductData


class AllowedProducts:
    __ALLOWED_PRODUCTS_TYPE = ProductData.product_types
    __MAX_PRODUCT_NAME_LENGTH = AllowedData.MAX_CHAR_FOR_PRODUCT_NAME
    __MIN_PRODUCT_NAME_LENGTH = AllowedData.MIN_CHAR_FOR_PRODUCT_NAME

    def __get_allowed_product_types_formated(self) -> str:
        allowed_types_formated = ""
        for item in self.__ALLOWED_PRODUCTS_TYPE:
            allowed_types_formated = f"{allowed_types_formated}-{item}\n"

        return allowed_types_formated

    def print_allowed_product_types(self):
        print("Allowed product types:")
        print(self.__get_allowed_product_types_formated())

    def is_product_type_allowed(self, product_type: str) -> bool:
        if product_type in self.__ALLOWED_PRODUCTS_TYPE:
            return True
        else:
            return False

    def check_product_name_length(self, product_name: str) -> bool:
        if self.__MIN_PRODUCT_NAME_LENGTH <= len(product_name) <= self.__MAX_PRODUCT_NAME_LENGTH:
            return True

        elif len(product_name) > self.__MAX_PRODUCT_NAME_LENGTH:
            print(f"Product name is too long (max {self.__MAX_PRODUCT_NAME_LENGTH.__str__()} characters)")

        elif len(product_name) < self.__MIN_PRODUCT_NAME_LENGTH:
            print(f"Product name is too short (min {self.__MIN_PRODUCT_NAME_LENGTH.__str__()} characters)")

        return False
