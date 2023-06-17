from rembg import remove
from PIL import Image
import os

folder = "downloads"
output_folder = "downloads-semFundo"

num_files = len(os.listdir(folder))
num = len(os.listdir(output_folder))

print(num_files)

for i, k in enumerate(os.listdir(folder)):
    if k.endswith(".jpg"):
        j = i + num
        input_path = os.path.join(folder, k)
        output_path = os.path.join(output_folder, f"{j}.png")

        with Image.open(input_path) as image:
            image_with_alpha = remove(image)
            image_with_alpha.save(output_path)

        os.remove(input_path)
