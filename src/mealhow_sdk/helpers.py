import re


async def str_to_int(raw_data: str) -> int:
    data = raw_data.strip().split(".")[0]
    return int("".join([i for i in data if i.isdigit()]))


def to_snake_case(str_value: str) -> str:
    str_value = str_value.lower()
    str_value = re.sub(r"\W+", "_", str_value)
    return str_value.strip("_")
