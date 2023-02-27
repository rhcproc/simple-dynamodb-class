
from dynamodb.base import dynamo_test as dynamo

if __name__ == '__main__':

    # put
    dynamo.put({'name': 'name01', 'amount': '1000'})

    # dynamo.put({'name': 'name03', 'amount': '3000'})
    data = dynamo.get('name01')
    print(data)

    # scan
    data = dynamo.scan()
    print(data)
    