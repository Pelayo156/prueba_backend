from decimal import Decimal
from django.conf import settings
from products.models import Product

# Clase carrito para manejar el mismo a través de las sesiones.
class Cart:
    # Constructor de la clase carrito. De esta forma obtengo la session del usuario y se la asigno a la instancia de carrito.
    # En el caso de que no existiera el carrito de compras de la session, lo inicializa como un diccionario vacío.
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # Método para agregar un producto al carrito.
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += 1
        self.save()

    # Método para guardar el carrito actualizado en la session.
    # Con self.session.modified = True indico que la session ha sido modificada y necesita ser guardada.
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    # Método para remover un producto del carrito.
    def remove(self, product):
        product_id = str(product.product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # Método para iterar sobre los elementos del carrito
    def __iter__(self):
        # Obtengo los ids de los productos que han sido agregados al carrito
        product_ids = self.cart.keys()
        # Obtengo los productos que coincidan con el id de la lista de productos anterior desde la base de datos
        products = Product.objects.filter(product_id__in=product_ids)
        for product in products:
            self.cart[str(product.product_id)]['product'] = product

        for item in self.cart.values():
            item['total_price'] = item['price'] * item['quantity']
            # Con yield puedo hacer que esta función me retorne un objeto iterable (no es una lista)
            yield item

    # Método para retornar cantidad total de productos
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    # Método para obtener el precio total del carrito
    def get_total_price(self):
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    # Método para limpiar el carrito de compras y dejarlo sin productos dentro
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True