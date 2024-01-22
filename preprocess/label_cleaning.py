import cv2
import glob
import os
import numpy as np
from tqdm import tqdm

def find_scope_video(video_path):
    pass

def find_scope_img_cv(img_path):
    if isinstance(img_path, str):
        image = cv2.imread(img_path)
    else:
        image = img_path

    # 그레이 스케일로 변환합니다.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 엣지 검출을 수행합니다.
    edges = cv2.Canny(gray, 50, 150)

    # 컨투어를 찾습니다.
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 가장 큰 컨투어를 찾습니다.
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        
        # 컨투어에 내접하는 원이 아닌 외접하는 사각형을 구합니다.
        x, y, w, h = cv2.boundingRect(largest_contour)
        
        # 이미지를 사각형 영역으로 자릅니다.
        crop_img = image[y:y+h, x:x+w]

        # 바운딩 박스를 다른 색상으로 그립니다.
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('img', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # 결과 이미지와 crop 된 이미지 return
    return image, crop_img

def find_scope_img_man(img_path):
    image = cv2.imread(img_path)

    h, w, _ = image.shape
    # 이미지의 중심 좌표
    y = h//2
    x = w //2
    # 반지름 길이
    r = y
    # offset
    offset = 10

    crop_img = image[0:h, x-r-offset:x+r+offset]

    return crop_img

def process_imgs(target_dir):
    # 루트 디렉토리 하위의 모든 .png 파일을 찾음
    for img_path in tqdm(glob.glob(os.path.join(target_dir, '**/*.png'), recursive=True)):
        # scope 영역을 찾고, 해당 영역으로 crop
        image, crop_img = find_scope_img_cv(img_path)

        # cv2.imwrite('result.png', image)
        # cv2.imwrite('cropped_result.png', crop_img)

        # 이미지를 640x640으로 리사이즈
        resized_image = cv2.resize(crop_img, (640, 640))

        # 리사이즈된 이미지를 원래 파일에 덮어씀
        cv2.imwrite(img_path, resized_image)

if __name__ == "__main__":
    # target dir 내의 img 를 processing
    # process_imgs(target_dir='../dataset_cleaned')

    # find_scope_img_cv('../dataset_cleaned/test/images/00177442_003649.png')

    crop_img = find_scope_img_man('../dataset_cleaned/test/images/00177442_003649.png')

