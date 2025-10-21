from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud.crud_url import create_db_url, get_db_url_by_code
from app.db.session import get_db, engine
from app.models.url import Base
from app.schema.url import URL, URLBase

Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.post("/shorten", response_model=URL, status_code=status.HTTP_201_CREATED)
def create_url(url: URLBase, db: Session = Depends(get_db)):
    """Creates a new shurl"""
    db_url = create_db_url(db=db, url=url)
    return db_url


@router.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    """Redirects to the original URL"""
    db_url = get_db_url_by_code(db=db, short_code=short_code)
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")
    if "http" not in db_url.target_url and "https" not in db_url.target_url:
        db_url.target_url = "https://" + db_url.target_url
    return RedirectResponse(url=db_url.target_url)

