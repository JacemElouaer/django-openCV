import cv2


def get_filtered_image(image, action):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    if action == 'NO_FILTER':
        filtered = img
    elif action == 'COLORIZED':
        filtered = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    elif action == 'GRAYSCALE':
        filtered = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif action == 'BLUERRED':
        height, width = img.shape[:2]
        # print (width, height)
        if width > 500:
            k = (50, 50)
        elif 200 < width <= 500:
            k = (25, 25)
        else:
            k = (10, 10)
        blur = cv2.blur(img, k)
        filtered = cv2.threshold(blur, cv2.COLOR_BGR2GRGB)
    elif action == 'BINARY':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        _, filtered = cv2.threshold(gray, 170, 155, cv2.THRESH_BINARY)
    elif action == 'INVERT':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        v, binary = cv2.threshold(gray, 170, 155, cv2.THRESH_BINARY)
        filtered = cv2.bitwise_not(binary)

    return filtered
