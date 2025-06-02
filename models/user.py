from sqlalchemy import Table, Column, Integer, String, MetaData
from database import metadata


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), unique=True, nullable=False),  
    Column("password", String(255), nullable=False),              
    Column("place", String(100), nullable=False),                 
    Column("age", Integer, nullable=False)
)
