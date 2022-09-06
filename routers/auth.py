import time
import datetime
from typing import Dict

import jwt
from passlib.context import CryptContext

from settings import Settings

settings = Settings()

JWT_SECRET = settings.SECRET
JWT_ALGORITHM = settings.ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")