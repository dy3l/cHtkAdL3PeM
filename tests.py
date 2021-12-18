import csv
from datetime import date

from pydantic import BaseModel, HttpUrl, confloat, conint, constr


class Product(BaseModel):
    id: constr(regex=r"[a-z0-9-+]+")
    brand: constr(regex=r"(Apple|Google|Huawei|Infinix|Oppo|Samsung|Xiaomi)")
    model: constr(min_length=1)
    display_diagonal: confloat(gt=0, lt=8)
    display_resolution: str
    display_type: str
    chipset: str
    body_weight: conint(gt=0, lt=300)
    battery_capacity: conint(gt=0, lt=8000)
    release_date: date


class ProductVariant(BaseModel):
    id: constr(regex=r"[a-z0-9-+]+")
    ram_size: conint(gt=0, lt=24)
    storage_size: conint(gt=0, lt=2048, multiple_of=2)
    product_id: constr(regex=r"[a-z0-9-+]+")


class Store(BaseModel):
    id: constr(regex=r"[a-z]+")
    name: constr(min_length=3)
    website: HttpUrl


class Offer(BaseModel):
    title: str
    price: conint(gt=0, lt=32000)
    link: HttpUrl
    images: HttpUrl
    store_id: constr(regex=r"[a-z]+")
    product_variant_id: str


def read_csv(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        return list(reader)


products = read_csv("data/products.csv")
product_variants = read_csv("data/product_variants.csv")
stores = read_csv("data/stores.csv")
offers = read_csv("data/offers.csv")


def test_products():
    for product in products:
        Product(
            id=product["id"],
            brand=product["brand"],
            model=product["model"],
            display_diagonal=product["display_diagonal"],
            display_resolution=product["display_resolution"],
            display_type=product["display_type"],
            chipset=product["chipset"],
            body_weight=product["body_weight"],
            battery_capacity=product["battery_capacity"],
            release_date=product["release_date"],
        )


def test_product_variants():
    for product_variant in product_variants:
        ProductVariant(
            id=product_variant["id"],
            ram_size=product_variant["ram_size"],
            storage_size=product_variant["storage_size"],
            product_id=product_variant["product_id"],
        )
        assert product_variant["product_id"] in [product["id"] for product in products]


def test_stores():
    for store in stores:
        Store(
            id=store["id"],
            name=store["name"],
            website=store["website"],
        )


def test_offers():
    for offer in offers:
        Offer(
            title=offer["title"],
            price=offer["price"],
            link=offer["link"],
            images=offer["images"],
            store_id=offer["store_id"],
            product_variant_id=offer["product_variant_id"],
        )
        assert offer["store_id"] in [store["id"] for store in stores]


test_products()
test_product_variants()
test_stores()
test_offers()
