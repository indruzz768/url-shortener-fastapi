from typing import List
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from ..database import get_db
from .. import crud, schemas

router = APIRouter()

@router.post("/", response_model=schemas.URLItem, status_code=201)
def create_short(payload: schemas.URLCreate, db: Session = Depends(get_db)):
    return crud.create_short_url(db, payload)

@router.get("/", response_model=List[schemas.URLItem])
def list_urls(db: Session = Depends(get_db)):
    return crud.list_recent(db)

@router.get("/{code}")
def resolve(code: str, db: Session = Depends(get_db)):
    obj = crud.get_by_code(db, code)
    if not obj:
        raise HTTPException(status_code=404, detail="Short code not found")
    crud.increment_click(db, obj)
    return RedirectResponse(obj.original_url, status_code=307)
