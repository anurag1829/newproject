import boto3

def create_cloudwatch_alarm(alarm_name, metric_name, namespace, threshold, comparison_operator, evaluation_periods, sns_topic_arn):
    cloudwatch = boto3.client('cloudwatch')
    
    response = cloudwatch.put_metric_alarm(
        AlarmName=alarm_name,
        MetricName=metric_name,
        Namespace=namespace,
        Threshold=threshold,
        ComparisonOperator=comparison_operator,
        EvaluationPeriods=evaluation_periods,
        AlarmActions=[sns_topic_arn],
        Statistic='Average',
        Period=300
    )
    print(f"CloudWatch alarm {alarm_name} created")

if __name__ == "__main__":
    alarm_name = 'JobFailureAlarm'
    metric_name = 'Errors'
    namespace = 'AWS/Logs'
    threshold = 1
    comparison_operator = 'GreaterThanOrEqualToThreshold'
    evaluation_periods = 1
    sns_topic_arn = 'arn:aws:sns:us-east-1:123456789012:MySNSTopic'
    
    create_cloudwatch_alarm(alarm_name, metric_name, namespace, threshold, comparison_operator, evaluation_periods, sns_topic_arn)

