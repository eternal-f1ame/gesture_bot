# import tensorflow as tf
# from tensorflow.python.keras.models import Sequential,Model
# from tensorflow.python.keras.metrics import Accuracy
# from tensorflow.python.keras.optimizers import Adam,SGD
# from tensorflow.python.keras.layers import Convolution2D,Dense,Softmax,InputLayer,MaxPool2D,Flatten,Dropout,Add,Input,Layer,add
# from tensorflow.python.keras.activations import relu,softmax,tanh
# from tensorflow.python.keras.losses import categorical_crossentropy,mean_absolute_error
# from tensorflow.python.keras.losses import sparse_categorical_crossentropy,mean_squared_error,mean_squared_logarithmic_error
# from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import cv2
from tensorflow import convert_to_tensor
from sklearn.preprocessing import LabelEncoder
import pickle
le = LabelEncoder()
import imutils
import numpy as np
from sklearn.metrics import pairwise
from sklearn.cluster import k_means
from tensorflow.python.keras.models import load_model
from tensorflow import convert_to_tensor
import xml.etree.ElementTree as ET

import rospy
import geometry_msgs
from geometry_msgs.msg import Twist