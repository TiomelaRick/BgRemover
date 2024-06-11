from django.shortcuts import render,redirect

# Create your views here.
from .form import ImageForm
from .models import Image

# Create your views here.
def index(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if (form.is_valid()):
            form.save()
            obj=form.instance
            img=Image.objects.all()
            for x in img:
                x.removebg()
            return render(request,"index.html",{"img":img, "obj":obj})
    else:
        out_img=Image.objects.all()
        out_img.delete()
        form=ImageForm()
        img=Image.objects.all()
        #for x in img:
            #x.caption = x.removebg()
    return render(request,"index.html",{"img":img, "form":form})