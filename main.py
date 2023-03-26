from typing import Union
import fastapi as fa
from database import get_connected
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
async def valid_user(user_id: int = -1, email: str = "XYZ"):
    db = await get_connected()
    # return {'email': email}
    if user_id and user_id != -1:
        db.execute(f'''SELECT user_id, username,
                    IF(EXISTS(SELECT 1 FROM users WHERE user_id = 12), 'true', 'false') as user_exists
                    FROM users
                    WHERE user_id = 12;''')
        user_exits = db.fetchone()
        db.close()
        return {'user_exists': bool(user_exits)}
    elif isinstance(email, str):
        try:
            db.execute(f'''select DISTINCT email, username, bio, profile_photo_url 
                            from  users where email='{email}' group by email;''')
            user_profile = db.fetchone()
            res = dict(zip(("email", "username", "bio", "profile_photo_url" ), user_profile))
            res['user'] = True
            db.close()
            return res
        except:
            db.close()
            return {'user': False}
    db.close()
    return "Invalid query!"

