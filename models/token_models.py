from pydantic import BaseModel


# atributos dos tokens
class Token(BaseModel):
    access_token: str
    token_type: str

