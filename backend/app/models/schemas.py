from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.database import Base
import uuid

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="standard")
    is_approved = Column(Boolean, default=False)

class Summary(Base):
    __tablename__ = "summaries"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    model = Column(String, nullable=False)
    original_filename = Column(String)
    summary_text = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class ModelAccessRequest(Base):
    __tablename__ = "model_access_requests"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    model = Column(String, nullable=False)
    status = Column(String, default="pending")
    requested_at = Column(DateTime(timezone=True), server_default=func.now())
