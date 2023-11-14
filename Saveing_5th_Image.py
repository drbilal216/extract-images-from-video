import os
import cv2
from ultralytics import YOLO
from datetime import datetime

model = YOLO("yolov8s.pt")

video_path = "3.mp4"
cap = cv2.VideoCapture(video_path)

# Set the new width and height for resizing
new_width = 1280 #640
new_height = 720 #480

# Get the video properties
fps = cap.get(cv2.CAP_PROP_FPS)

# Flag to track recording status
recording = False
frame_count = 0

# Create a folder to save frames
output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

# Save every 5th frame
save_every_nth_frame = 5
frame_counter = 0

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        # Resize the frame
        frame = cv2.resize(frame, (new_width, new_height))

        results = model(frame, device='cpu', classes=0, conf=0.3)
        annotated_frame = results[0].plot()

        for result in results[0]:
            class_id = result.boxes.cls.cpu().numpy().astype(int)
            print(class_id)
            if class_id == 0:
                print("########################")
                print("Person detected!")
                # Save every 5th frame
                frame_counter += 1
                if frame_counter % save_every_nth_frame == 0:
                    frame_count += 1
                    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    image_path = os.path.join(output_folder, f"frame_{frame_count}_{current_time}.jpg")
                    cv2.imwrite(image_path, frame)
                    print(f"Frame saved: {image_path}")

                # Start recording if not already recording
                if not recording:
                    recording = True
                    print("Recording started!")

            else:
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("No person detected.")

                # Stop recording if currently recording
                if recording:
                    recording = False
                    print("Recording stopped!")

        cv2.imshow("Video", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()