import cv2
import json
import os
import numpy as np
import glob
from tqdm import tqdm

def find_scope_img_man(img_path):
    image = cv2.imread(img_path)

    h, w, _ = image.shape
    y = h // 2
    x = w // 2
    r = y
    offset = 10
    dist = r + offset

    crop_img = image[0:h, x-dist:x+dist]
    imgheight, imgwidth, _ = crop_img.shape
    label = organize_label(imgheight, imgwidth, img_path=img_path, x=x, y=y, dist=dist)

    return crop_img, label

def organize_label(imgheight, imgwidth, img_path, x, y, dist):
    label_path = os.path.splitext(img_path)[0] + '.json'

    with open(label_path, 'r') as file:
        label_data = json.load(file)

        # 예를 들어 라벨 데이터가 바운딩 박스의 좌표를 포함하고 있다고 가정
        # 라벨 데이터 구조에 따라 조정 필요
        for item in label_data['shapes']:
            # item['points']는 라벨의 좌표 리스트를 포함
            for point in item['points']:
                # 이미지를 중심으로 크롭했기 때문에 x 좌표를 조정
                point[0] -= (x - dist)

        # labelPath 필드 수정
        label_data['imagePath'] = img_path.split('\\')[-1].split('.')[0] + '_cropped.png'

        # img 크기 필드 수정
        label_data['imageHeight'] = imgheight
        label_data['imageWidth'] = imgwidth

    return label_data

if __name__ == "__main__":
    # 루트 디렉토리 설정
    dataset_root_dir = '../train'
    # 새로 저장될 디렉토리
    dest_dir = '../dataset_clean'

    # 루트 디렉토리 하위의 모든 .jpeg 파일을 찾음
    for img_path in tqdm(glob.glob(os.path.join(dataset_root_dir, '**/*.jpeg'), recursive=True)):
        img, label = find_scope_img_man(img_path)
        
        # 새 이미지 저장
        cropped_img_path = os.path.join(dest_dir, img_path.split('\\')[-1].split('.')[0] + '_cropped.png')
        cv2.imwrite(cropped_img_path, img)

        # 업데이트된 라벨 파일 저장
        updated_label_path = os.path.join(dest_dir, img_path.split('\\')[-1].split('.')[0] + '_cropped.json')
        with open(updated_label_path, 'w') as file:
            json.dump(label, file, indent=4)
