from fastapi import APIRouter, HTTPException
from app.models import TextData, BatchTextData
from app.schemas import KeywordResponse, BatchKeywordResponse
from keybert import KeyBERT
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

# Initialize KeyBERT model once
kw_model = KeyBERT()

@router.post("/extract_keywords/", response_model=KeywordResponse)
async def extract_keywords(data: TextData):
    try:
        keywords = kw_model.extract_keywords(data.text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=data.num_keywords)
        keywords = [kw[0] for kw in keywords]  # Extract only the keyword strings
        return {"keywords": keywords}
    except Exception as e:
        logger.error(f"Error extracting keywords: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/extract_keywords_batch/", response_model=BatchKeywordResponse)
async def extract_keywords_batch(data: BatchTextData):
    try:
        results = []
        for text in data.texts:
            keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=data.num_keywords)
            keywords = [kw[0] for kw in keywords]  # Extract only the keyword strings
            results.append({"text": text, "keywords": keywords})
        return {"results": results}
    except Exception as e:
        logger.error(f"Error extracting keywords in batch: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
