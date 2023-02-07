import cv2


def draw_box(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 0), 3, 1)

    width = img.shape[2]
    if x + w / 2 < (width / 2) - 50:
        str = "left"
    elif x + w / 2 > (width / 2) + 50:
        str = "right"
    else:
        str = "mid"

    cv2.putText(img, F'Tracking {x} {str}',
                (15, 70), font, 0.5, (0, 0, 255), 2)

    return (width / 2) - (x + w / 2)
