data "aws_iam_policy_document" "bar" {
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

resource "aws_iam_role" "bar" {
  name_prefix        = "bar"
  assume_role_policy = data.aws_iam_policy_document.bar.json
}