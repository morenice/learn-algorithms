import random
import string
import json


def make_random_key(key_len=10):
    random_key_factor = string.ascii_lowercase + string.digits + string.ascii_uppercase
    return ''.join(random.choice(random_key_factor) for _ in range(key_len))


def make_random_value(max_value=100000000):
    return random.randint(0,max_value)


if __name__ == "__main__":
    data_count = 100000
    data_dup_per = 10.0
    write_file = "input.txt"

    dup_data_count = int(data_count / data_dup_per)
    new_data_count = data_count - dup_data_count

    new_data = [(make_random_key(), make_random_value()) for _ in range(new_data_count)]

    for data in new_data:
        if len(new_data) >= data_count:
            break

        new_data.insert(random.randint(0, len(new_data)), data)

    with open(write_file, "w") as f:
        f.write(json.dumps(new_data))
