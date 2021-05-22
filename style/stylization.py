#import tensorflow as tf
from tensorflow.image import resize
from tensorflow import constant
#from tensorflow import image.resize
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np


predictor_instance = None


class Predictor():
    
    def __init__(self):

        self.hub_module = hub.load('styleModel.tar.gz')


    def prepareImage(self, file_path):

        content_image = plt.imread(file_path)
        content_image = content_image.astype(np.float32)[np.newaxis, ...] / 255.

        return content_image


    def prepareStyleImage(self, file_path):

        style_image = plt.imread(file_path)
        style_image = style_image.astype(np.float32)[np.newaxis, ...] / 255.

        style_image = resize(style_image, (256, 256))
        
        return style_image

    def predict(self, styleImage_path, contentImage_path):

        content_image = self.prepareImage(contentImage_path)
        style_image = self.prepareStyleImage(styleImage_path)

        outputs = self.hub_module(constant(content_image), constant(style_image))
        stylized_image = outputs[0]

        return stylized_image


class SingleFactoryPredictor():
    
    predictor_instance = None

    def __init__(self):
        if self.predictor_instance:
            return self.predictor_instance
        else:
            self.predictor_instance = Predictor()
            return self.predictor_instance

    @staticmethod
    def get_instance(self):
        if self.predictor_instance:
            return self.predictor_instance
        else:
            self.predictor_instance = Predictor()
            return self.predictor_instance