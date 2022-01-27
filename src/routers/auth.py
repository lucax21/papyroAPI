from fastapi import APIRouter
from sqlalchemy.orm import Session
from src.infra.providers import hash_provider

router = APIRouter()


