
import boto3

def create_sns_topic(topic_name):
    sns = boto3.client('sns')
    response = sns.create_topic(Name=topic_name)
    topic_arn = response['TopicArn']
    print(f"SNS topic {topic_name} created with ARN: {topic_arn}")
    return topic_arn

def subscribe_to_sns_topic(topic_arn, protocol, endpoint):
    sns = boto3.client('sns')
    response = sns.subscribe(
        TopicArn=topic_arn,
        Protocol=protocol,
        Endpoint=endpoint
    )
    subscription_arn = response['SubscriptionArn']
    print(f"Subscribed to SNS topic {topic_arn} with subscription ARN: {subscription_arn}")

if __name__ == "__main__":
    topic_name = 'MySNSTopic'
    protocol = 'email'  # Change to 'sms' or 'lambda' as needed
    endpoint = 'your_email@example.com'  # Change to your email or phone number
    
    topic_arn = create_sns_topic(topic_name)
    subscribe_to_sns_topic(topic_arn, protocol, endpoint)

