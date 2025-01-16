import json


class Product:
    def __init__(self, id, name, qnt=0):
        self.id = id
        self.name = name
        self.qnt = qnt


class Inventory:
    def __init__(self):
        self.products = []

    def save_json(self, filename):
        data = [
            {"id": product.id, "name": product.name, "qnt": product.qnt}
            for product in self.products
        ]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_json(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
            self.products = [
                Product(item["id"], item["name"], item["qnt"]) for item in data
            ]

    def add_product(self, name, id, qnt):
        for product in self.products:
            if product.id == id:
                if product.name == name:
                    if qnt != 0:
                        product.qnt += qnt
                        return
                    else:
                        product.qnt == 1
                        return
                else:
                    return

        product = Product(id, name, qnt)
        self.products.append(product)

    def edit_product(self, id, name, qnt):
        for product in self.products:
            if product.id == id:
                product.name = name
                product.qnt = qnt
                break

    def remove_product(self, id):
        self.products = [product for product in self.products if product.id == id]

    def get_products(self):
        return self.products

    def clear(self):
        self.products = []
        return
