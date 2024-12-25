from bs4 import BeautifulSoup

def extract_class_content(file_path, target_class):
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, "lxml")
    elements = soup.find_all(class_=target_class)
    return set(element.text.strip() for element in elements)

follower_file = "path/to/follow.html" #替換
fan_file = "=path/to/fan.html" #替換

target_class = "_ap3a _aaco _aacw _aacx _aad7 _aade"

follower_content = extract_class_content(follower_file, target_class)
fan_content = extract_class_content(fan_file, target_class)

difference = follower_content - fan_content

for item in difference:
    print(item)
