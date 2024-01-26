import os
import json
import numpy as np
from tqdm import tqdm
from ultralytics import YOLO

def ndarray_serialize(data):
    output = []
    for obj in data:
        if isinstance(obj, np.ndarray):
            output.append(obj.tolist())
    
    return output[0]

def construct_json(results, img_name, output_dir):
    results = results[0]

    # 결과를 JSON 형식으로 변환
    json_data = {
        "version": "0.3.3",
        "flags": {},
        "shapes": [],
        "imagePath": os.path.basename(img_name),
        "imageData": None,
        "imageHeight": results.orig_shape[0],
        "imageWidth": results.orig_shape[1],
        "text": ""
    }
    # import pdb; pdb.set_trace();
    for idx, r in enumerate(results):
        # {0: 'BF', 1: 'LF', 2: 'Fat', 3: 'Bone', 4: 'Dura', 5: 'Instrument', 6: 'Vessel', 7: 'Care'}
        class_name = r.names
        # print(f"box cls : {r.boxes.cls} \t idx : {idx}")
        cls_idx = r.boxes.cls[0]
        # print(f"cls_dix : {cls_idx}")
        cls = class_name[int(cls_idx)]
        masks=r.masks[0].xy
        mask = ndarray_serialize(masks)
        # print(f"mask len : {len(masks)}")
        shape = {
            "label": cls,
            "text": "",
            "points": mask,
            "group_id": None,
            "shape_type": "polygon",
            "flags": {}
        }
        json_data["shapes"].append(shape)

    # json 파일 저장 경로 설정
    json_name = os.path.basename(img_name).split('.')[0] + '.json'
    json_path = os.path.join(output_dir, json_name)
    
    # json 파일 저장
    with open(json_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)
    
    return json_path

if __name__ == "__main__":
    # Load a model
    model = YOLO("../runs/segment/baseline/weights/best.pt")  # 모델 경로 수정
    
    source = 'source'  # 소스 이미지 경로 수정
    output_dir = 'source'  # 출력 JSON 파일 경로 수정
    os.makedirs(output_dir, exist_ok=True)
    
    # source directory 에 있는 모든 img 에 대해 json 파일 생성
    for img_name in tqdm(os.listdir(source)):
        img_path = os.path.join(source, img_name)
        # 이미지 파일이 아닌 경우 건너뛰기
        if not img_path.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue
        
        # Inference the model
        try:
            results = model(img_path, verbose=False)
        except Exception as e:
            print(f"img : {img_name}\nerror : {e}\n")
            continue
        
        # output 으로 json 파일 만들기
        construct_json(results, img_path, output_dir)

    print("모든 이미지에 대해 json 파일을 만들었습니다.")
