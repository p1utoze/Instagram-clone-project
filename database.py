import os
from dotenv import load_dotenv


def __getenv():
    load_dotenv(os.path.join(os.getcwd(), 'secrets', '.env'))


__getenv()
print(os.getenv('DATABASE_PASSWORD'))

