from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import ColumnExpressionArgument
from app.db.session import Base


class URL(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True, index=True)
    target_url = Column(String, index=True, nullable=False)
    short_code = Column(String, index=True, nullable=False)
