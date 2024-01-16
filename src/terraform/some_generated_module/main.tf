data "aws_iam_policy_document" "test_assume_role" {
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
}
