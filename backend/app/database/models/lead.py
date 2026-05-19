from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID

import uuid

from app.database.base import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    company_name = Column(String)

    website = Column(String)

    email = Column(String)

    phone = Column(String)

    industry = Column(String)

    score = Column(Integer, default=0)

    status = Column(String, default="new")