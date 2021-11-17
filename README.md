# Python AWS Lambda Serverless GitHub Actions Template

This is a simple template to setup a Python cron job as an AWS CloudFormation stack with a Lambda function and automatically deploy it using the Serverless framework with GitHub Actions. If you prefer to use CircleCI, check out this [template](https://github.com/nyoungstudios/py-lambda-circleci) instead. 

## Features

This template uses a couple of Serverless plugins to make deploying the CloudFormation stack easier.
- [`serverless-layers`](https://www.serverless.com/plugins/serverless-layers) allows you to install the Python packages in the [requirements.txt](./requirements.txt) file to a separate Lambda layer which reduces the size of your code layer.
- [`serverless-deployment-bucket`](https://www.serverless.com/plugins/serverless-deployment-bucket) allows us to manage the S3 deployment bucket versioning and permissions.

Additionally, I have setup a simple [Python function](src/logging_setup.py) so you can setup a logger for your project without getting double prints in AWS CloudWatch.

## How to Setup?

1. Create a new repository based off of this template. Here is the GitHub [documentation](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/creating-a-repository-from-a-template) about creating a repository from a template.
2. In your AWS console, create a new [IAM policy](https://console.aws.amazon.com/iam/home?#/policies). If you are unsure what permissions to add to the policy, I've created a [minimal IAM policy](./gh-actions-aws-iam.json) with all the necessary permissions that GitHub Actions needs to deploy your CloudFormation stack. You can simply copy this to the AWS IAM policy JSON editor. Within the IAM policy JSON file, change `us-west-1` to whatever region you are using. Additionally change placeholder number `012345678901` to your AWS account number.
3. Next, create a [AWS User](https://console.aws.amazon.com/iam/home?#/users) based off of this policy. Set the `Access type` to `Programmatic access`. And on the permissions page, select `Attach existing policies directly` and search for the policy you just created in step 4.
4. Within the `Settings` tab on your GitHub repository, click on the `Secrets` tab and set the environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` from the AWS User that you just created. Additionally, you can set the `AWS_DEFAULT_REGION` too.
5. And that's it! Now, whenever you push to your GitHub repository, your code will automatically be deployed as a CloudFormation stack.

## Python Versions

This template uses `Python 3.8`, but if you prefer to use a different Python version, just change `3.8` in [serverless.yml](./serverless.yml) and [deploy.yml](.github/workflows/deploy.yml) to whatever version you like. Here are the supported [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html) Python runtimes. 
