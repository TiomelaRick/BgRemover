import os
from rembg import remove
from PIL import Image as imgg
from django.db import models
from django.core.files.storage import default_storage

# Charger le modèle CNN entraîné


# Create your models here.
# Create your models here.
class Image(models.Model):
    caption=models.ImageField()
    image=models.ImageField(upload_to="img/%y")

    def __str__(self):
        return self.caption

    def removebg(self):

        #output_folder = "output_image"
        #load the input image
        output_folder = 'main/static/images'
        filename = '10.png'
        output_path = os.path.join(output_folder, filename)
        #output_path = os.path("static\\images\\10.png") #output_path = os.path.join(output_folder, filename.split('.')[0] + '.png')

        input_image = imgg.open(self.image.path)
        input_image.thumbnail((500, 500))
        print(input_image)
        #remove the background using rembg
        output_image = remove(input_image)

        #self.caption.path=output_path
        #save the output into PNG file
        output_image.save(output_path)

        

