import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from utils import Arguments, bcolors, _print_dict, cc
import os, uuid

def get_content(url, lst, el):
    content = [urljoin(url, elem.get(el, "")) for elem in lst if elem.get(el)]
    if el != "href":
        print(*content, sep="\n")
    return content


class Spider(Arguments):
    def __init__(self):
        super().__init__()
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        self.extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')
        pass

    def download_images(self, imgs):
        for img in imgs:
            full_file = img.split("/")
            if len(full_file) > 1 and full_file[-1] == "":
                full_file.pop()
            file = full_file[-1].split("?")[0]
            if not file.lower().endswith(self.extensions):
                print("REFUSED ->", file)
                # file = f'default_{uuid.uuid4().hex}.jpg'

            response = requests.get(img)
            img_data = response.content
            with open(os.path.join(self.path, file), 'wb') as handler:
                handler.write(img_data)
        return

    def get_images(self, url, curr_depth):

        response = requests.get(url)
        cc(bcolors.OKGREEN)
        print(response)
        cc(bcolors.OKBLUE, ed="\n")
        print("Response URL : ", response.url)
        cc(bcolors.OKGREEN, ed="\n")

        soup = BeautifulSoup(response.content, "html.parser")
        if soup:
            imgs = soup.find_all('img')
            # print(imgs)
            imgs = get_content(url, imgs, "src")
            # print(imgs)
            # print("coucou")
            links = soup.find_all('a', href=True)
            cc(bcolors.WARNING, ed="\n")
            links = get_content(url, links, "href")
            self.download_images(imgs)
            # return
            if self.recursive == True and curr_depth + 1 <= self.max_depth:
                if len(links):
                    for link in links:
                        self.get_images(link, curr_depth + 1)
        else:
            cc(bcolors.ENDC)
            return
        cc(bcolors.ENDC)
        return



def main():
    spider = Spider()
    print(spider)
    print(spider.url)
    spider.get_images(spider.url, 0)
    exit()


if __name__ == "__main__":
    # try:
        main()
    # except Exception as e:
        # print(type(e), e, sep=" : ")
