# ts에서 모델 불러오기
# pip install tensorflow

import tensorflow as tf

def load_model():
# 모델 다운로드 불러오기.  
    model = tf.keras.applications.MobileNetV2(weights="imagenet")
    print("Success to load model")

    return model

model = load_model()