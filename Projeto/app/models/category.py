from pydantic import BaseModel
from typing import Optional

class Category(BaseModel):
    nome: str
    category_id: int
    category_products: Optional[list] = None