from fastapi import FastAPI
from instagram.insta_phish_api import router as insta_router
# from contextlib import asynccontextmanager
# import user_interface

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     style()  # Run the animation at application startup
#     menu()
#     yield

# app = FastAPI(lifespan=lifespan)

app.include_router(insta_router)

