import cv2


class ImageProcessor:
    """
    The ImageProcessor class manages and applies various image processing methods and deep learning models.
    It allows for registration of custom methods and models, and provides functionality to apply them to images.
    """

    def __init__(self):
        self.methods = {}
        self.models = {}

    def register_method(self, name, method):
        """
        Register a new image processing method.
        :param name: The name of the method.
        :param method: The method function.
        """
        self.methods[name] = method

    def register_model(self, name, model):
        """
        Register a new deep learning model.
        :param name: The name of the model.
        :param model: The model object.
        """
        self.models[name] = model

    def apply_method(self, img, method_name, **kwargs):
        """
        Apply a registered image processing method.
        :param img: The input image.
        :param method_name: The name of the method to apply.
        :param kwargs: Additional parameters for the method.
        :return: The processed image.
        """
        if method_name not in self.methods:
            raise ValueError(f"Method {method_name} not registered.")
        return self.methods[method_name](img, **kwargs)

    def apply_model(self, img, model_name, **kwargs):
        """
        Apply a registered deep learning model.
        :param img: The input image.
        :param model_name: The name of the model to apply.
        :param kwargs: Additional parameters for the model.
        :return: The processed image and labels.
        """
        if model_name not in self.models:
            raise ValueError(f"Model {model_name} not registered.")
        return self.models[model_name].predict(img, **kwargs)


# Example methods and model stubs

def detect_faces(img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), **kwargs):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=scaleFactor,
        minNeighbors=minNeighbors,
        minSize=minSize,
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    labels = []
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        labels.append(f"bbox: {x}, {y}, {w}, {h}")

    return img, labels


class DummyModel:
    def predict(self, img, **kwargs):
        # Placeholder for a deep learning model prediction
        height, width, _ = img.shape
        labels = f"bbox: 0, 0, {width}, {height}"
        return img, labels
