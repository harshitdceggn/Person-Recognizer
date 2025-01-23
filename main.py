from deepface import DeepFace
import cv2
import threading
import time

def detect_faces(frame):
    return DeepFace.extract_faces(frame, detector_backend="opencv", enforce_detection=False)

def recognize_faces(face_img, images, names, model):
    found_match = False
    matched_name = "UNKNOWN"

    for idx, img in enumerate(images):
        result = DeepFace.verify(img, face_img, model_name=model, enforce_detection=False)
        if result["verified"]:
            matched_name = names[idx]
            found_match = True
            break

    return found_match, matched_name

def process_frame(frame, images, names, model):
    output_frame = frame.copy()
    faces = detect_faces(frame)
    for face in faces:
        if "facial_area" in face:
            facial_area = face['facial_area']
            startX, startY = facial_area['x'], facial_area['y']
            endX, endY = startX + facial_area['w'], startY + facial_area['h']

            face_img = frame[startY:endY, startX:endX]
            found_match, matched_name = recognize_faces(face_img, images, names, model)

            if found_match:
                cv2.rectangle(output_frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                cv2.putText(output_frame, matched_name, (startX, startY - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            else:
                cv2.rectangle(output_frame, (startX, startY), (endX, endY), (0, 0, 255), 2)
                cv2.putText(output_frame, "UNKNOWN", (startX, startY - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    return output_frame

def compare(image_list, video_source=0, model="VGG-Face"):
    images = []
    names = list(image_list.keys())

    for name, image_path in image_list.items():
        img = cv2.imread(image_path)
        if img is not None:
            images.append(img)
        else:
            print(f"Warning: Unable to load image from {image_path}")

    video_capture = cv2.VideoCapture(video_source)

    def update_frame():
        nonlocal ret, frame
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break
            time.sleep(0.01)

    ret, frame = video_capture.read()
    threading.Thread(target=update_frame, daemon=True).start()

    while True: 
        if not ret:
            break

        start_time = time.time()

        output_frame = process_frame(frame, images, names, model)
        processing_time = time.time() - start_time
        fps = 1 / processing_time
        cv2.putText(output_frame, f"FPS: {fps:.2f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow("Video", output_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

image_list = {
    "harshit": r"D:\harshit_intern\harshit1.jpg", 
    "modi ji": r"D:\harshit_intern\modi1.jpg"
}
compare(image_list)
