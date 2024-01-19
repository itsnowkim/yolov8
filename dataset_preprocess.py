import cv2
import os
import glob
from tqdm import tqdm

# 루트 디렉토리 설정
dataset_root_dir = 'dataset_640'
# 루트 디렉토리 하위의 모든 .jpeg 파일을 찾음
for jpeg_path in tqdm(glob.glob(os.path.join(dataset_root_dir, '**/*.png'), recursive=True)):
    # 이미지 로드
    image = cv2.imread(jpeg_path)

    # 이미지를 640x640으로 리사이즈
    resized_image = cv2.resize(image, (640, 640))

    # 리사이즈된 이미지를 원래 파일에 덮어씀
    cv2.imwrite(jpeg_path, resized_image)

print("모든 이미지가 리사이즈되어 저장되었습니다.")
