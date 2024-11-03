from playsound import playsound
from rembg import remove
from PIL import Image
import os
from tqdm import tqdm

input_folder = "/Users/arronax/Desktop/conv"
output_folder = "/Users/arronax/Desktop/output"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

image_files = [file for file in os.listdir(input_folder) if file.endswith(".png")]
progress_bar = tqdm(total=len(image_files))

for filename in image_files:
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)

    img = Image.open(input_path)
    R = remove(img)
    R.save(output_path)
    progress_bar.update(1)

progress_bar.update(1)
progress_bar.close()

playsound('/Users/arronax/scripts/vomit.wav')
print("готовенько")