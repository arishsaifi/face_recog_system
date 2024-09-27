import face_recognition
import cv2
import os
import numpy as np

def load_images_from_dataset(path='dataset/'):
    images = []
    classNames = []

    folders = os.listdir(path)
    for folder in folders:
        folder_path = os.path.join(path, folder)
        if os.path.isdir(folder_path):
            for img_name in os.listdir(folder_path):
                img_path = os.path.join(folder_path, img_name)
                curImg = cv2.imread(img_path)
                if curImg is not None:
                    images.append(curImg)
                    classNames.append(folder)
                    print(f"Loaded image: {img_path}")
                else:
                    print(f"Failed to load image: {img_path}")

    return images, classNames

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img)
        
        if encodings:  # Check if encodings are found
            encodeList.append(encodings[0])
        else:
            print("No face found in the image.")

    return encodeList

if __name__ == '__main__':
    images, classNames = load_images_from_dataset()
    encoded_face_train = findEncodings(images)

    # Saving encodings using numpy
    np.save('encoded_faces.npy', encoded_face_train)
    np.save('class_names.npy', np.array(classNames))  # Convert to NumPy array
    print("Encoded faces and class names have been saved.")
