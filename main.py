import cv2
import time
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

    width = img.shape[1]
    if x + w / 2 < (width / 2) - 50:
        str = "left"
    elif x + w / 2 > (width / 2) + 50:
        str = "right"
    else:
        str = "mid"

    cv2.putText(img, F'Tracking {x} {str}',
                (15, 70), font, 0.5, (0, 0, 255), 2)

    return (x + w / 2)


if __name__ == '__main__':
    pi_address = "192.168.137.125"

    init_distance = 0

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
    # tracker = cv2.TrackerCSRT_create()

    while True:
        ret, img = cap.read()

        cv2.imshow("Tracking", img)

        key = cv2.waitKey(1)
        if key == 32:  # スペース入力でトラッキング対象選択
            break

    # Create bbox
    bbox = cv2.selectROI("Tracking", img, False)
    tracker.init(img, bbox)

    init_distance = distance_sencor.get_distance()
    while init_distance == 0:
        init_distance = distance_sencor.get_distance()
        if init_distance < 2 and init_distance > 400:
            distance = 0

    font = cv2.FONT_HERSHEY_SIMPLEX

    while True:
        timer = cv2.getTickCount()
        ret, img = cap.read()

        success, bbox = tracker.update(img)
        if success:
            x = draw_box(img, bbox)

            width_high = img.shape[1]
            width_low = 0

            turn_speed = range_chahger(x, width_low, width_high, -80, 80)

            cv2.putText(img, F'{turn_speed}',
                        (200, 70), font, 0.5, (0, 0, 255), 2)

            distance = distance_sencor.get_distance()

            if distance < 2 and distance > 400:
                distance = 0

            print(init_distance, end=", ")
            print(distance)

            if distance > init_distance + 10:
                driverL.drive(-10)
                driverR.drive(-10)
            elif distance < init_distance - 10:
                driverL.drive(10)
                driverR.drive(10)
            else:
                driverL.stop()
                driverR.stop()

            # if turn_speed > 5:
            #     driverL.drive(turn_speed)
            #     driverR.drive(-turn_speed)
            # elif turn_speed < -5:
            #     driverL.drive(turn_speed)
            #     driverR.drive(-turn_speed)
            # else:
            #     driverL.stop()
            #     driverR.stop()

            # time.sleep(0.01)

            # driverL.stop()
            # driverR.stop()

        else:
            cv2.putText(img, 'Tracking Lost', (15, 70),
                        font, 0.5, (0, 0, 255), 2)

            distance = distance_sencor.get_distance()

            if distance < 2 and distance > 400:
                distance = 0

            print(init_distance, end=", ")
            print(distance)

            if distance > init_distance + 5:
                driverL.drive(-50)
                driverR.drive(-50)
            elif distance < init_distance - 5:
                driverL.drive(50)
                driverR.drive(50)
            else:
                driverL.stop()
                driverR.stop()

        cv2.imshow("Tracking", img)

        time.sleep(0.02)

        key = cv2.waitKey(1)
        if key == 27:  # Esc入力時は終了
            driverL.stop()
            driverR.stop()
            break

    # 終了処理
    cap.release()
    cv2.destroyAllWindows()
