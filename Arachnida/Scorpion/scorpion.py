from PIL import Image
from PIL.ExifTags import TAGS
from utils import Arguments, bcolors, cc


class Scorpion(Arguments):

    def __init__(self):
        super().__init__()


    def get_data_image(self, img):
        data = {
            "Filename": img.filename,
            "Image Size": img.size,
            "Image Height": img.height,
            "Image Width": img.width,
            "Image Format": img.format,
            "Image Mode": img.mode,
            "Image is Animated": getattr(img, "is_animated", False),
            "Frames in Image": getattr(img, "n_frames", 1)
        }
        return data


    def decrypt(self):
        for n, img_name in enumerate(self.image):
            cc(bcolors.BRIGHT_CYAN)
            text = f"Image {n}"
            centered_text = text.center(40, "*")
            print(centered_text + bcolors.ENDC, end="\n\n")

            img = Image.open(img_name)
            data = self.get_data_image(img)

            for label,value in data.items():
                if label == "Filename":
                    cc(bcolors.BRIGHT_GREEN)
                    print(f"{value}".center(40, " "), end="\n\n")
                    cc(bcolors.ENDC)
                else:
                    print(f"{label:25}: {value}")
            
            cc(bcolors.ENDC, ed="\n")
            
            text = "EXIF METADATA"
            centered_text = text.center(40, ".")
            exifdata = img.getexif()
            
            print(centered_text)
            if len(exifdata) == 0:
                print("n/a".center(40, " "))

            for tag_id in exifdata:
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id)
                if isinstance(data, bytes):
                    data = data.decode()
                print(f"{tag:25}: {data}")
            print(end="\n\n")
        return


def main():
    scorpion = Scorpion()
    print(scorpion)
    scorpion.decrypt()
    return


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(type(e), e, sep=" : ")

