from tools.service import print_name
import requests
import re
from collections import Counter


@print_name
def hw36_1():
    def get_response(url: str):
        return requests.get(f"{url}")

    url = "https://example.com"
    response = get_response(url)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    print("Response Headers:", response.headers)


@print_name
def hw36_2():
    async def get_common_words(url_list):
        all_words = []
        word_pattern = re.compile(r'\b\w+\b')

        try:
            for url in url_list:
                print(f"Processing {url}")
                response = requests.get(url)
                if response.status_code == 200:
                    all_words.extend(word_pattern.findall(response.text))
        except Exception as e:
            print(f"Error: {e}")

        return all_words

    site_list = [
        "https://example.com",
        "https://lms.itcareerhub.de",
        "https://www.google.com",
        "https://www.youtube.com",
        "https://www.facebook.com",
        "https://www.instagram.com",
        "https://www.twitter.com", ]

    result = get_common_words(site_list)
    result_count = Counter(result)
    for k, v in result_count.most_common(10):
        print(f"{v}: {k}")


if __name__ == '__main__':
    hw36_1()
    hw36_2()
