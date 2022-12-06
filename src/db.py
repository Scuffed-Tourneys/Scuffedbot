from typing import Any, Dict
from pymongo import MongoClient
from pymongo.database import Database
from os import getenv

class db():
	def __init__(self) -> None:
		self.client: Database = self.get_database()
		return
	
	def get_database(self) -> Database:
		CONNECTION_STRING: str = f"mongodb://{getenv('MONGO_USR')}:{getenv('MONGO_PWD')}@localhost:27017/?authMechanism=DEFAULT"
		client: MongoClient = MongoClient(CONNECTION_STRING)
		return client['scuffedbot']
	
	def test_connection(self) -> Dict[str, Any]:
		return self.client.server_info()

database: db = db()