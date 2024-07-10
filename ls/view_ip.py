import ipaddress


def net():
    network = ipaddress.IPv4Network('192.168.0.0/16')
    for ip in network:
        print(ip)


# 23_1 ==================
def generate_squares(n):
    for x in range(1, 1 + n):
        yield x**2


if __name__ == '__main__':
    gen = generate_squares(5)
    for k in range(5):
        try:
            print(next(gen))
        except StopIteration:
            print('finish')
