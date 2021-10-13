import csv
from datetime import date

from pydantic import BaseModel, HttpUrl, confloat, conint, constr


class Mobile(BaseModel):
    id: constr(regex=r'[a-z0-9-+]+')
    brand: constr(regex=r'(Apple|Huawei|Infinix|Oppo|Samsung|Xiaomi)')
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


class Product(BaseModel):
    title: str
    price: conint(gt=0, lt=32000)
    link: HttpUrl
    images: HttpUrl


def test_products():
    with open("data/products.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        products = list(reader)
    for product in products:
        Product(
            title=product["title"],
            price=product["price"],
            link=product["link"],
            images=product["images"],
        )


def test_mobiles():
    with open("data/mobiles.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        mobiles = list(reader)
    for mobile in mobiles:
        Mobile(
            id=mobile["id"],
            brand=mobile["brand"],
            model=mobile["model"],
            ram_size=mobile["ram_size"],
            storage_size=mobile["storage_size"],
            display_diagonal=mobile["display_diagonal"],
            display_resolution=mobile["display_resolution"],
            display_type=mobile["display_type"],
            chipset=mobile["chipset"],
            body_weight=mobile["body_weight"],
            battery_capacity=mobile["battery_capacity"],
            release_date=mobile["release_date"],
        )


test_products()
test_mobiles()
