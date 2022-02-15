import colorsys

import numpy as np
import cv2 as cv

if __name__ == '__main__':
    imag = cv.imread("12.jpg")
    t_gray = cv.cvtColor(imag, cv.COLOR_BGR2RGB)
    cv.imshow("read_img", imag)
    cv.imwrite("gray.jpg", t_gray)
    cv.imshow("t_gray", t_gray)


    # 等待
    cv.waitKey(0)
    # 释放内存
    cv.destroyAllWindows()
