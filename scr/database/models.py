from pydantic import BaseModel


class DBConnect(BaseModel):
    name: str = 'db'
    user_name: str = 'postgres_user'
    password: str = 'postgres_password'
    db_name: str = 'postgres_db'
# db:
#   image: postgres:15
#   environment:
#     POSTGRES_USER: postgres_user
#     POSTGRES_PASSWORD: postgres_password
#     POSTGRES_DB: postgres_db
#   volumes:
#     - postgres_data:/var/lib/postgresql/data/
