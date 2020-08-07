import base64
import hashlib
import os 
from os import path
from basescript import BaseScript

IMAGE_EXT = ['png', 'jpg', 'img']


class ImageProcessor(BaseScript):
    def __init__(self):
        super().__init__()
        self.img_dir = self.args.image_dir
        # Check if the Image Directory Exists
        if not os.path.isdir(self.img_dir):
            self.log.info("Invalid image directoy path")
            raise Exception("Not a valid directory")
        self.images = self.prime_images(self.img_dir)
        self.processed_imgs = self.process_images(self.images).keys()

    def _generate_hash(self, key):
        return hashlib.md5(bytes(key,'utf8')).hexdigest()

    def prime_images(self, im_dir):
        proc_images = []
        self.log.info("reading images from the path")
        for f in os.listdir(im_dir):
            im_path = path.join(im_dir, f)
            if path.isfile(im_path) and f.split(".")[1] in IMAGE_EXT:
                proc_images.append(im_path)
        return proc_images

    def process_images(self, images):
        encoded_images = {}
        for image_path in images:
            with open(image_path, "rb") as imageFile:
                enc_image = base64.b64encode(imageFile.read())
                # Generating Unique id based on first 100 encoded characters
                enc_id = self._generate_hash(str(enc_image[0:100]))
                encoded_images[enc_id] = enc_image
        return encoded_images

    def define_args(self, parser):
        parser.add_argument("-i", "--image-dir", help="Path of image directory", required=True)

#if __name__ == "__main__":
#    ImageProcessor().start()

