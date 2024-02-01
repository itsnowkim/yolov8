import os
import shutil
import glob
import cv2
import numpy as np
from tqdm import tqdm
from gaussian import apply_gaussian_blur

def copy_directory_structure(src, dst):
    print("소스 디렉토리 구조와 파일을 대상 디렉토리로 복사합니다.")
    for dirpath, dirnames, filenames in tqdm(os.walk(src)):
        # 대상 디렉토리 경로 생성
        structure = os.path.join(dst, os.path.relpath(dirpath, src))
        if not os.path.isdir(structure):
            os.makedirs(structure)

        # 파일 복사
        for file in filenames:
            src_file = os.path.join(dirpath, file)
            dst_file = os.path.join(structure, file)
            shutil.copyfile(src_file, dst_file)

def apply_random_gaussian_blur_to_images(src, dst):
    print("이미지 파일에 랜덤으로 가우시안 블러를 적용합니다.")
    for filepath in tqdm(glob.iglob(dst + '/**/*.png', recursive=True)):
        # 이미지 로드
        image = cv2.imread(filepath)

        # 0.5 확률로 블러 적용
        if np.random.rand() < 0.5:
            image = apply_gaussian_blur(image, random_apply=True)

        # 결과 이미지 저장
        cv2.imwrite(filepath, image)

if __name__ == "__main__":
    root = '../dataset'
    dest = '../dataset_aug_random'

    # root 디렉토리에서 dest 디렉토리로 복사
    copy_directory_structure(root, dest)

    # dest 디렉토리에 있는 이미지 파일에 가우시안 블러 적용
    apply_random_gaussian_blur_to_images(root, dest)
