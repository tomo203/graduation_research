import cv2


def draw_box(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 0), 3, 1)
    cv2.putText(img, 'Tracking', (15, 70), font, 0.5, (0, 0, 255), 2)


if __name__ == '__main__':

    # mjpg-streamerを動作させているPC・ポートを入力
    URL = "http://192.168.10.21:8080/?action=stream"
    cap = cv2.VideoCapture(URL)

    # Create tracker
    tracker = cv2.TrackerKCF_create()
    ret, img = cap.read()

    # Create bbox
    bbox = cv2.selectROI("Tracking", img, False)
    tracker.init(img, bbox)

    font = cv2.FONT_HERSHEY_SIMPLEX

    while True:
        timer = cv2.getTickCount()
        ret, img = cap.read()

        success, bbox = tracker.update(img)
        if success:
            draw_box(img, bbox)
        else:
            cv2.putText(img, 'Tracking Lost', (15, 70), font, 0.5, (0, 0, 255), 2)

        cv2.imshow("Tracking", img)

        key = cv2.waitKey(1)
        if key == 27:  # Esc入力時は終了
            break

    # 終了処理
    cap.release()
    cv2.destroyAllWindows()
