python_sources()
pex_binary(name="bin", entry_point="main.py", environment="docker_python")
file(name="yaml", source="config.yaml")
archive(name="archive", packages=[":bin"], files=[":yaml"], format="zip")
