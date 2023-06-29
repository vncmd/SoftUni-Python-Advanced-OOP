from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, name: str):
        res = [p for p in self.products if p.name == name][0]
        if res:
            return res[0]

    def remove(self, name: str):
        product = self.find(name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        return '\n'.join([f"{x.name}: {x.quantity}" for x in self.products])
