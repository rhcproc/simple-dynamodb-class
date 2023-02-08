# simple-dynamodb-class

This is a simple class for dynamodb.

### Structure
- config.py is a configuration file for dynamodb.
- dynamodb/base.py is a class for dynamodb.
- main.py is a sample code.
- dynamodb/tests.py is a test code.

### Requirement
- python3.6
- boto3


### Installation & test
```bash
$ git clone https://github.com/rhcproc/simple-dynamodb-class
$ cd simple-dynamodb-class
$ pip install requirements.txt
$ python -m unittest 
```

### Usage
```python

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
```

### License
MIT

### Author
rhcproc (rhcproc@gmail.com)

### Reference
- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.html

