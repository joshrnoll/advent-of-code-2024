import requests

def get_input():
    day = input("Enter day: ")
    url = f"https://adventofcode.com/2024/day/{day}/input"

    my_session_cookie = input("Enter your session cookie: ")
    cookies = dict(session=my_session_cookie)
    response = requests.get(url, cookies=cookies)

    return response.text