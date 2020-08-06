import base64
import hashlib
import os 
from os import path

IMAGE_EXT = ['png', 'jpg', 'img']
class PublishImage:
    def __init__(self, img_dir):
        self.img_dir = img_dir
        # Check if the Image Directory Exists
        if not os.path.isdir(img_dir):
            raise Exception("Not a valid directory")
        self.images = self.prime_images(self.img_dir)
        self.process_images(self.images)

    def _generate_hash(self, key):
        return hashlib.md5(bytes(key,'utf8')).hexdigest()

    def prime_images(self, im_dir):
        proc_images = {}
        for f in os.listdir(im_dir):
            im_path = path.join(im_dir, f)
            if path.isfile(im_path) and f.split(".")[1] in IMAGE_EXT:
                proc_images[f.split(".")[0]] = im_path 
        return proc_images

    def process_images(self, images):
        self.encoded_images = {}
        for image_name, image_path in images.items():
            with open(image_path, "rb") as imageFile:
                enc_image = base64.b64encode(imageFile.read())
                enc_id = self._generate_hash(image_name)
                self.encoded_images[enc_id] = enc_image

        print(self.encoded_images.keys())

obj = PublishImage("sample_images")

