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
    conn = mariadb.connect(**connect_params)
    return conn


# conn = __get_connect()
# # print(connect_params.values())
#
#
# db = conn.cursor()
# query = '''select p.location, count(*) as total_posts
# from post p
# # where location in ('karnataka')
# group by p.location
# having total_posts >=4
# order by total_posts desc;'''
# id = 4
# query2 = f'''select photo_id, video_id, user_id, caption, location from post where post_id={id}'''
# try:
#     db.execute(query2)
#     results = db.fetchone()
#     print(*results)
#     # for i in results:
#     #     print(*i)
#    # Commit your changes in the database
#     conn.commit()
# except:
#    # Rollback in case there is any error
#     conn.rollback()
#     print('Error')
# conn.close()
