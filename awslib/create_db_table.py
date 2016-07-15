import boto3

client = boto3.resource('dynamodb', region_name='us-east-1')


table = client.create_table(
    TableName='dateapp',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'dob',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'dob',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)


# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='dateapp')

# Print out some data about the table.
print(table.item_count)