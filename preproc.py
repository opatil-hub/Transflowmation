import os
from PIL import Image

image_dir = '../DeepLIIF_Training_Set/'
imtypes = ["IHC", "Hematoxlyn", "mpIF_DAPI", "mpIF_Lap2", "mpIF_Ki67", "Segmentation"]
for imtype in imtypes:
    os.makedirs('../' + imtype+  "_Training_Set", exist_ok=True)
fnames = os.listdir(image_dir)

image = Image.open(image_dir + fnames[0])
small_image = image.crop([512 * 5, 0, 512 * (5+1), 512])
print(small_image.size)

for fname in fnames:
    image = Image.open(image_dir + fname)
    for i, imtype in enumerate(imtypes):
        small_image = image.crop([512 * i, 0, 512 * (i+1), 512])
        small_image.save('../' + imtype + '_Training_Set/' + fname)
