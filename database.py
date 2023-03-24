import os
from dotenv import load_dotenv
import mariadb
# from sqlalchemy import create_engine, URL
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# url_obj = URL.create('mariadb',
#                      username=os.getenv('DATABASE_USER'),
#                      host=os.getenv('DATABASE_HOST'),
#                      password=os.getenv('DATABASE_PASSWORD'),
#                      port=3306,
#                      database=os.getenv('DATABASE'))
# engine = create_engine(url_obj)
# Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# db = Session.begin()


def __get_connect():
    load_dotenv(os.path.join(os.getcwd(), 'secrets', '.env'))
    connect_params = {'user': os.getenv('DATABASE_USER'),
     'password': os.getenv('DATABASE_PASSWORD'),
     'database': os.getenv('DATABASE'),
     'port': 3306,
     'host': os.getenv('DATABASE_HOST')
     }
    skysql_params = {'host': "dbpgf03059429.sysp0000.db.skysql.net",
                     'user': "dbpgf03059429",
                     'password': os.getenv('SKYSQL_PASSWORD'),
                     'port': 3306,
                     'ssl_ca': 'secrets/skysql_chain_2022.pem',
                     'database': 'social_media'}
    conn = mariadb.connect(**connect_params)
    return conn


# conn = __get_connect()
# print(conn.user)


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
#    #  conn.commit()
# except:
#    # Rollback in case there is any error
#    #  conn.rollback()
#     print('Error')
# conn.close()
# with engine.connect() as db:
#     res = db.execute(query)
#     for i in res.all():
#         print(i)