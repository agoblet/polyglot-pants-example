# Copyright 2023 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).
import logging

from pants.backend.terraform.target_types import TerraformFieldSet
from pants.core.goals.lint import LintTargetsRequest
from pants.core.util_rules.external_tool import ExternalTool
from pants.core.util_rules.config_files import ConfigFilesRequest
from pants.core.util_rules.partitions import PartitionerType
from pants.engine.platform import Platform
from pants.option.option_types import ArgsListOption, BoolOption, FileOption, SkipOption

logger = logging.getLogger(__name__)


class TFLint(ExternalTool):
    """A Pluggable Terraform Linter."""

    options_scope = "terraform-tflint"
    name = "tflint"
    help = "tflint"
    default_version = "v0.50.3"
    default_known_versions = [
        "v0.50.3|macos_arm64|95291d30a2a360a4762a788ad9823b094b81cc192de85586d575e591b24204bc|9365626"
    ]

    skip = SkipOption("lint")
    args = ArgsListOption(example="--minimum-severity=MEDIUM")

    def config_request(self) -> ConfigFilesRequest:
        return ConfigFilesRequest(
            discovery=True,
            check_existence=[".tflint.hcl"],
        )

    def generate_url(self, plat: Platform) -> str:
        plat_str = {
            "macos_arm64": "darwin_arm64",
            "macos_x86_64": "darwin_amd64",
            "linux_arm64": "linux_arm64",
            "linux_x86_64": "linux_amd64",
        }[plat.value]
        return f"https://github.com/terraform-linters/tflint/releases/download/{self.version}/tflint_{plat_str}.zip"

    def generate_exe(self, _: Platform) -> str:
        return "./tflint"


class TFLintRequest(LintTargetsRequest):
    field_set_type = TerraformFieldSet
    tool_subsystem = TFLint
    partitioner_type = PartitionerType.DEFAULT_SINGLE_PARTITION
