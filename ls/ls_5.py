def get_weather():
    is_sunny = bool(int(input('Is sunny (0/1)? ')))
    is_rainy = bool(int(input('Is rainy (0/1)? ')))
    is_windy = bool(int(input('Is windy (0/1)? ')))
    is_snowy = bool(int(input('Is snowy (0/1)? ')))
    is_foggy = bool(int(input('Is foggy (0/1)? ')))
    return is_sunny, is_rainy, is_windy, is_snowy, is_foggy


def give_recomendation(
        is_sunny,
        is_rainy,
        is_windy,
        is_snowy,
        is_foggy):
    recomendation = ''
    if is_sunny:
        recomendation += ' Go for a walk'
    if is_rainy:
        recomendation += ' Take an umbrella'
    if is_windy:
        recomendation += ' Take a hat'
    if is_snowy:
        recomendation += ' Take a scarf'
    if is_foggy:
        recomendation += ' Take a flashlight'
    # if
    # else:
    #     print('Stay at home')
    return recomendation


if __name__ == '__main__':
    weather = get_weather()
    print(give_recomendation(*weather))
