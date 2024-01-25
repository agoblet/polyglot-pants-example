import yaml
import shutil
import os

TARGET_DIR="src/terraform/some_generated_module"
TEMPLATE="""data "aws_iam_policy_document" "%s" {
  statement {
    effect = "Allow"
    actions = [
      "sts:AssumeRole"
    ]
    principals {
      type        = "Service"
      identifiers = ["codebuild.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "%s" {
  name_prefix        = "%s"
  assume_role_policy = data.aws_iam_policy_document.%s.json
}"""

with open('src/python/some_code_generator/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

shutil.rmtree(TARGET_DIR, ignore_errors=True)
os.mkdir(TARGET_DIR)

with open(f'{TARGET_DIR}/BUILD', 'w') as f:
    f.write("terraform_module()")

for role in config["roles"]:
    with open(f'{TARGET_DIR}/{role}.tf', 'w') as f:
        f.write(TEMPLATE % ((role,) * 4))
