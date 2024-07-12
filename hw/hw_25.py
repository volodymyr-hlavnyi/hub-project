from faker import Faker
from faker_food import FoodProvider
import random


def find_longest_word(check_list: list[str]) -> str:
    return sorted(check_list, key=lambda s: len(check_list))[::-1][0]


def create_fake_file(data: list):
    with open("products.txt", "w") as f:
        for line in data:
            f.write(line)
            f.write("\n")


def read_data() -> list:
    with open("products.txt", "r") as f:
        data = f.readlines()
    return data


def generate_cost():
    return random.randint(1, 100) / 10


def generate_pcs():
    return random.randint(1, 100)


def calculate_total_price(data: list(str)) -> int:
    sum_total = 0
    for line in data:
        key, cost, pcs = line.split(',')
        s_cost = float(cost)
        s_pcs = int(pcs)
        sum_total += s_cost * s_pcs
    return round(sum_total,2)


if __name__ == '__main__':
    print('\n25_1', '==' * 10)
    words = ["apple", "banana", "cherry", "dragonfruit"]
    result = find_longest_word(words)
    print(result)

    print('\n25_2', '==' * 10)

    fake = Faker()
    fake.add_provider(FoodProvider)
    my_data = []
    for i in range(100):
        my_data.append(f"{fake.fruit()}, {generate_cost()}, {generate_pcs()}")
    create_fake_file(my_data)
    data = read_data()
    # for item in data:
    #     print(item)
    total_sum = calculate_total_price(data)
    print(f"Total sum: {total_sum}")
