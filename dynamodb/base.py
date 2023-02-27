from dynamodb import Meta

class DynamoDB(Meta):
    def __init__(self, table_name: str, partition_key: str, sort_key: None, 
                                                        cursor: None) -> None:
        super().__init__(table_name, partition_key, sort_key, cursor)
        
        
    def get(self, key: str) -> dict:
        table = self.client.Table(self.table_name)
        res = table.get_item(Key={self.partition_key: key})
        return res['Item']
        
    def put(self, item: dict) -> None:
        table = self.client.Table(self.table_name)
        table.put_item(Item=item)

    def scan(self, **kwargs) -> list:
        table = self.client.Table(self.table_name)
        res = None
        if kwargs.get('filter_expression') is None:
            res = table.scan()
        else :
            res = table.scan(
                FilterExpression=kwargs.get('filter_expression'),
                ExpressionAttributeValues=kwargs.get('expression_attribute_values')
            )
        return res['Items']

    def delete(self, key: str) -> None:
        table = self.client.Table(self.table_name)
        table.delete_item(Key={self.partition_key: key})

    def update(self, **kwargs) -> None:
        table = self.client.Table(self.table_name)
        table.update_item(
            Key={self.partition_key: kwargs.get('key')},
            UpdateExpression=f"set {kwargs.get('target')} = :{kwargs.get('target')}",
            ExpressionAttributeValues={f":{kwargs.get('target')}":kwargs.get('values')}
        )

    def low_update(self, **kwargs) -> None:
        table = self.client.Table(self.table_name)
        table.update_item(
            Key={self.partition_key: kwargs.get('key')},
            UpdateExpression=kwargs.get('update_expression'),
            ExpressionAttributeValues=kwargs.get('expression_attribute_values')
        )

dynamo_test = DynamoDB('test', 'name', None, cursor=None)

