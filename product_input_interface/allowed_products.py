class WarehouseProducts:
    __allowed_products_type = ["helmet", "rifle", "medkit"]
    __max_product_name_length = 60
    __min_product_name_length = 1

    def print_allowed_product_types(self):
        print("Allowed product types:")
        for item in self.__allowed_products_type:
            print(f"- {item}")

    def check_product_type(self, product_type: str):
        allowed_products = self.__allowed_products_type
        if product_type in allowed_products:
            return True
        else:
            print("Product type was not valid.")
            return False

    def check_product_name_length(self, product_name: str):
        allowed_length = self.__max_product_name_length
        if 1 <= len(product_name) <= allowed_length:
            return True

        elif len(product_name) > 60:
            print(f"Product name is too long (max {self.__max_product_name_length.__str__()} characters)")

        elif len(product_name) == 0:
            print(f"Product name is too short (min {self.__min_product_name_length.__str__()} characters)")

        return False
