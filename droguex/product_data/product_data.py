from droguex.product_data.product import Product
from droguex.product_data.product_types import ProductTypes
from droguex.utils.console_cleaner import console_clean


class ProductData:
    # This class will store in memory all product types for now as in database
    product_types = [i.value for i in ProductTypes]
    product_objects = []  # temporary memory to store objects
    id = 0

    def __get_id_for_new_product(self) -> int:
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
        self.product_objects.append(Product(self.__get_id_for_new_product(), *product_temp))

    def __get_product_by_id(self, product_id):
        for i in self.product_objects:
            if i.id == product_id:
                return i

        return None

    def is_product_in_memory_by_id(self, product_id) -> bool:
        return True if any(i.id == product_id for i in self.product_objects) else False

    def remove_product_by_id(self, product_id: int):
        if self.is_product_in_memory_by_id(product_id):
            product = self.__get_product_by_id(product_id)
            self.product_objects.remove(product)
        else:
            print("Product with such id is not in memory")

    def show_product_by_id(self, product_id):
        try:
            print(vars(self.__get_product_by_id(product_id)))
        except TypeError:
            print(f"There is product with id '{product_id}' in memory")
