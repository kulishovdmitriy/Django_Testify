import random


def gen_password(length):
    result = "".join([str(random.randint(0, 9)) for _ in range(length)])
    return result


def parse_length(request, default=10):
    length = request.GET.get('length', str(default))
    if not length.isnumeric():
        raise ValueError("Value error: int")
    length = int(length)
    if not 3 < length < 100:
        raise ValueError("Length must be [3...100]")
    return length


def format_list(lst):
    return "<br>".join([str(value) for value in lst])
