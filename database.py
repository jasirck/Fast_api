from databases import Database
from sqlalchemy import MetaData
from sqlalchemy import create_engine

DATABASE_URL = "mysql+aiomysql://root:1234@localhost:3306/test_auth"

database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine("mysql+pymysql://root:1234@localhost:3306/test_auth")
