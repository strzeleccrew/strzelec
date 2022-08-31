class WarehouseProducts:
    __ALLOWED_PRODUCTS_TYPE = ["helmet", "rifle", "medkit"]
    __MAX_PRODUCT_NAME_LENGTH = 60
    __MIN_PRODUCT_NAME_LENGTH = 1

    def print_allowed_product_types(self):
        print("Allowed product types:")
        for item in self.__ALLOWED_PRODUCTS_TYPE:
            print(f"- {item}")

    def check_product_type(self, product_type: str):
        if product_type in self.__ALLOWED_PRODUCTS_TYPE:
            return True
        else:
            print("Product type was not valid.")
            return False

    def check_product_name_length(self, product_name: str):
        if self.__MIN_PRODUCT_NAME_LENGTH <= len(product_name) <= self.__MAX_PRODUCT_NAME_LENGTH:
            return True

        elif len(product_name) > 60:
            print(f"Product name is too long (max {self.__MAX_PRODUCT_NAME_LENGTH.__str__()} characters)")

        elif len(product_name) == 0:
            print(f"Product name is too short (min {self.__MIN_PRODUCT_NAME_LENGTH.__str__()} characters)")

        return False
