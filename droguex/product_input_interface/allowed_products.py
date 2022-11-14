from droguex.product_data.allowed_data_settings import AllowedDataSettings
from droguex.product_data.product_data import ProductData


class AllowedProducts:
    __ALLOWED_PRODUCTS_TYPE = ProductData.product_types
    __PURPOSE = ProductData.product_purposes

    __MAX_PRODUCT_NAME_LENGTH = AllowedDataSettings.MAX_CHAR_FOR_PRODUCT_NAME
    __MIN_PRODUCT_NAME_LENGTH = AllowedDataSettings.MIN_CHAR_FOR_PRODUCT_NAME

    def __get_allowed_product_types_formatted(self) -> str:
        return "".join(f"-{i}\n" for i in self.__ALLOWED_PRODUCTS_TYPE)

    def print_allowed_product_types(self):
        print("Allowed product types:")
        print(self.__get_allowed_product_types_formatted())

    def is_product_type_allowed(self, product_type: str) -> bool:
        return True if product_type.lower() in self.__ALLOWED_PRODUCTS_TYPE else False

    def is_product_name_length_valid(self, product_name: str) -> bool:
        if self.__MIN_PRODUCT_NAME_LENGTH <= len(product_name) <= self.__MAX_PRODUCT_NAME_LENGTH:
            return True

        elif len(product_name) > self.__MAX_PRODUCT_NAME_LENGTH:
            print(f"Product name is too long (max {self.__MAX_PRODUCT_NAME_LENGTH.__str__()} characters)")

        elif len(product_name) < self.__MIN_PRODUCT_NAME_LENGTH:
            print(f"Product name is too short (min {self.__MIN_PRODUCT_NAME_LENGTH.__str__()} characters)")

        return False

    def __get_allowed_product_purposes_formatted(self) -> str:
        return "".join(f"-{i}\n" for i in self.__PURPOSE)

    def is_product_purpose_valid(self, product_purpose) -> bool:
        return True if product_purpose in self.__PURPOSE else False

    def print_allowed_product_purpose(self):
        print(f"Allowed purpose:")
        print(self.__get_allowed_product_purposes_formatted())
