from abc import ABCMeta, abstractmethod
from config import config
import boto3

class Meta(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, table_name: str, partition_key: str, sort_key: None, 
                                                        cursor: None) -> None:
        self.table_name = table_name
        self.partition_key = partition_key
        self.sort_key = sort_key

        self.client = None
        if cursor is None:
            self.client = boto3.resource('dynamodb',
                aws_access_key_id=config.DYNAMODB_ACCESS_KEY_ID,
                aws_secret_access_key=config.DYNAMODB_SECRET_ACCESS_KEY,
                region_name=config.DYNAMODB_REGION_NAME)
        else: self.client = cursor
        print("DynamoDB connection established.")

    @abstractmethod
    def get(self, key) -> dict:
        pass

    @abstractmethod
    def put(self, item) -> None:
        pass

    @abstractmethod
    def scan(self, filter_expression=None,
                                expression_attribute_values=None) -> list:
        pass

    @abstractmethod
    def delete(self, key) -> None:
        pass

    @abstractmethod
    def update(self, key, update_expression,
                expression_attribute_values=None) -> None:
        pass

