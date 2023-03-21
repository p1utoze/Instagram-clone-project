import os
from dotenv import load_dotenv
import mariadb


def __get_connect():
    load_dotenv(os.path.join(os.getcwd(), 'secrets', '.env'))
    connect_params = {'user': os.getenv('DATABASE_USER'),
     'password': os.getenv('DATABASE_PASSWORD'),
     'database': os.getenv('DATABASE'),
     'port': 3306,
     'host': os.getenv('DATABASE_HOST')
     }
    return mariadb.connect(**connect_params)


# connect_params = __getenv()
# print(connect_params.values())

# conn = mariadb.connect(**connect_params)

# db = conn.cursor()
query = '''select p.location, count(*) as total_posts
from post p
# where location in ('karnataka')
group by p.location
having total_posts >=4
order by total_posts desc;'''
# try:
#
#     db.execute(query)
#     results = db.fetchall()
#     for i in results:
#         print(*i)
#    # Commit your changes in the database
#     db.commit()
# except:
#    # Rollback in case there is any error
#     db.rollback()
#
# db.close()
