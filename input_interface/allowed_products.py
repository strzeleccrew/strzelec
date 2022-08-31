class WarehouseProducts:
    allowed_products = ["helmet", "rifle", "medkit"]
    max_product_name_lenght = 60

    def check_product_name(self, product_name):
        allowed_products = self.allowed_products
        if product_name in allowed_products:
            return True
        else:
            return False

    def check_product_name_lenght(self, product_name: str):
        allowed_lenght = self.max_product_name_lenght
        if 1 <= len(product_name) <= allowed_lenght:
            return True
        else:
            return False
