from pydantic import BaseModel


class DBConnect(BaseModel):
    Host: str = 'dpg-csjn03m8ii6s73d6048g-a.oregon-postgres.render.com'
    Port: str = 'Обычно это 5432'
    Maintenance: str = 'postgres_db_yd4o'
    Username: str = 'postgres_user'
    Password: str = '(например, pWUfrJ3QzD52cp7CvvxrKhmMdr9jNK2m)'


# db:
#   image: postgres:15
#   environment:
#     POSTGRES_USER: postgres_user
#     POSTGRES_PASSWORD: postgres_password
#     POSTGRES_DB: postgres_db
#   volumes:
#     - postgres_data:/var/lib/postgresql/data/

"""
Host: Введите хост вашей базы данных из URL (например, dpg-csjn03m8ii6s73d6048g-a.oregon-postgres.render.com).
Port: Обычно это 5432 (стандартный порт для PostgreSQL).
Maintenance database: Введите имя вашей базы данных (например, postgres_db_yd4o).
Username: Введите имя пользователя базы данных (например, postgres_user).
Password: Введите пароль (например, pWUfrJ3QzD52cp7CvvxrKhmMdr9jNK2m).
"""
