from allowed_products import WarehouseProducts


class InputInterface:

    @staticmethod
    def user_input_product_name():
        return input("Please enter product name: ")

    @staticmethod
    def user_quantity_of_product():
        return input("Please enter quantity: ")

