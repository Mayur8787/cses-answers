import os
import dotenv
import argparse
import requests

from bs4 import BeautifulSoup

dotenv.load_dotenv(".env")


class Generator:
    """
    To generate predefind templates
    number: The problem number
    """

    def __init__(self, number):
        self.number = number
        self.base_URL = "https://www.cses.fi/"
        self.login_id = os.getenv("LOGIN")
        self.password = os.getenv("PASSWORD")
        self.session = requests.Session()
        self.directory = ""
        self.session.get(self.base_URL + "login/")
        self.phpsessid = self.session.cookies.get("PHPSESSID")
        self.headers = {
            "Host": "cses.fi",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "85",
            "Origin": "https://cses.fi",
            "Connection": "keep-alive",
            "Referer": "https://cses.fi/login",
            "Cookie": f"PHPSESSID={self.phpsessid}",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Priority": "u=0, i",
        }

    def request(self, method: str, url: str, data=None):
        if method == "get":
            response = self.session.get(url=url)
        else:
            response = self.session.post(url=url, headers=self.headers, data=data)
        return response

    def parse(self, response):
        return BeautifulSoup(response.text, features="html.parser")

    def findTag(self, soup: BeautifulSoup, tagname: str, filters: dict[str, str]):
        return soup.find(tagname, attrs=filters)

    def login(self):
        response = self.request(url=self.base_URL + "login/", method="get")
        if response.status_code != 200:
            return f"Error occured. Status={response.status_code}"
        soup = self.parse(response)
        tag = self.findTag(
            soup, tagname="input", filters={"name": "csrf_token", "type": "hidden"}
        )
        if not tag:
            return "csrf_token not found"
        csrf_token = tag.get("value")
        payload = {
            "nick": self.login_id,
            "pass": self.password,
            "csrf_token": csrf_token,
        }

        response = self.request(
            method="post", url=f"{self.base_URL}login/", data=payload
        )

        if response.status_code != 200:
            return f"Error. Status={response.status_code}"
        return "Success"

    def get_tests(self):
        response = self.request(
            method="get", url=f"{self.base_URL}problemset/tests/{self.number}/"
        )
        if response.status_code != 200:
            return
        soup = self.parse(response)
        self.csrf_token = self.findTag(
            soup,
            tagname="input",
            filters={"type": "hidden", "name": "csrf_token"},
        ).get("value")
        response = self.request(
            method="post",
            url=f"{self.base_URL}problemset/tests/{self.number}/",
            data={"csrf_token": self.csrf_token, "download": "true"},
        )
        return response.content

    def create_template(self):
        content = """
class Solution:
    def give_input(self,inp):
        pass

    def solution(self):
        pass


if __name__ == "__main__":
    obj = Solution()
"""

        with open(f"{self.directory}/solution.py", "w") as fp:
            fp.write(content)
        return None

    def generate(self):
        response = self.request(method="get", url=self.base_URL + "problemset/")
        if response.status_code != 200:
            return f"Error occured. Status={response.status_code}"
        soup = self.parse(response)
        tag = self.findTag(
            soup, tagname="a", filters={"href": f"/problemset/task/{self.number}"}
        )
        if not tag:
            return f"Problem no. {self.number} is invalid"
        self.directory = tag.text.strip().lower().replace(" ", "_")
        if os.path.exists(self.directory):
            return f'Directory for problem "{tag.text}" already exists.'
        os.mkdir(self.directory)
        self.create_template()
        message = self.login()
        if message != "Success":
            return f"Error. {message}"
        filedata = self.get_tests()
        self.session.cookies.clear()
        with open(f"{self.directory}/tests.zip", "wb") as fp:
            fp.write(filedata)
        return "Template and tests generated successfully."


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("problem_number", help="Number of the problem")
    args = parser.parse_args()
    obj = Generator(args.problem_number)
    print(obj.generate())
