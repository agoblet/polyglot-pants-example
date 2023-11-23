module "some_cool_module" {
  source = "../some_cool_module"
}

provider "aws" {
  profile = "playground"
}

terraform {
  backend "s3" {
    bucket = "mlops-tf-playground"
    key    = "state/pants-test/terraform.tfstate"
    region = "eu-west-1"
  }
}