import serial

s = serial.Serial('COM3', 115200)

while True:

    data = []
    for i in range(19):
        data.append(s.read())
        data[i] = int.from_bytes(data[i], byteorder='big')
    if (data[0] != 255 or data[1] != 254):
        print("에러")
    pud_1 = "{0:b}".format(data[5]).zfill(8)
    hrt_up = int(pud_1[5:8], 2)
    hrt_up = hrt_up << 8
    hrt_down = data[2]
    hrt = hrt_down + hrt_up
    if data[4] == 2:
        print("분당 심박수 :", data[6])
        print("심박시간격 :", hrt)
    if data[4] == 5:
        print("분당 심박수(평균) :", data[6])