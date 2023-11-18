import aws_cdk as cdk
from aws_cdk import aws_cloudfront as cloudfront
from aws_cdk import aws_cloudfront_origins as origins
from aws_cdk import aws_s3 as s3

app = cdk.App()
stack = cdk.Stack(app, "cdk-url-redirect-stack")

# バケットを作成する
bucket = s3.Bucket(
    stack,
    "DummyBucket",
    block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
    removal_policy=cdk.RemovalPolicy.DESTROY,
)

cf_function = cloudfront.Function(stack, "Function", code=cloudfront.FunctionCode.from_file(file_path="function.js"))

# CloudFrontのディストリビューションを作成する
distribution = cloudfront.Distribution(
    stack,
    "Distribution",
    default_behavior=cloudfront.BehaviorOptions(
        origin=origins.S3Origin(bucket),
        function_associations=[
            cloudfront.FunctionAssociation(
                function=cf_function, event_type=cloudfront.FunctionEventType.VIEWER_REQUEST
            ),
        ],
    ),
    default_root_object="index.html",
)


app.synth()
