import numpy as np
import cv2 as cv


if __name__ == '__main__':
    imag = cv.imread("12.jpg")
    t_gray = cv.resize(imag, dsize=(50, 50))
    imag_color = cv.cvtColor(imag, 6)
    cv.imshow("imag_color", imag_color)
    cv.imshow("123.jpg", imag)
    print("未修改", imag.shape)
    print("修改", t_gray.shape)
    image_crop = np.array([
        [1.6, 0, -150],
        [0, 1.6, -240]
    ], dtype=np.float32)
    image_crop_jpg = cv.warpAffine(imag, image_crop, (183, 275))
    cv.imshow("image_crop_jpg", image_crop_jpg)

    while True:
        # 检测键盘输入q（必须是英文的）
        if ord('q') == cv.waitKey(0):
            break
    # 释放内存
    cv.destroyAllWindows()
