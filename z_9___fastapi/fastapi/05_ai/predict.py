# 이미지 예측하기 전에 모델이 필요합니다.
# 모델 -> Tensorflow에서 다운받아서 불러오도록하겠습니다.

# Pillow를 사용해 이미지를 불러오기
from PIL.Image import Image
import numpy as np

from model_loader import model

from tensorflow.keras.applications.imagenet_utils import decode_predictions


# AI가 이해할 수 있도록 이미지를 변환해주는 함수입니다. -> numpy
def predict(image: Image):
    image = np.asarray(image.resize((224, 224)))[..., :3]  # RGB
    image = np.expand_dims(image, 0) #차원을 확장..  => 이미지가 2차원 -> 3차원으로 변경
    image = image / 127.5 - 1.0  # 0~255 -> -1~1  Saler(정규화) -> 이미지 데이터가 -1 ~ 1 형태로 정규화.

    results = decode_predictions(model.predict(image), 3)[0]          # 리스트에서 첫번째 값반환.  
    print('results : ', results)

    result_list = []
    for i in results:
        result_list.append({"class": i[1], "probability": f"{i[2]*100:0.2f}%"})

    return result_list




    
