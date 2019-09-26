import cv2

text_file = open("../hello-mot-master/walkingdataset/frames/train/E1/gt/gt.txt", "r")
#파일 불러오기
lines = text_file.readlines()
# print(lines)
gt = []
for a in lines:
    split_a = a.split(',')
    split_a = list(map(int, split_a))
    gt.append(split_a)
    #라인별로 읽어 int형으로 저장해둔다

dot_list=[]
for i in gt:
    index = i[0]
    fileindex = index + 1
    img = cv2.imread('../hello-mot-master/walkingdataset/frames/train/E1/img1/{0:03d}.jpg'.format(fileindex))

    x = gt[index][2]
    y = gt[index][3]
    w = gt[index][4]
    h = gt[index][5]
    #보기쉽게 변수설정

    x_of_dot=int(x+w/2)
    y_of_dot=int(y+h/2)
    #그릴 dot의 위치설정을 위한 변수 설정

    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
    dot_list.append([x_of_dot,y_of_dot])
    for a,b in dot_list:
        cv2.line(img, (a, b), (a, b), (255, 0, 0), 20)


    cv2.imshow('image', img)
    cv2.imwrite('../hello-mot-master/walkingdataset/frames/train/E1/img2/{0:03d}.jpg'.format(fileindex),img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
