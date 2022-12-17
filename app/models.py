from dataclasses import dataclass
from datetime import datetime

@dataclass
class Tweet:
    text:str
    id:int = None
    created_at:datetime = datetime.now()