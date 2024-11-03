from playsound import playsound
import os
from PIL import Image, ExifTags
from tqdm import tqdm

def correct_orientation(img):
    """
    Исправляет ориентацию изображения на основе EXIF-данных.
    """
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = img._getexif()

        if exif is not None:
            orientation_value = exif.get(orientation)

            if orientation_value == 3:
                img = img.rotate(180, expand=True)
            elif orientation_value == 6:
                img = img.rotate(270, expand=True)
            elif orientation_value == 8:
                img = img.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        # Если нет EXIF или ориентации, просто возвращаем исходное изображение
        pass

    return img

def main():
    src_dir = input("Введите путь к папке с исходными изображениями: ")
    dst_dir = input("Введите путь к папке для сохранения конвертированных изображений: ")

    # Спрашиваем степень сжатия у пользователя
    quality = int(input("Введите степень сжатия для JPEG (от 0 до 100): "))

    images = os.listdir(src_dir)
    progress_bar = tqdm(total=len(images))

    for image in images:
        img_path = os.path.join(src_dir, image)
        img = Image.open(img_path)

        # Исправляем ориентацию изображения на основе EXIF-данных
        img = correct_orientation(img)

        # Извлекаем EXIF, если оно существует
        exif_data = img.info.get('exif')

        # Сохраняем изображение с EXIF и указанным качеством
        output_path = os.path.join(dst_dir, os.path.splitext(image)[0] + '.jpg')
        if exif_data:
            img.save(output_path, 'JPEG', exif=exif_data, quality=quality)
        else:
            img.save(output_path, 'JPEG', quality=quality)

        progress_bar.update(1)

    progress_bar.close()

main()
playsound('vomit.wav')  # Относительный путь к звуковому файлу