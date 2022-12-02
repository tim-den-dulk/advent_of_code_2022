import requests
import os
from pathlib import Path


class GetInputs:
    def __init__(self, day):
        self.day = day
        self.filepath = Path(f"day/day{day}.txt")

    def lines(self):
        if not os.path.exists(self.filepath):
            self.download()
        return self.get_from_file()

    def get_from_file(self):
        with open(self.filepath, "r") as file:
            data = file.readlines()
            return [line[:-1] for line in data]

    def download(self):
        """
        Feels like a chore to implement this with headers & authorization, just do it manually for now
        also this https://www.reddit.com/r/adventofcode/comments/z9dhtd/please_include_your_contact_info_in_the_useragent/
        """
        print(Path(os.curdir).resolve())
        raise NotImplementedError("please download manually")
        # os.makedirs(self.filepath.parent, exist_ok=True)
        # session = requests.Session()
        # url = f"https://adventofcode.com/2021/day/{self.day}/input"
        # text = session.get(url).text
        # with open(self.filepath, "w") as file:
        #     file.write(text)
        #     file.write("\n")
