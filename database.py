import os
from dotenv import load_dotenv
import mariadb
from random import sample
import time
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
async def get_connected():
    conn = __get_connect()
    db = conn.cursor()
    return db


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


conn = __get_connect()
# print(conn.user)


# db = conn.cursor()
# query = '''select user_id, email, username, bio, profile_photo_url
# from users
# where user_id in (select follower_id from follows where followee_id  = 15);'''
# # id = 4
# # query2 = f'''select photo_id, video_id, user_id, caption, location from post where post_id={id}'''
# try:
    # db.execute(query)
    # results = db.fetchall()
    # d = {}
    # keys = ("user_id", "email", "username", "bio", "profile_photo_url")
    # samples = sample(range(1, results.__len__() + 1), k=10)
    # for k, *v in zip(keys, zip(*[results[i] for i in samples])):
    #     d[k] = v[0]
    # print(d)
   #  for i in results:
   #      print(*i)
   # Commit your changes in the database
   #  conn.commit()
# except:
#    # Rollback in case there is any error
#    #  conn.rollback()
#     print('Error')
# conn.close()
# with engine.connect() as db:
#     res = db.execute(query)
#     for i in res.all():
#         print(i)
# start = time.time()
# d = {k: v for k, v in zip(range(10000), range(30000, 40001))}
# print(time.time() - start)
#
# start = time.time()
# d = {}
# for k, v in zip(range(10000), range(30000, 40001)):
#     d[k] = v
# print(time.time() - start)
