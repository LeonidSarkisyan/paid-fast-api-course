import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_USER = os.environ.get('DB_USER')
    DB_PASS = os.environ.get('DB_PASS')
    DB_NAME = os.environ.get('DB_NAME')

    @property
    def get_database_url(self):
        return (f'postgresql+asyncpg://{self.DB_USER}:'
                f'{self.DB_PASS}@{self.DB_HOST}:'
                f'{self.DB_PORT}/{self.DB_NAME}')


settings = Settings()
