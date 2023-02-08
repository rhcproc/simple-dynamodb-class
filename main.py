
from dynamodb.base import DynamoDB

if __name__ == '__main__':
    dynamo = DynamoDB('test', 'name', None, cursor=None)
    # put
    dynamo.put({'name': 'name03', 'amount': '3000'})
    data = dynamo.get('name01')
    print(data)

    # scan
    data = dynamo.scan()
    print(data)
    