from typing import Union
import fastapi as fa
from database import __getenv

app = fa.FastAPI(title='Social_media_API')

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/posts/{post_id}")
def get_postid(post_id: int, q: Union[str, None]=None):
    connection_params = __getenv()