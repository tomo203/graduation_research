import cv2


if __name__ == '__main__':

    # mjpg-streamerを動作させているPC・ポートを入力
    URL = "http://192.168.10.21:8080/?action=stream"
    cap = cv2.VideoCapture(URL)

    while True:
        ret, img = cap.read()

        cv2.imshow("Tracking", img)

        key = cv2.waitKey(1)
        if key == 27:  # Esc入力時は終了
            break

    # 終了処理
    cap.release()
    cv2.destroyAllWindows()
