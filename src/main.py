from fastapi import FastAPI
from entrypoints.routes import *

# origins = [
#     "http://localhost:3000",
#     "http://ip:port",
#     os.getenv("FRONTEND_API_HOST")
# ]

# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app = FastAPI()

# app.include_router()