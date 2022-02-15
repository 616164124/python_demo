
import numpy as np
import cv2


def te():
    print("1213")
    return


if __name__ == '__main__':
    # Create a black image
    img = np.zeros((512, 512, 3), np.uint8)

    # draw a diagonal blue line with thickness of 5 px
    cv2.line(img, (0, 0), (260, 260), (255, 0, 0), 5)
    cv2.line(img, (122, 33), (260, 260), (122, 123, 0), 4)

    # 为了演示，建窗口显示出来
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 300, 300)  # 定义frame的大小
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    te()

