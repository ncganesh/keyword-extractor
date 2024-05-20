from pydantic import BaseModel, conlist
from typing import List

class TextData(BaseModel):
    text: str
    num_keywords: int = 5  # Default number of keywords to extract

class BatchTextData(BaseModel):
    texts: conlist(str, min_items=1)  # A list of texts to process
    num_keywords: int = 5  # Default number of keywords to extract
