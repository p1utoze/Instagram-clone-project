from typing import Union
import fastapi as fa
from database import get_connected
from random import sample, randint
from fastapi.middleware.cors import CORSMiddleware
app = fa.FastAPI(title='Social_media_API')
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://127.0.0.1:5500'], # Set this to a list of allowed origins, e.g. ['http://localhost', 'https://example.com']
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'], # Set this to a list of allowed HTTP methods, e.g. ['GET', 'POST', 'PUT', 'DELETE']
    allow_headers=['Content-Type', 'Authorization'], # Set this to a list of allowed HTTP headers, e.g. ['Content-Type', 'Authorization']
)




@app.get("/posts/{post_id}")
async def get_postid(post_id: int, q: Union[str, None]=None):
    db = await get_connected()
    query = f'''select photo_id, video_id, user_id, caption, location from post where post_id={post_id}'''
    db.execute(query)
    res = db.fetchone()
    db.close()
    return dict(zip(('photo_id', 'video_id', 'user_id', 'caption', 'location'), res))


@app.get("/users")
async def valid_user(user_bool: int = 0, name: str = "XYZ"):
    db = await get_connected()
    # return {'email': email}
    if user_bool and name:
        db.execute(f'''SELECT user_id, username,
                    IF(EXISTS(SELECT 1 FROM users WHERE username='{name.lower()}'), 'true', 'false') as user_exists
                    FROM users
                    WHERE username='{name.lower()}';''')
        user_exits = db.fetchone()
        db.close()
        return dict(zip(("user_id", "username", "exists" ), user_exits))
    elif isinstance(name, str):
        try:
            db.execute(f'''select DISTINCT user_id, email, username, bio, profile_photo_url 
                            from  users where username='{name.lower()}' group by email;''')
            user_profile = db.fetchone()
            res = dict(zip(("user_id", "email", "username", "bio", "profile_photo_url" ), user_profile))
            res['user'] = True
            db.close()
            return res
        except:
            db.close()
            return {'user': False}
    db.close()
    return "Invalid query!"

@app.get("/followers/{user_id}")
async def followers_transact(user_id: int, self: int = 0, suggestion: bool = False ):
    db = await get_connected()
    keys = ("user_id", "email", "username", "bio", "profile_photo_url")
    if self:
        try:
            db.execute(f'''select  user_id, email, username, bio, profile_photo_url from users where user_id={user_id}''')
            user_data = db.fetchone()
            return dict(zip(keys, user_data))
        except:
            return "Internal server Error"
    elif suggestion:
        try:
            db.execute(f'''select user_id, username, bio from users where user_id not in (select distinct follower_id from follows where followee_id={user_id})''')
            suggest = db.fetchall()
            samples = sample(suggest, k=1)[0]
            return dict(zip(("user_id", "username", "bio"), samples))
        except:
            return "Internal server Error"
    try:
        db.execute(f'''select  email, username, bio, profile_photo_url from users where user_id={user_id}''')
        user_data = db.fetchone()
        db.execute(f'''select user_id, email, username, bio, profile_photo_url from users 
        where user_id in (select follower_id from follows where followee_id={user_id}) and profile_photo_url like 'http%';''')
        resp = db.fetchall()
        response = {}
        samples = sample(range(1, resp.__len__()), k=10)
        for k, *v in zip(keys, zip(*[resp[i] for i in samples])):
            response[k] = v[0]
        return response
    except:
        return 'Internal server error'


