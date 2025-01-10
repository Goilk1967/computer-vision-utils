import cv2
import numpy as np
class ImageAugmentor:
    def __init__(self, image):
        self.image = image
    def random_rotate(self):
        angle = np.random.uniform(-30, 30)
        h, w = self.image.shape[:2]
        M = cv2.getRotationMatrix2D((w//2, h//2), angle, 1.0)
        return cv2.warpAffine(self.image, M, (w, h))
    def horizontal_flip(self):
        return cv2.flip(self.image, 1)
