import os
import shutil

filelist = os.listdir('dataset')
jpeg_files = [f for f in filelist if f.endswith('.jpeg')]

idx=0
testlist = []
for f in jpeg_files:
    idx+=1
    if idx%10 == 0:
        testlist.append(f)

# 선택된 파일과 동일한 이름을 가진 '.json' 파일을 './test' 폴더로 이동
for file_name in testlist:
    # 확장자 제외한 파일 이름
    base_name = file_name.split('.')[0]

    # '.jpeg' 파일과 '.json' 파일의 경로
    jpeg_path = os.path.join('dataset', file_name)
    json_path = os.path.join('dataset', base_name + '.json')

    # './test' 폴더로 '.jpeg' 파일 이동
    shutil.move(jpeg_path, os.path.join('./dataset/test', file_name))

    # '.json' 파일이 존재한다면, 이동
    if os.path.exists(json_path):
        shutil.move(json_path, os.path.join('./dataset/test', base_name + '.json'))

