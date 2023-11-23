import logging
import pathlib
import subprocess

logging.basicConfig(level=logging.INFO)


def main():
    targets = get_targets()
    dependencies = get_dependencies(targets)
    graph_to_markdown(targets, dependencies)


def get_targets() -> list[str]:
    logging.info("getting targets")
    return (
        subprocess.run(["pants", "list", "::"], capture_output=True, check=True)
        .stdout.decode("utf-8")
        .strip("\n")
        .split("\n")
    )


def get_dependencies(targets: list[str]) -> list[tuple[str, str]]:
    logging.info("getting dependencies")
    dependencies = []
    for target in targets:
        target_dependencies = (
            subprocess.run(
                ["pants", "dependencies", target], capture_output=True, check=True
            )
            .stdout.decode("utf-8")
            .strip("\n")
            .split("\n")
        )
        dependencies.extend([(target, d) for d in target_dependencies if d != ""])
    return dependencies


def get_mermaid_proof_target(target: str) -> str:
    variable = target.replace("#", "_POUND_")
    label = strip_directory(target)

    return f"{variable}[{label}]"


def get_directory(target: str) -> str:
    if ":" in target:
        directory = pathlib.Path(target.split(":")[0])
    else:
        directory = pathlib.Path(target).parent
    if directory.is_file():
        directory = directory.parent
    return str(directory)


def strip_directory(target: str) -> str:
    directory = get_directory(target)
    return target.replace(directory, "").strip("/")


def graph_to_markdown(targets: list[str], dependencies: list[tuple[str, str]]) -> None:
    # TODO fix bug with nodes containing the word 'graph'
    logging.info("creating mermaid graph")
    targets_mermaid = "\n".join(
        [
            f"subgraph {get_directory(t)};{get_mermaid_proof_target(t)};end;"
            for t in targets
        ]
    )
    dependencies_mermaid = ";\n".join(
        [
            f"{get_mermaid_proof_target(t)} --> {get_mermaid_proof_target(d)}"
            for t, d in dependencies
        ]
    )

    mermaid_markdown = (
        f"```mermaid\n"
        f"graph LR;\n"
        f"{targets_mermaid}\n"
        f"{dependencies_mermaid}\n"
        f"```"
    )

    with open("pants_dependency_graph.md", "w") as f:
        f.write(mermaid_markdown)


if __name__ == "__main__":
    main()
