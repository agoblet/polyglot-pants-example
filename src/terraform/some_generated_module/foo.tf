data "aws_iam_policy_document" "foo" {
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

resource "aws_iam_role" "foo" {
  name_prefix        = "foo"
  assume_role_policy = data.aws_iam_policy_document.foo.json
}