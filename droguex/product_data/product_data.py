from droguex.product_data.product import Product
from droguex.product_data.product_types import ProductTypes
from droguex.utils.console_cleaner import console_clean


class ProductData:
    # This class will store in memory all product types for now as in database
    product_types = [i.value for i in ProductTypes]
    product_objects = []  # temporary memory to store objects
    id = 0

    @staticmethod
    def __get_id_for_new_product() -> int:
        ProductData.id += 1
        return ProductData.id

    @console_clean
    def show_products_in_werehouse(self):
        print("-" * 30,
              "\nList of products in werehouse:")
        if self.product_objects:
            for i in self.product_objects:
                print(vars(i))

        print("-" * 30)

    def add_new_product_to_memory(self, product_temp: tuple):
        ProductData.product_objects.append(Product(self.__get_id_for_new_product(), *product_temp))
