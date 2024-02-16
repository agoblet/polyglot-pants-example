python_sources()
python_aws_lambda_function(
    name="lambda",
    runtime="python3.9",
    # Pants will convert this to `project.lambda_example:example_handler`.
    handler="main.py:lambda_handler",
)
