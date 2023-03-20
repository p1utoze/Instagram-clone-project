import os
from dotenv import load_dotenv
import mariadb
def __getenv():
    load_dotenv(os.path.join(os.getcwd(), 'secrets', '.env'))
    return {'user': os.getenv('DATABASE_USER'),
     'password': os.getenv('DATABASE_PASSWORD'),
     'database': os.getenv('DATABASE'),
     'port': 3306,
     'host': os.getenv('DATABASE_HOST')
     }


connect_params = __getenv()
print(connect_params.values())

conn = mariadb.connect(**connect_params)

cur = conn.cursor()
query = '''select p.location, count(*) as total_posts
from post p
# where location in ('karnataka')
group by p.location
having total_posts >=4
order by total_posts desc;'''

cur.execute(query)
results = cur.fetchall()
for i in results:
    print(*i)
