import PIL.Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width = 100):
    width, height = image.size
    ratio = 0.45
    new_height = int(new_width * (height / width) * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)

def main(new_width=100):
    ilosc = int(input("Podaj ilość plików, które chcesz przekonwertować na ascii: "))
    for i in range(ilosc):
        path = input(f"Podaj ścieżkę dla {i+1} pliku: ")
        try:
            image = PIL.Image.open(path)
        except:
            print(path, "jest nieprawidłową ścieżką obrazu.")
        new_image_data = pixels_to_ascii(grayify(resize_image(image)))

        pixel_count = len(new_image_data)

        ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
        
        with open(f"ascii_image{i+1}.txt", "w") as f:
            f.write(ascii_image)
    print("Konwertowanie zakończone!")
main()