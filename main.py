import cv2
import pigpio
import tb6643kq_driver as motordriver
import hcsr04_driver as sensor


def range_chahger(in_num: float, in_low: float, in_high: float, out_low: float, out_high: float) -> float:
    out_num = ((in_num - in_low) / (in_high - in_low)) * \
        (out_high - out_low) + out_low

    return out_num


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


if __name__ == '__main__':
    pi_address = "192.168.137.125"

    pi = pigpio.pi(pi_address)

    driverL = motordriver.Tb6643kq_driver(pi, 5, 6)
    driverR = motordriver.Tb6643kq_driver(pi, 22, 27)
    distance_sencor = sensor.hcsr04_driver(pi, 23, 24)

    driverL.stop()
    driverR.stop()

    # mjpg-streamerを動作させているPC・ポートを入力
    URL = "http://" + pi_address + ":8080/?action=stream"
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

            cv2.putText(img, F'Tracking {x}',
                        (200, 70), font, 0.5, (0, 0, 255), 2)

            width_high = img.shape[2] / 2
            width_low = -1 * width_high

            turn_speed = range_chahger(x, width_low, width_high, -100, 100)

            if x == "left":
                driverL.drive(turn_speed)
                driverR.drive(-1 * turn_speed)
            elif x == "right":
                driverL.drive(-1 * turn_speed)
                driverR.drive(turn_speed)
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
