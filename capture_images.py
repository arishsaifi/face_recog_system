import cv2
import os

def capture_images(emp_name, save_dir='dataset/', img_count=10):
    cam = cv2.VideoCapture(0)
    
    if not cam.isOpened():
        print("Camera could not be opened")
        return

    # Create directory for saving images
    path = os.path.join(save_dir, emp_name)
    if not os.path.exists(path):
        os.makedirs(path)

    captured_count = 0
    while captured_count < img_count:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break

        cv2.imshow("Capturing Images", frame)

        # Save image
        img_name = os.path.join(path, f"{emp_name}_{captured_count}.jpg")
        cv2.imwrite(img_name, frame)
        print(f"Captured {img_name}")
        captured_count += 1

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    emp_name = input("Enter the employee's name: ")
    capture_images(emp_name)
