module "some_cool_module" {
  source = "../some_cool_module"
}

provider "aws" {}

terraform {
 backend "s3" {
   bucket = "lighthouse-mlops-tf-state"
   key    = "state/pants-test-axel/terraform.tfstate"
   region = "eu-west-1"
 }
}

module "lambda_function" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = "my-lambda1"
  description   = "My awesome lambda function"
  handler       = "lambda_function.handler"
  runtime       = "python3.9"

  create_package = false
  local_existing_package = "../../../dist/src.python.some_lambda/lambda.zip"
}
