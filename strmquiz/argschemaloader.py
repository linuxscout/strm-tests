import ast
import json
from pathlib import Path
from typing import Any, Dict, Union


class myArgsValidator:
    def __init__(self, source: Union[str, Path, Dict[str, Any]]):
        """
        source: path to json file, raw json string, or dict
        """

        if isinstance(source, (str, Path)):
            path = Path(source)
            if path.exists():
                text = path.read_text(encoding="utf-8").strip()
                if not text:
                    raise ValueError(f"JSON file {path} is empty")
                self.schema = json.loads(text)
            else:
                self.schema = json.loads(str(source))
        elif isinstance(source, dict):
            self.schema = source
        else:
            raise ValueError(f"Unsupported source type: {type(source)}")

    def get_command_schema(self, cmd: str) -> Dict[str, Any]:
        return self.schema.get(cmd, {})

    def validate_args_file(self, filename=""):
        if filename:
            path = Path(filename)
            text = ""
            if path.exists():
                text = path.read_text(encoding="utf-8").strip()
                if not text:
                    raise ValueError(f"JSON file {path} is empty")
            json_text = json.loads(text)
            validated_args = self.validate_args(json_text)
            return validated_args
        return {}

    def validate_args(
        self,
        provided: Dict[str, Any],
        command="",
    ) -> Dict[str, Any]:

        validated = {}

        if command:
            args_schema = self.schema.get(command, {}).get("args", {})
        else:
            args_schema = self.schema.get("args", {})
        # print("Provided", provided)
        # print("args schema", args_schema)
        # args_schema = self.schema.get("args", {})
        for arg_name, spec in args_schema.items():
            # 1. take provided value or default
            value = provided.get(arg_name, spec.get("default"))

            # 2. type check
            expected_type = spec.get("type")
            if expected_type == "integer":
                try:
                    value = int(value)
                except TypeError:
                    raise TypeError(f"{arg_name} {value} must be an integer")
            if expected_type == "float":
                try:
                    value = float(value)
                except TypeError:
                    raise TypeError(f"{arg_name} {value} must be an float")

            elif expected_type == "string":
                value = str(value)
            elif expected_type == "boolean":
                value = bool(value)
            elif expected_type == "list":

                if not isinstance(value, list):
                    value = ast.literal_eval(str(value))
                    if not isinstance(value, list):
                        raise ValueError(
                            f"{arg_name} {value} {type(value)} must be a list"
                        )
            elif expected_type == "dict":
                if not isinstance(value, dict):
                    value = ast.literal_eval(str(value))
                    if not isinstance(value, dict):
                        raise ValueError(f"{arg_name} must be a dict")

            # 3. range check
            if "range" in spec and isinstance(value, int):
                lo, hi = spec["range"]
                if not (lo <= value <= hi):
                    raise ValueError(f"{arg_name} must be between {lo} and {hi}")

            # 4. choices check
            if "choices" in spec and value not in spec["choices"]:
                raise ValueError(f"{arg_name} must be one of {spec['choices']}")

            validated[arg_name] = value

        return validated


if __name__ == "__main__":
    # Load schema (from file or dict)
    pass
