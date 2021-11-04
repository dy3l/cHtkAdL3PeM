import csv
from datetime import date

from pydantic import BaseModel, HttpUrl, confloat, conint, constr


class Offer(BaseModel):
    title: str
    price: conint(gt=0, lt=32000)
    link: HttpUrl
    images: HttpUrl
    store_id: constr(regex=r"[a-z]+")
    product_id: str


class Product(BaseModel):
    id: constr(regex=r"[a-z0-9-+]+")
    brand: constr(regex=r"(Apple|Google|Huawei|Infinix|Oppo|Samsung|Xiaomi)")
    model: constr(min_length=1)
    ram_size: conint(gt=0, lt=24)
    storage_size: conint(gt=0, lt=2048, multiple_of=2)
    display_diagonal: confloat(gt=0, lt=8)
    display_resolution: str
    display_type: str
    chipset: str
    body_weight: conint(gt=0, lt=300)
    battery_capacity: conint(gt=0, lt=8000)
    release_date: date


class Store(BaseModel):
    id: constr(regex=r"[a-z]+")
    name: constr(min_length=3)
    website: HttpUrl


def test_offers():
    with open("data/offers.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        offers = list(reader)
    for offer in offers:
        Offer(
            title=offer["title"],
            price=offer["price"],
            link=offer["link"],
            images=offer["images"],
            store_id=offer["store_id"],
            product_id=offer["product_id"],
        )


def test_products():
    with open("data/products.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        products = list(reader)
    for product in products:
        Product(
            id=product["id"],
            brand=product["brand"],
            model=product["model"],
            ram_size=product["ram_size"],
            storage_size=product["storage_size"],
            display_diagonal=product["display_diagonal"],
            display_resolution=product["display_resolution"],
            display_type=product["display_type"],
            chipset=product["chipset"],
            body_weight=product["body_weight"],
            battery_capacity=product["battery_capacity"],
            release_date=product["release_date"],
        )


def test_stores():
    with open("data/stores.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        stores = list(reader)
    for store in stores:
        Store(
            id=store["id"],
            name=store["name"],
            website=store["website"],
        )


test_products()
test_offers()
test_stores()
