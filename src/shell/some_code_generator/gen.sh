target_dir=../../terraform/some_generated_module
rm -rf $target_dir
mkdir $target_dir

echo "terraform_module()" > $target_dir/BUILD
echo 'data "aws_iam_policy_document" "test_assume_role" {
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

resource "aws_iam_role" "generated" {
  name_prefix        = "generated-pants-role"
  assume_role_policy = data.aws_iam_policy_document.test_assume_role.json
}' > $target_dir/main.tf
