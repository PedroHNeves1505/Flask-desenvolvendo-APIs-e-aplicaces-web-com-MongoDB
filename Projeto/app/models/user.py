from pydantic import BaseModel

class LoginPlayLoad(BaseModel):
    username: str
    password: str