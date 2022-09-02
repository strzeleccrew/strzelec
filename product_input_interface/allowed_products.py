from product_input_interface.product_types import ProductType


class WarehouseProducts:
    __ALLOWED_PRODUCTS_TYPE = [product_type.value for product_type in ProductType]
    __MAX_PRODUCT_NAME_LENGTH = 60
    __MIN_PRODUCT_NAME_LENGTH = 1

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
