import cv2
import json
from ultralytics import YOLO
from google.colab.patches import cv2_imshow  # Import cv2_imshow for Colab

def process_video_from_json(json_path, model_path, output_path=None):
    # Load the data from the JSON file
    with open(json_path, 'r') as f:
        vids = json.load(f)

    video_data=vids["videos"][0];
    video_path = video_data["video_path"]
    latitude = video_data["location"]["latitude"]
    longitude = video_data["location"]["longitude"]

    # Load the YOLOv8 model
    model = YOLO(model_path)

    # Open the video file or webcam
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Cannot open video.")
        return None,None

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Define the codec and create VideoWriter if saving output
    if output_path:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        if not ret:
            print("Finished processing video.")
            break

        # Perform object detection on the frame
        results = model(frame)

        # Visualize the detections on the frame
        annotated_frame = results[0].plot()

        # Save the annotated frame to the output file
        if output_path:
            out.write(annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print(f"Latitude: {latitude}, Longitude: {longitude}")

    # Release resources
    cap.release()
    if output_path:
        out.release()
    cv2.destroyAllWindows()
    return latitude,longitude

# Example Usage
json_path ="/content/videos.json"  # Path to your JSON file
model_path = "/content/runs/detect/train/weights/best.pt"  # YOLOv8 model path
output_path = "output.mp4"  # Path to save the output video
lat,lng= process_video_from_json(json_path, model_path, output_path)

