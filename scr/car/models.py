from pydantic import BaseModel


class Decode(BaseModel):
    id: int = 5050
    username: str = 'Karl'
    login: str
    password: str
    email: str = 'Пока-что не нужно'
