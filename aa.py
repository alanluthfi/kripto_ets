from PIL import Image
import pickle
image = Image.open("test_out.png")
pixels = list(image.getdata())
width, height = image.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

bs = pickle.dumps(pixels)
print(pixels)