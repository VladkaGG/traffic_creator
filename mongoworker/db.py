from pymongo.errors import ServerSelectionTimeoutError
from motor.motor_asyncio import AsyncIOMotorClient
from urllib.parse import urlparse
from typing import Iterable
import logging
logger = logging.getLogger(__name__)


class Connection:
    connection = None

    def __init__(self, uri: str):
        uri_parse = urlparse(uri)
        scheme = uri_parse.scheme
        if 'mongodb' not in scheme:
            raise ValueError(f'Wrong URI with unexpected scheme - {uri}')
        self.user = uri_parse.username
        self.password = uri_parse.password
        self.host = uri_parse.hostname or 'localhost'
        self.port = uri_parse.port or 27017
        self.database = uri_parse.path[1:] or 'default'

    def __enter__(self):
        if self.connection is None:
            uri = 'mongodb://'
            if self.user and self.password:
                uri += f'{self.user}:{self.password}@{self.host}:{self.port}'
            else:
                uri += f'{self.host}:{self.port}'
            self.connection = AsyncIOMotorClient(uri, serverSelectionTimeoutMS=5000)
            try:
                self.connection.server_info()
            except ServerSelectionTimeoutError:
                logger.warning(f'Cannot connect to mongodb with this URI: {uri}')
                raise
        return self.connection[self.database]

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
        if exc_type:
            raise exc_type(exc_val, exc_tb)

    def __del__(self):
        if self.connection:
            self.connection.close()

    def __getitem__(self, item):
        return self.connection.__getitem__(item)


class Model:
    __connection = None

    def __init__(self, uri: str, collection: str = None):
        self._uri = uri
        self.collection = collection or self.__class__.__name__

    def connect(self):
        if self.__connection is None:
            self.__connection = Connection(self._uri)
        return self.__connection

    async def insert_one(self, data):
        if data:
            with self.connect() as database:
                collection = database[self.collection]
                result = await collection.insert_one(data)
            return result.inserted_id

    async def insert_many(self, data: Iterable):
        if data:
            with self.connect() as database:
                collection = database[self.collection]
                result = await collection.insert_many(data)
            return len(result.inserted_ids)

    async def find_one(self, query):
        with self.connect() as database:
            collection = database[self.collection]
            document = await collection.find_one(query)
        return document

    async def find(self, query):
        with self.connect() as database:
            collection = database[self.collection]
            cursor = await collection.find(query)
        result = await cursor.to_list()
        return result

    async def update(self, query, data):
        with self.connect() as database:
            collection = database[self.collection]
            result = collection.update_many(query, data)
        return result.modified_count

    async def delete(self, query, data):
        with self.connect() as database:
            collection = database[self.collection]
            result = collection.delete_many(query, data)
        return result.deleted_count
