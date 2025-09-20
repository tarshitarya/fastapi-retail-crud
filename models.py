# from pydantic import BaseModel

# class Product(BaseModel):
#     id : int
#     name : str
#     description : str
#     price : float
#     quantity : int 

    # def __init__(self, id:int, name:str, description:str, price:float, quantity:int):
    #     self.id = id
    #     self.name = name
    #     self.description = description
    #     self.price = price
    #     self.quantity = quantity

from pydantic import BaseModel

# Shared fields
class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

# For requests (add/update) — no id
class ProductCreate(ProductBase):
    pass

# For responses — includes id
class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True  # Required for SQLAlchemy model-to-Pydantic conversion

