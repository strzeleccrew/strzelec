from droguex.product_data.product_types_enum import ProductType
from droguex.utils.console_cleaner import console_clean


class ProductData:
    # This class will store in memory all product types for now
    product_types = [i.value for i in ProductType]
    product_objects = []  # temporary memory to store objects
    id = 0

    @console_clean
    def show_products_in_werehouse(self):
        print("-" * 30,
              "\nList of products in werehouse:")
        if self.product_objects:
            for i in self.product_objects:
                print(vars(i))

        print("-" * 30)
