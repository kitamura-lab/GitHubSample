from ultralytics import YOLO

model = YOLO("yolov8x-pose.pt")

results = model("bus.jpg")
keypoints = results[0].keypoints
print(keypoints.data)
