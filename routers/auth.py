import time
import datetime
from typing import Dict

import jwt

from settings import Settings

settings = Settings()

JWT_SECRET = settings.SECRET
JWT_ALGORITHM = settings.ALGORITHM

