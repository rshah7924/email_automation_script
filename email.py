import boto3
import io
import csv
import pandas as pd

s3 = boto3.client(service_name = 's3', region_name = '', aws_access_key_id = '', aws_secret_access_key = '')
ses = boto3.client(service_name = 'ses', region_name = '', aws_access_key_id = '', aws_secret_access_key = '')

ses.verify_email_address(
EmailAddress = ''
)

obj = s3.get_object(Bucket='',Key='')
data = pd.read_csv(io.BytesIO(obj['Body'].read()), usecols=['Email Address'])
email_addresses = data['Email Address'].values.tolist()
for i in range(len(email_addresses)):
    email = email_addresses[i]
    ses.send_email(
Source = '',
    Destination = {
        'ToAddresses': [email],
        'CcAddresses': [email]
    },
    ReplyToAddresses = [email],
    
    Message = {
        'Subject': {
            'Data': 'For My Investors',
            'Charset': 'utf-8'
        },
        'Body': {
            'Text': {
                'Data': 'This is your body message',
                'Charset': 'utf-8'
            },
            'Html': {
                'Data': """""",
                'Charset': 'utf-8'
            }
        }
    }
)
    i+=1