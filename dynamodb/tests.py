
from dynamodb.base import DynamoDB
import unittest
import moto
import boto3

@moto.mock_dynamodb
class TestDynamoDB(unittest.TestCase):
    def setUp(self):
        dynamodb = boto3.resource('dynamodb', 'us-east-1')
        dynamodb.create_table(
            TableName='test',
            KeySchema=[
                {
                    'AttributeName': 'name',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'name',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        self.dynamo = DynamoDB('test', 'name', None, dynamodb)
        self.dynamo.put({'name': 'name01', 'amount': 1000})
        self.dynamo.put({'name': 'name02', 'amount': 2000})
        self.dynamo.put({'name': 'name03', 'amount': 3000})

    def test_get(self):
        self.assertEqual(self.dynamo.get('name01'), {'name': 'name01', 'amount': 1000})

    def test_put(self):
        self.dynamo.put({'name': 'name04', 'amount': '4000'})
        self.assertEqual(self.dynamo.get('name04'), {'name': 'name04', 'amount': '4000'})
    
    def test_scan(self):
        self.assertEqual(self.dynamo.scan(), [{'name': 'name01', 'amount': 1000}, 
                                              {'name': 'name02', 'amount': 2000}, 
                                              {'name': 'name03', 'amount': 3000}])

    def test_scan_filter(self):
        self.assertEqual(self.dynamo.scan(filter_expression='amount >= :amount',
                                          expression_attribute_values={':amount': 3000}), 
                                          [{'name': 'name03', 'amount': 3000}])

    def test_delete(self):
        self.dynamo.delete('name03')
        self.assertEqual(self.dynamo.scan(), [{'name': 'name01', 'amount': 1000}, 
                                              {'name': 'name02', 'amount': 2000}])

    def test_update(self):
        self.dynamo.update('name01', 'amount', 1313)
        self.assertEqual(self.dynamo.get('name01'), {'name': 'name01', 'amount': 1313})

    def test_low_update(self):
        self.dynamo.low_update('name01', 'set amount = :amount',
                                expression_attribute_values={':amount': 23})
        self.assertEqual(self.dynamo.get('name01'), {'name': 'name01', 'amount': 23})

if __name__ == '__main__':
    unittest.main()
