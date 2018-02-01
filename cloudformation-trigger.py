def lambda_handler(event, context):
    # TODO implement
    import boto3
    print 'start execution'
    cf_client = boto3.client('cloudformation')
    cf_client.create_stack(
    StackName='VPC-30',
    please remove this line------
    
    TemplateURL='https://s3.amazonaws.com/cloudformation-template-lambda-bucket/vpc.yaml'
    )
