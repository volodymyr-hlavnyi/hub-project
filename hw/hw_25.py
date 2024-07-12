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


def calculate_total_price(data: list):
    sum_cost = 0
    sum_pcs = 0
    for line in data:
        key, cost, pcs = line.split(',')
        sum_cost += float(cost)
        sum_pcs += int(pcs)
    return sum_cost, sum_pcs


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
    cost, pcs = calculate_total_price(data)
    print(f"Total cost: {cost}, pcs: {pcs}")
