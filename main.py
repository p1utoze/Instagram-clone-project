from typing import Union
import fastapi as fa
from database import __get_connect

app = fa.FastAPI(title='Social_media_API')
conn = __get_connect()
db = conn.cursor()


@app.get("/posts/{post_id}")
async def get_postid(post_id: int, q: Union[str, None]=None):

    query = f'''select photo_id, video_id, user_id, caption, location from post where post_id={post_id}'''
    db.execute(query)
    res = db.fetchone()
    return dict(zip(('photo_id', 'video_id', 'user_id', 'caption', 'location'), res))


@app.get("/users")
async def valid_user(user_id: int = -1, email: str = "XYZ"):
    if user_id and user_id != -1:
        db.execute(f'''SELECT user_id, username,
                    IF(EXISTS(SELECT 1 FROM users WHERE user_id = 12), 'true', 'false') as user_exists
                    FROM users
                    WHERE user_id = 12;''')
        user_exits = db.fetchone()
        return {'user_exists': bool(user_exits)}
    elif email:
        db.execute(f'''select DISTINCT email, username, bio, profile_photo_url 
                        from  users where email='{email}' group by email;''')
        user_profile = db.fetchall()
        return user_profile
    return "Invalid query!"
