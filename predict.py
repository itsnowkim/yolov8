from ultralytics import YOLO

# model 경로
modelpath="yolov8m-seg.pt"
# predict target 파일 경로
sourcepath="1.jpeg"

model=YOLO(modelpath)
model.predict(source="1.png", show=True, save=True, hide_labels=False, hide_conf=False, conf=0.5, save_txt=False, save_crop=False, line_thickness=2)