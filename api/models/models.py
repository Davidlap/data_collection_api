from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    Table,
    Date,
    Numeric,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Category(Base):

    __tablename__ = "categories"

    id = Column(String, primary_key=True)
    name = Column(String)
    items = relationship("Item")

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name}"


class Item(Base):

    __tablename__ = "items"

    id = Column(String, primary_key=True)
    name = Column(String)
    category_id = Column(String, ForeignKey("categories.id"))

    def __repr__(self):
        return f"<Item(id={self.id}, name={self.name}, category_id={self.category_id}"


class Location(Base):

    __tablename__ = "locations"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    country_name = Column(String)
    pmt_id = Column(String)
    jics_id = Column(String)
    stores = relationship("Store")

    def __repr__(self):
        return f"<Location(name={self.name}, country_name={self.country_name}, pmt_id={self.pmt_id}, jics_id={self.jics_id}"


class Store(Base):

    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    zipcode = Column(String)
    outlet_type = Column(String)
    location_id = Column(Integer, ForeignKey("locations.id"))

    def __repr__(self):
        return f"<Store(name={self.name}, zipcode={self.zipcode}, outlet_type={self.outlet_type}, location_id={self.location_id}"


class Url(Base):

    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    url = Column(String)
    item_id = Column(Integer, ForeignKey("items.id"))
    store_id = Column(Integer, ForeignKey("stores.id"))

    def __repr__(self):
        return f"<Url(url={self.url}, item_id={self.item_id}, store_id={self.store_id}"


class ProductPrice(Base):

    __tablename__ = "product_prices"

    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey("stores.id"))
    title = Column(String)
    price = Column(Numeric)
    quantity = Column(Numeric)
    unit = Column(String)
    price_unit = Column(String)
    img_url = Column(String)
    date_collected = Column(Date)

    def __repr__(self):
        return f"<ProductPrice(title={self.title}, price={self.price}, quantity={self.quantity}, unit={self.unit}, price_unit={self.price_unit}, img_url={self.img_url}, img_url={self.date_collected}"