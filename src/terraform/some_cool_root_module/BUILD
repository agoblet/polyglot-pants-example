terraform_module()
terraform_deployment(
    name="some_cool_root_module_deployment",
    root_module=":some_cool_root_module",
    dependencies=[":lockfile", "src/python/some_lambda:lambda"],
)
file(name="lockfile", source=".terraform.lock.hcl")
