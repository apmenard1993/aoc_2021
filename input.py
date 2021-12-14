import requests


def get_input(num):
    url = f"https://adventofcode.com/2021/day/{num}/input"
    cookies = {
        "session": "53616c7465645f5fedddaa59b7e83000b052be89c5c7a624efa801b6cd66f6d3a380383c391cda13599a1f53f397bc2b"}
    headers = {"Accept-Encoding": "gzip"}
    resp = requests.get(url, cookies=cookies, headers=headers)
    return resp.text

