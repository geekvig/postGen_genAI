# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json

def process_posts(raw_file_path, processed_file_path="data/processed_posts.json"):
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        print (posts)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process_posts()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
