import re


def camel_to_snake_case(string: str) -> str:
    snake_string = re.sub(r"(?<!^)(?=[A-Z])", "_", string).lower()
    return snake_string


def add_plural_form(string: str) -> str:
    if string.endswith("s"):
        return f"{string}es"
    return f"{string}s"


def generate_tablename(string: str) -> str:
    snake_case = camel_to_snake_case(string)
    plural_snake_case = add_plural_form(snake_case)
    return plural_snake_case
