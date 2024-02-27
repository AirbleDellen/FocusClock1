import time
import os

def countdown_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print(f"Time left: {timer_display}", end='\r')
        time.sleep(1)
        seconds -= 1

    print("\nTime's up! Stay focused!")

def main():
    try:
        minutes = int(input("请输入保持专注的分钟数 单位：分钟: "))
        countdown_timer(minutes)
    except ValueError:
        print("无效的输入，请输入有效数字")

if __name__ == "__main__":
    main()
