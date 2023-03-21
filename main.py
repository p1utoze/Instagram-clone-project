from typing import Union
import fastapi as fa
from database import __get_connect

app = fa.FastAPI(title='Social_media_API')

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/posts/{post_id}")
async def get_postid(post_id: int, q: Union[str, None]=None):
    conn = __get_connect()
    db = conn.cursor()
    query = f'''select photo_id, video_id, user_id, caption, location from post where post_id={post_id}'''
    db.execute(query)
    res = db.fetchone()
    return dict(zip(('photo_id', 'video_id', 'user_id', 'caption', 'location'), res))
