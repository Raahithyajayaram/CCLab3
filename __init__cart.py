'''import json

import products
from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list:
    cart_details = dao.get_cart(username)
    if cart_details is None:
        return []
    
    items = []
    for cart_detail in cart_details:
        contents = cart_detail['contents']
        evaluated_contents = eval(contents)  
        for content in evaluated_contents:
            items.append(content)
    
    i2 = []
    for i in items:
        temp_product = products.get_product(i)
        i2.append(temp_product)
    return i2

    


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str):
    dao.delete_cart(username)
'''
import json

from typing import List

from products import Product

from cart import dao





class Cart:

    def __init__(self, id: int, username: str, contents: List[Product], cost: float):

        """

        Represents a shopping cart.

        :param id: Cart ID

        :param username: Associated username

        :param contents: List of product objects in the cart

        :param cost: Total cost of the cart

        """

        self.id = id

        self.username = username

        self.contents = contents

        self.cost = cost



    @staticmethod

    def load(data: dict) -> "Cart":

        """

        Load a Cart instance from a dictionary.

        """

        return Cart(

            id=data["id"],

            username=data["username"],

            contents=[Product(**product_data) for product_data in data["contents"]],

            cost=data["cost"],

        )





def get_cart(username: str) -> List[Product]:

    """

    Fetch the cart details for a user.



    :param username: The username whose cart is being fetched.

    :return: A list of Product objects in the cart.

    """

    cart_details = dao.get_cart(username)

    if not cart_details:

        return []



    # Collect all product IDs from cart contents

    product_ids = {

        product_id

        for cart_detail in cart_details

        for product_id in json.loads(cart_detail["contents"])

    }



    # Fetch product details in bulk and map by ID

    products_map = {

        product.id: product

        for product in products.get_products(list(product_ids))

    }

    # Return product objects corresponding to the IDs

    return [products_map[pid] for pid in product_ids if pid in products_map]

def add_to_cart(username: str, product_id: int) -> None:

    """

    Add a product to the cart.

    :param username: The username to add the product for.

    :param product_id: The product ID to add.

    """

    dao.add_to_cart(username, product_id)

def remove_from_cart(username: str, product_id: int) -> None:

    """

    Remove a product from the cart.
    :param username: The username to remove the product for.

    :param product_id: The product ID to remove.

    """

    dao.remove_from_cart(username, product_id)

def delete_cart(username: str) -> None:

    """

    Delete the cart for a user.
    :param username: The username whose cart is to be deleted.

    """

    dao.delete_cart(username)

