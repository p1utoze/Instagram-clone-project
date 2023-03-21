from typing import Union
import fastapi as fa
from database import __get_connect

app = fa.FastAPI(title='Social_media_API')
conn = __get_connect()
db = conn.cursor()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/posts/{post_id}")
async def get_postid(post_id: int, q: Union[str, None]=None):

    query = f'''select photo_id, video_id, user_id, caption, location from post where post_id={post_id}'''
    db.execute(query)
    res = db.fetchone()
    return dict(zip(('photo_id', 'video_id', 'user_id', 'caption', 'location'), res))


@app.get("/users/")
async def valid_user(user_id: int):
    db.execute(f'''select EXISTS (select user_id from users WHERE user_id={user_id}) as user_exists;''')
    user_exits = db.fetchone()
    return {'user_exists': bool(user_exits)}
