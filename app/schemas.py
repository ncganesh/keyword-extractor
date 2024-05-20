from typing import List, Dict
from pydantic import BaseModel

class KeywordResponse(BaseModel):
    keywords: List[str]

class BatchKeywordResponse(BaseModel):
    results: List[Dict[str, List[str]]]
