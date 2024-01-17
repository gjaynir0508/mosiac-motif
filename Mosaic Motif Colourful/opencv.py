import cv2 as cv
import numpy as np

PIXELS_PER_BOX = 75
BORDER = 11


def mosaic_arr(r, c, c_arr, pixels_per_box=PIXELS_PER_BOX, border=BORDER):
    multiplier = pixels_per_box + border
    arr = np.full((r * multiplier + border, c * multiplier +
                  border, 3), (0, 0, 255), dtype=np.uint16)
    for i in range(r):
        for j in range(c):
            arr[border + i * multiplier:border + i * multiplier + pixels_per_box, border + j * multiplier:border + j * multiplier +
                pixels_per_box] = (c_arr[i][j] * 180, 255, 180) if c_arr[i][j] != 0 else (0, 0, 255)

    return cv.cvtColor(arr.astype(np.uint8), cv.COLOR_HSV2BGR)


def highlight_boxes(arr, r1, c1, r2, c2, pixels_per_box=PIXELS_PER_BOX, border=BORDER, color=(121, 17, 234), thickness=BORDER // 2 - 1):
    copy = arr.copy()
    multiplier = pixels_per_box + border
    start = border // 2 - thickness // 2
    copy[r1 * multiplier + start:r1 * multiplier + start + thickness,
         c1 * multiplier + start:c2 * multiplier + start] = color
    copy[r2 * multiplier + start:r2 * multiplier + start + thickness,
         c1 * multiplier + start:c2 * multiplier + start + thickness] = color
    copy[r1 * multiplier + start:r2 * multiplier + start, c1 *
         multiplier + start:c1 * multiplier + start + thickness] = color
    copy[r1 * multiplier + start:r2 * multiplier + start + thickness, c2 *
         multiplier + start:c2 * multiplier + start + thickness] = color

    return copy


def color_from_number(num):
    r, g, b = cv.cvtColor(np.array([[(num * 180, 255, 180)
                                     if num != 0 else (0, 0, 255)]]).astype(np.uint8), cv.COLOR_HSV2RGB)[0][0]
    return f"#{r:02x}{g:02x}{b:02x}", (r, g, b)


if __name__ == "__main__":
    arr = mosaic_arr(3, 4, [[1, 2, 1, 2], [2, 1, 1, 1], [2, 2, 1, 3]])
    hex, (r, g, b) = color_from_number(100)
    arr[5:45, 5:45] = b, g, r

    cv.imshow("image", arr)
    cv.waitKey(0)
    cv.destroyAllWindows()

    arr = highlight_boxes(arr, 0, 0, 1, 2)
    cv.imshow("image", arr)
    cv.waitKey(0)
    cv.destroyAllWindows()

    cv.imwrite("image.png", arr)
