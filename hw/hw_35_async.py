import requests
import re
from collections import Counter
import asyncio
import aiohttp


async def hw36_1():
    async def get_response(url: str, session: aiohttp.ClientSession):
        try:
            async with session.get(url) as response:
                print(f"Fetching {url}")
                status = response.status
                headers = response.headers
                text = await response.text()
                return (status, text, headers)
        except Exception as e:
            print(f"Error fetching{url} {e}")
            return "", 0, {}

    url_list = ["https://example.com"]
    async with aiohttp.ClientSession() as session:
        tasks = [get_response(url, session) for url in url_list]
        responses = await asyncio.gather(*tasks)

    for status, header, text in responses:
        print("Status Code:", status)
        print("Response Text:", header)
        print("Response Headers:", status)


async def hw36_2():
    async def fetch(url, session):
        try:
            async with session.get(url) as response:
                print(f"Fetching {url}")
                return await response.text()
        except Exception as e:
            print(f"Error fetching{url} {e}")
            return ""

    async def get_common_words(url_list):
        all_words = []
        word_pattern = re.compile(r'\b\w+\b')

        async with aiohttp.ClientSession() as session:
            tasks = [fetch(url, session) for url in url_list]
            responses = await asyncio.gather(*tasks)

        for response in responses:
            all_words.extend(word_pattern.findall(response))

        return all_words

    site_list = [
        "https://example.com",
        "https://lms.itcareerhub.de",
        "https://www.google.com",
        "https://www.youtube.com",
        "https://www.facebook.com",
        "https://www.instagram.com",
        "https://www.twitter.com", ]

    result = await get_common_words(site_list)
    result_count = Counter(result)
    for k, v in result_count.most_common(10):
        print(f"{v}: {k}")


if __name__ == '__main__':
    asyncio.run(hw36_1())
    asyncio.run(hw36_2())
