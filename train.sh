# # batch size 에 따라 학습 결과 분석
# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=32
# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=64
# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=8

# # model size 별 분석
# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8n-seg.pt imgsz=640 batch=16
# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8s-seg.pt imgsz=640 batch=16
# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8l-seg.pt imgsz=640 batch=16
# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8x-seg.pt imgsz=640 batch=16

# # augmentation 테스트
# # base
# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=16 overlap_mask=false flipud=0.0 fliplr=0.0 copy_paste=0.0 mixup=0.0
# # flip
# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=16 overlap_mask=false flipud=0.5 fliplr=0.0 copy_paste=0.0 mixup=0.0
# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=16 overlap_mask=false flipud=0.0 fliplr=0.5 copy_paste=0.0 mixup=0.0
# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=16 overlap_mask=false flipud=0.5 fliplr=0.5 copy_paste=0.0 mixup=0.0
# # copy_paste
# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=16 overlap_mask=false flipud=0.0 fliplr=0.0 copy_paste=0.5 mixup=0.0
# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=16 overlap_mask=false flipud=0.0 fliplr=0.0 copy_paste=1.0 mixup=0.0

# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=16 overlap_mask=false flipud=0.5 fliplr=0.0 copy_paste=0.5 mixup=0.0
# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=16 overlap_mask=false flipud=0.0 fliplr=0.5 copy_paste=0.5 mixup=0.0
# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=16 overlap_mask=false flipud=0.5 fliplr=0.5 copy_paste=0.5 mixup=0.0

# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=16 overlap_mask=false flipud=0.5 fliplr=0.0 copy_paste=1.0 mixup=0.0
# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=16 overlap_mask=false flipud=0.0 fliplr=0.5 copy_paste=1.0 mixup=0.0
# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=16 overlap_mask=false flipud=0.5 fliplr=0.5 copy_paste=1.0 mixup=0.0
# # mixup
# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=16 overlap_mask=false flipud=0.0 fliplr=0.0 copy_paste=0.0 mixup=0.1
# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=16 overlap_mask=false flipud=0.0 fliplr=0.0 copy_paste=0.0 mixup=0.3
# yolo task=segment mode=train epochs=100 data=dataset/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=16 overlap_mask=false flipud=0.0 fliplr=0.0 copy_paste=0.0 mixup=0.5

# gaussian blur 테스트
yolo task=segment mode=train epochs=100 data=dataset_aug/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=16 overlap_mask=false flipud=0.5 fliplr=0.0 copy_paste=0.0 mixup=0.0
yolo task=segment mode=train epochs=100 data=dataset_aug_random/dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=16 overlap_mask=false flipud=0.5 fliplr=0.0 copy_paste=0.0 mixup=0.0




