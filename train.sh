# batch size 에 따라 학습 결과 분석
yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=32
yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=64
yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=8

# model size 별 분석
yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8n-seg.pt imgsz=640 batch=16
yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8s-seg.pt imgsz=640 batch=16
yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8l-seg.pt imgsz=640 batch=16
yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8x-seg.pt imgsz=640 batch=16
