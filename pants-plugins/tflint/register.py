# Copyright 2023 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).
from tflint.tflint import TFLint, TFLintRequest
from pants.core.goals.lint import LintResult
from pants.core.util_rules.external_tool import DownloadedExternalTool, ExternalToolRequest
from pants.core.util_rules.source_files import SourceFiles, SourceFilesRequest
from pants.engine.fs import Digest, MergeDigests
from pants.engine.platform import Platform
from pants.engine.process import FallibleProcessResult, Process
from pants.engine.rules import Get, MultiGet, collect_rules, rule
from pants.util.logging import LogLevel
from pants.util.strutil import pluralize
from pants.engine.env_vars import EnvironmentVars, EnvironmentVarsRequest
from pants.core.util_rules.config_files import ConfigFiles, ConfigFilesRequest
from pants.backend.terraform.dependency_inference import InferTerraformModuleDependenciesRequest, TerraformModuleDependenciesInferenceFieldSet
from pants.engine.target import InferredDependencies

@rule
async def run_tflint(request: TFLintRequest.Batch, tflint: TFLint, platform: Platform) -> LintResult:
    downloaded_tflint, sources, config_file = await MultiGet(
        Get(DownloadedExternalTool, ExternalToolRequest, tflint.get_request(platform)),
        Get(SourceFiles, SourceFilesRequest(fs.sources for fs in request.elements)),
        Get(ConfigFiles, ConfigFilesRequest, tflint.config_request()),
    )

    env = await Get(EnvironmentVars, EnvironmentVarsRequest(["PATH"]))

    input_digest = await Get(
        Digest,
        MergeDigests(
            (
                downloaded_tflint.digest,
                sources.snapshot.digest,
                config_file.snapshot.digest,
            )
        ),
    )

    argv = [
        downloaded_tflint.exe,
        *tflint.args,
        "--recursive"
    ]
    process_result = await Get(
        FallibleProcessResult,
        Process(
            argv=argv,
            input_digest=input_digest,
            description=f"Run tflint on {pluralize(len(sources.files), 'file')}",
            level=LogLevel.DEBUG,
            env=env
        ),
    )

    return LintResult.create(request, process_result)


def rules():
    return [
        *collect_rules(),
        *TFLintRequest.rules(),
    ]
