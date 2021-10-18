import boto3
import csv

s3 = boto3.resource('s3',
    aws_access_key_id='my_access_key_id',
    aws_secret_access_key='my_secret_access_key'
)

# create bucket
print("create bucket")
try:
    s3.create_bucket(Bucket='yiqiu-hw3-bucket', CreateBucketConfiguration={
    'LocationConstraint': 'us-west-2'})
except Exception as e:
    print (e)

# make bucket publicly available
print("make bucket publicly available")
bucket = s3.Bucket("yiqiu-hw3-bucket")
bucket.Acl().put(ACL='public-read')

# upload a file into the bucket
s3.Object('yiqiu-hw3-bucket', 'experiments.csv').put(Body=open('./experiments.csv', 'rb'))
output = s3.Object('yiqiu-hw3-bucket', 'experiments.csv').Acl().put(ACL='public-read')
print(output)
s3.Object('yiqiu-hw3-bucket', 'exp1.csv').put(Body=open('./exp1.csv', 'rb'))
output = s3.Object('yiqiu-hw3-bucket', 'exp1.csv').Acl().put(ACL='public-read')
print(output)
s3.Object('yiqiu-hw3-bucket', 'exp2.csv').put(Body=open('./exp2.csv', 'rb'))
output = s3.Object('yiqiu-hw3-bucket', 'exp2.csv').Acl().put(ACL='public-read')
print(output)
s3.Object('yiqiu-hw3-bucket', 'exp3.csv').put(Body=open('./exp3.csv', 'rb'))
output = s3.Object('yiqiu-hw3-bucket', 'exp3.csv').Acl().put(ACL='public-read')
print(output)

# create the DynamoDB table
dyndb = boto3.resource('dynamodb',
    region_name='us-west-2',
    aws_access_key_id='my_access_key_id',
    aws_secret_access_key='my_secret_access_key'
)

try:
    table = dyndb.create_table(
    TableName='DataTable',
    KeySchema=[
        {
            'AttributeName': 'PartitionKey',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'RowKey',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'PartitionKey',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'RowKey',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
except Exception as e:
    print (e)

# Read the metadata from a CSV file, Move the data objects into 
# the blob store, and Enter the metadata row into the table
urlbase = "https://s3-us-west-2.amazonaws.com/yiqiu-hw3-bucket/"
table = dyndb.Table("DataTable")
with open('./experiments.csv', 'r') as csvfile:
    csvf = csv.reader(csvfile, delimiter=',', quotechar='|', )
    next(csvf)
    for item in csvf:
        print(item)
        body = open('./' + item[4], 'rb')
        s3.Object('yiqiu-hw3-bucket', item[4]).put(Body=body )
        md = s3.Object('yiqiu-hw3-bucket', item[4]).Acl().put(ACL='public-read')

        url = " https://s3-us-west-2.amazonaws.com/yiqiu-hw3-bucket/" + item[4]
        metadata_item = {'PartitionKey': item[4], 'RowKey': item[0],
        'Temp' : item[1], 'Conductivity' : item[2], 'Concentration':item[3], 'url':url}
        try:
            table.put_item(Item=metadata_item)
        except:
            print ("item may already be there or another failure")