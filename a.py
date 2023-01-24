import cv2
import pigpio
import tb6643kq_driver as driver


def draw_box(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 0), 3, 1)

    height, width,  = img.shape[:2]
    if x + w / 2 < (width / 2) - 50:
        str = "left"
    elif x + w / 2 > (width / 2) + 50:
        str = "right"
    else:
        str = "mid"

    cv2.putText(img, F'Tracking {x} {str}',
                (15, 70), font, 0.5, (0, 0, 255), 2)

    return str


if __name__ == '__main__':

    pi = pigpio.pi("192.168.10.109")

    driverL = driver.Tb6643kq_driver(pi, 5, 6)
    driverR = driver.Tb6643kq_driver(pi, 22, 27)

    driverL.stop()
    driverR.stop()

    # mjpg-streamerを動作させているPC・ポートを入力
    URL = "http://192.168.10.109:8080/?action=stream"
    cap = cv2.VideoCapture(URL)

    # Create tracker
    tracker = cv2.TrackerKCF_create()

    while True:
        ret, img = cap.read()

        cv2.imshow("Tracking", img)

        key = cv2.waitKey(1)
        if key == 32:  # スペース入力でトラッキング対象選択
            break

    # Create bbox
    bbox = cv2.selectROI("Tracking", img, False)
    tracker.init(img, bbox)

    font = cv2.FONT_HERSHEY_SIMPLEX

    while True:
        timer = cv2.getTickCount()
        ret, img = cap.read()

        success, bbox = tracker.update(img)
        if success:
            x = draw_box(img, bbox)

            if x == "left":
                driverL.drive(60)
                driverR.drive(-60)
            elif x == "right":
                driverL.drive(-60)
                driverR.drive(60)
            else:
                driverL.stop()
                driverR.stop()

        else:
            cv2.putText(img, 'Tracking Lost', (15, 70),
                        font, 0.5, (0, 0, 255), 2)

        cv2.imshow("Tracking", img)

        key = cv2.waitKey(1)
        if key == 27:  # Esc入力時は終了
            driverL.stop()
            driverR.stop()
            break

    # 終了処理
    cap.release()
    cv2.destroyAllWindows()
