# polyglot-pants-example

This repository serves as showcase for the [Pants](https://www.pantsbuild.org) build system.

## Highlighted features

General
- Caching of build results in [src/python/some_cool_library/main_test.py](src/python/some_cool_library/main_test.py)

Python
- 3rd party Python dependency management in [3rdparty/python](3rdparty/python)
- Reusable library code in [src/python/some_cool_library](src/python/some_cool_library)
- Deployed app code in [src/python/some_cool_app](src/python/some_cool_app)

Docker
- Dependency inference of base images in [src/python/some_cool_app/Dockerfile](src/docker/some_cool_app/Dockerfile)
- Publishing images to Dockerhub in [pants.toml](pants.toml)
- Tagging images with Git commit SHA in [BUILD](BUILD)
- Skipping publishing for internal base images in [src/docker/some_cool_base_image/BUILD](src/docker/some_cool_base_image/BUILD)

Polyglot
- Dependency inference between Docker and Python in [src/python/some_cool_app/Dockerfile](src/docker/some_cool_app/Dockerfile)
