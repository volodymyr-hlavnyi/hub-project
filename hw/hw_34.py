from tools.service import print_name


@print_name
def hw34_1():
    def extract_emails(text):
        import re
        pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
        return_text = []
        matches = re.findall(pattern, text)
        if len(matches) > 0:
            return_text = matches
        else:
            return_text = "Don`t find any emails..."

        return return_text

    text = "Contact us at info@example.com or support@example.com for assistance."
    emails = extract_emails(text)
    print(emails)


@print_name
def hw34_2():
    # Напишите функцию highlight_keywords(text, keywords),
    # которая выделяет все вхождения заданных ключевых
    # слов в тексте, окружая их символами *.
    # Функция должна быть регистронезависимой при
    # поиске ключевых слов.
    def highlight_keywords(text, keywords):
        import re
        for keyword in keywords:
            text = re.sub(re.compile(f'({keyword})', re.IGNORECASE), r'*\1*', text)

        return text

    text = "This is a sample text. We need to highlight Python and programming."
    keywords = ["python", "programming"]
    highlighted_text = highlight_keywords(text, keywords)
    print(highlighted_text)


if __name__ == '__main__':
    hw34_1()
    hw34_2()
