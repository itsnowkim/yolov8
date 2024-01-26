import cv2
import os
from ultralytics import YOLO

# model 경로
modelpath="runs/segment/baseline/weights/best.pt"
model=YOLO(modelpath)

# predict target 파일 경로
# sourcepath="./dataset/test/images/00170404_086811.png"

for i in range(2,11):
    sourcepath=f"videos/Timeline {i}.mp4"
    basename = os.path.basename(sourcepath)

    if sourcepath.endswith('mp4'):
        cap = cv2.VideoCapture(sourcepath)
        
        # 비디오 쓰기를 위한 준비
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        out = cv2.VideoWriter(f'output_{basename}', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

        # Loop through the video frames
        while cap.isOpened():
            # Read a frame from the video
            success, frame = cap.read()

            if success:
                # Run YOLOv8 inference on the frame
                results = model(frame)

                # Visualize the results on the frame
                annotated_frame = results[0].plot()

                # 추론된 프레임을 비디오 파일에 쓰기
                out.write(annotated_frame)

            else:
                # 비디오의 끝이면 반복 중단
                break

        # 비디오 캡처 객체와 비디오 쓰기 객체 해제 및 모든 창 닫기
        cap.release()
        out.release()
        cv2.destroyAllWindows()