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

    def scan(self, filter_expression=None,
                                expression_attribute_values=None) -> list:
        table = self.client.Table(self.table_name)
        res = None
        if filter_expression is None: res = table.scan()
        else :
            res = table.scan(
                FilterExpression=filter_expression,
                ExpressionAttributeValues=expression_attribute_values
            )
        return res['Items']

    def delete(self, key: str) -> None:
        table = self.client.Table(self.table_name)
        table.delete_item(Key={self.partition_key: key})

    def update(self, key: str, target: str, values=None) -> None:
        table = self.client.Table(self.table_name)
        table.update_item(
            Key={self.partition_key: key},
            UpdateExpression=f"set {target} = :{target}",
            ExpressionAttributeValues={f":{target}": values}
        )

    def low_update(self, key: str, update_expression: str,
                    expression_attribute_values=None) -> None:
        table = self.client.Table(self.table_name)
        table.update_item(
            Key={self.partition_key: key},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
        )

