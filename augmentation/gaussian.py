import cv2
import numpy as np

def apply_gaussian_blur(image, kernel_size=(15, 15), sigma=10, random_apply=False):
    if random_apply:
        # 이미지 크기 가져오기
        height, width = image.shape[:2]

        # 블러를 적용할 영역의 크기 설정 (예: 100x100)
        blur_size = height//2
        x = np.random.randint(0, width - blur_size)  # X 위치
        y = np.random.randint(0, height - blur_size) # Y 위치

        # 선택된 영역에 가우시안 블러 적용
        blurred_region = cv2.GaussianBlur(image[y:y+blur_size, x:x+blur_size], kernel_size, sigma)

        # 블러 처리된 영역을 원본 이미지에 다시 합치기
        image[y:y+blur_size, x:x+blur_size] = blurred_region
        return image
    else:
        # 전체 이미지에 가우시안 블러 적용
        return cv2.GaussianBlur(image, kernel_size, sigma)

if __name__ == "__main__":
    # 이미지 불러오기
    # image = cv2.imread('../dataset/test/images/00170404_086652_cropped.png')
    image = cv2.imread('../dataset/test/images/00170404_089881_cropped.png')
    cv2.imshow('Original Image', image)

    # 전체 이미지에 가우시안 블러 적용
    blurred_image_full = apply_gaussian_blur(image, random_apply=False)

    # 랜덤한 영역에만 가우시안 블러 적용
    blurred_image_partial = apply_gaussian_blur(image, random_apply=True)

    # 원본 이미지와 블러 처리된 이미지를 화면에 표시
    cv2.imshow('Blurred Image Full', blurred_image_full)
    cv2.imshow('Blurred Image Partial', blurred_image_partial)

    # 키 입력을 대기 (예: 0은 무한 대기)
    cv2.waitKey(0)

    # 모든 창 닫기
    cv2.destroyAllWindows()
