import tensorflow as tf
import cv2


def cnn(image_path):
    image =cv2.imread(image_path, cv2.IMREAD_COLOR)
    print(image_path)
    print(image)
    
    image = cv2.resize(image, (200,200))
    image = image.reshape((1,200,200,3))
    
   
    model = tf.keras.models.load_model('cnn.h5')
    predict = model.predict(image,verbose=1)
    if predict[0][0] == 0:
        result = 'diamond'
        return result
    
    elif predict[0][0] == 1:
        result = 'heart'
        return result
    
    elif predict[0][0] == 2:
        result = 'oblong'
        return result

    elif predict[0][0] == 3:
        result = 'oval'
        return result

    elif predict[0][0] == 4:
        result = 'round'
        return result
    
    elif predict[0][0] == 5:
        result = 'square'
        return result

    else:
        result = 'triangle'
        return result


model = tf.keras.models.load_model('cnn.h5')