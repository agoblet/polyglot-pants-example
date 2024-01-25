module "some_cool_module" {
  source = "../some_cool_module"
}

provider "aws" {
  profile = "playground"
}

terraform {
  backend "s3" {
    bucket = "lighthouse-mlops-tf-state"
    key    = "state/pants-test-axel/terraform.tfstate"
    region = "eu-west-1"
  }
}
