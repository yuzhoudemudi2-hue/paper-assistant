"""Small YAML loading wrapper with a Phase 1 fallback parser."""

from pathlib import Path
from typing import Any


class YamlLoadError(RuntimeError):
    """Raised when YAML content cannot be parsed."""


def load_yaml_mapping(path: Path) -> dict[str, Any]:
    """Load a YAML mapping from disk.

    Args:
        path: YAML file path.

    Returns:
        Parsed mapping.

    Raises:
        YamlLoadError: If parsing fails or the file does not contain a mapping.
    """

    text = path.read_text(encoding="utf-8")
    content = _load_with_pyyaml(text)
    if content is None:
        content = _load_simple_yaml(text)

    if not isinstance(content, dict):
        raise YamlLoadError(f"YAML file must contain a mapping: {path}")

    return content


def _load_with_pyyaml(text: str) -> Any | None:
    """Use PyYAML when it is installed."""

    try:
        import yaml
    except ModuleNotFoundError:
        return None

    try:
        return yaml.safe_load(text) or {}
    except yaml.YAMLError as exc:
        raise YamlLoadError("YAML content is invalid.") from exc


def _load_simple_yaml(text: str) -> dict[str, Any]:
    """Parse the simple YAML subset used by Phase 1 configuration templates."""

    root: dict[str, Any] = {}
    stack: list[tuple[int, dict[str, Any]]] = [(-1, root)]
    pending_list_key: tuple[int, dict[str, Any], str] | None = None

    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        stripped_line = raw_line.strip()

        if stripped_line.startswith("- "):
            if pending_list_key is None:
                raise YamlLoadError("List item found without a parent key.")
            list_indent, parent, key = pending_list_key
            if indent <= list_indent:
                raise YamlLoadError("List item indentation is invalid.")
            if parent.get(key) == {}:
                parent[key] = []
            current_list = parent.setdefault(key, [])
            if not isinstance(current_list, list):
                raise YamlLoadError("List parent is not a list.")
            current_list.append(_parse_scalar(stripped_line[2:].strip()))
            continue

        pending_list_key = None
        while stack and indent <= stack[-1][0]:
            stack.pop()
        if ":" not in stripped_line or not stack:
            raise YamlLoadError(f"Unsupported YAML line: {raw_line}")

        key, raw_value = stripped_line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        parent_mapping = stack[-1][1]

        if raw_value == "":
            child: dict[str, Any] = {}
            parent_mapping[key] = child
            stack.append((indent, child))
            pending_list_key = (indent, parent_mapping, key)
        else:
            parent_mapping[key] = _parse_scalar(raw_value)

    return root


def _parse_scalar(raw_value: str) -> Any:
    """Parse a scalar from the simple YAML subset."""

    if raw_value in {"[]", ""}:
        return []
    if raw_value in {"true", "True"}:
        return True
    if raw_value in {"false", "False"}:
        return False
    if raw_value.startswith('"') and raw_value.endswith('"'):
        return raw_value[1:-1]
    if raw_value.startswith("'") and raw_value.endswith("'"):
        return raw_value[1:-1]

    try:
        return int(raw_value)
    except ValueError:
        pass

    try:
        return float(raw_value)
    except ValueError:
        return raw_value
