from django.shortcuts import render
from django.core.files.storage import default_storage

from .models import Triangle, Round, Diamond, Oval, Oblong, Heart, Square
from keras.preprocessing import image
# from tensorflow import Graph,Session
# from tensorflow import Session
import tensorflow as tf
import cv2
import os
import json
import numpy as np
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


from django.shortcuts import render
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
import numpy as np

from bar.models import Triangle
global graph,model

#function to handle an uploaded file.
from .cnn import cnn

# img_height, img_width=200,200
# with open('./models/imagenet_classes.json','r') as f:
#     labelInfo=f.read()

# labelInfo=json.loads(labelInfo)

# model_graph = Graph()
# with model_graph.as_default():
#     tf_session = Session()
#     with tf_session.as_default():
#         model=load_model('cnn.h5')


# Create your views here.
def index(request):
    return render(request, 'bar/index.html')

def face(request):
    
    return render(request, 'bar/face.html')

def predict(request):

    # Models

    triangle = Triangle.objects.all()
    diamond = Diamond.objects.all()
    oval = Oval.objects.all()
    oblong = Oblong.objects.all()
    round = Round.objects.all()
    heart = Heart.objects.all()
    square = Square.objects.all()

    context = {'triangle':triangle,'diamond':diamond,'oval':oval,'oblong':oblong,'round':round,'heart':heart,'square':square}
    if request.method == 'POST' and  'cnnBtn' in request.POST:
        

        upload1 = request.FILES['upload1']
        fss = FileSystemStorage()
        file = fss.save(upload1.name, upload1)
        file_url = fss.url(file)
        img_path='static'+file_url
        
        
        classe = cnn(img_path)
        print(file)
        print(file_url)
        # print(classe)

        context={'classe':classe,'file_url':file_url,'triangle':triangle ,'diamond':diamond,'oval':oval,'oblong':oblong,'round':round,'heart':heart,'square':square}

        if classe=="heart":
            return render(request, 'bar/heart.html', context)    

        elif classe=="diamond":
            return render(request, 'bar/diamond.html', context)    
        
        elif classe=="oblong":
            return render(request, 'bar/oblong.html', context)    
        
        elif classe=="oval":
            return render(request, 'bar/oval.html', context)    

        elif classe=="round":
            return render(request, 'bar/round.html', context)    

        elif classe=="square":
            return render(request, 'bar/square.html', context)    

        else:
            return render(request, 'bar/triangle.html', context)    
        
        return render(request, 'bar/predict.html', context)
    
    return render(request, 'bar/predict.html',context)


def diamond(request):
    diamond = Diamond.objects.all()
    context = {'diamond':diamond}
    return render(request, 'bar/diamond.html',context)


def triangle(request):
    triangle = Triangle.objects.all()
    context = {'triangle':triangle}
    return render(request, 'bar/triangle.html', context)




def oval(request):
    oval = Oval.objects.all()
    context = {"oval":oval}
    return render(request, 'bar/oval.html', context)




def oblong(request):
    oblong = Oblong.objects.all()
    context = {'oblong':oblong}
    return render(request, 'bar/oblong.html', context)




def round(request):
    round = Round.objects.all()
    context = {'round':round}
    return render(request, 'bar/round.html', context)


def heart(request):
    heart = Heart.objects.all()
    context = {'heart':heart}
    return render(request, 'bar/heart.html', context)


def square(request):
    square = Square.objects.all()
    context = {'square':square}
    return render(request, 'bar/square.html', context)
