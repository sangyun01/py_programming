# 8주차 객체와 클래스

# Lab: TV 클래스 정의

class TVsettings:
    def __init__(self, channel, volume, ON):
        self.setChannel = channel
        self.getvolume = volume
        self.turnon = ON

    def show(self):
        print(f"{self.setChannel} {self.getvolume} {self.turnon}")


samsung = TVsettings(11, 20, True)
samsung.show()

#dkdkdkdk