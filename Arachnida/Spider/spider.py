import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from utils import Arguments, bcolors, _print_header, cc
import os, uuid


def get_content(url, lst, el):
    content = [urljoin(url, elem.get(el, "")) for elem in lst if elem.get(el)]
    return content


class Spider(Arguments):
    def __init__(self):
        super().__init__()
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        self.extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')
        self.content_type = ('image/png', 'image/jpg', 'image/jpeg', 'image/gif', 'image/bmp', 'image/webp')
        self.already_dw_images = []
        self.already_done_links = []
        pass

    def download_images(self, imgs):
        for img in imgs:
            if img in self.already_dw_images:
                print("This image was already downloaded, continuing...")
                continue
            else:
                self.already_dw_images.append(img)
            
            full_file = img.split("/")
            if len(full_file) > 1 and full_file[-1] == "":
                full_file.pop()
            file = full_file[-1].split("?")[0]
            try:
                response = requests.get(img)
                content_type = response.headers.get("Content-Type", "").lower()
                if not file.lower().endswith(self.extensions):
                    if content_type not in (self.content_type):
                        cc(bcolors.FAIL)
                        print("WRONG CONTENT TYPE->", content_type)
                        cc(bcolors.WARNING)
                        continue
                    file = f'default_{uuid.uuid4().hex}.' + content_type.split("/")[-1]
                    print("No extension found, now ->", file)
                img_data = response.content
                with open(os.path.join(self.path, file), 'wb') as handler:
                    handler.write(img_data)
                cc(bcolors.OKCYAN)
                print(f"New image {img} downloaded! :)")
                cc(bcolors.WARNING)
            except Exception as e:
                print(f"Couldn't download the image '{img}' because it was inaccessible, sorry :((")
        return

    def get_images(self, url, curr_depth):

        try:
            cc(bcolors.FAIL)
            print("\nCurr_depth =", curr_depth)
            cc(bcolors.ENDC)
            response = requests.get(url)
            cc(bcolors.OKBLUE, ed="\n")
            print("Response URL : ", response.url)
            cc(bcolors.OKGREEN)
            print(response, end="\n\n")

            soup = BeautifulSoup(response.content, "html.parser")
            if soup:
                imgs = soup.find_all('img')
                imgs = get_content(url, imgs, "src")
                links = soup.find_all('a', href=True)
                cc(bcolors.WARNING)
                links = get_content(url, links, "href")
                self.download_images(imgs)
                if curr_depth == 0:
                    print("Number of links:", len(links))
                if self.recursive == True and curr_depth + 1 <= self.max_depth:
                    if len(links):
                        cc(bcolors.ENDC)
                        for link in links:
                            if link in self.already_done_links:
                                print("Already visited this link, continuing...")
                                continue
                            self.already_done_links.append(link)
                            self.get_images(link, curr_depth + 1)
            else:
                cc(bcolors.ENDC)
                return
            cc(bcolors.ENDC)
            return
        except Exception as e:
            print(f"Couldn't access URL '{url}' because it was inaccessible, sorry :((")

    def start(self):
        _print_header(bcolors.BRIGHT_RED, "Let's begin now 😈")
        self.get_images(self.url, 0)
        print()
        _print_header(bcolors.OKGREEN, "Done ;)")


def main():
    spider = Spider()
    print(spider)
    spider.start()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(type(e), e, sep=" : ")
