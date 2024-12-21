import threading
import time
from datetime import datetime
import random

# Hàm thực thi cho mỗi luồng (Google, Yahoo, Facebook)
def web_thread(name):
    print(f"Starting {name}")
    
    # Mỗi luồng sẽ in 5 lần
    for _ in range(5):
        current_time = datetime.now().strftime("%b %d %H:%M:%S %Y")
        print(f"{name}: Web {current_time}")
        time.sleep(random.randint(1, 3))  # Tạm dừng ngẫu nhiên từ 1 đến 3 giây

    print(f"Exiting {name}")

# Hàm chạy chương trình chính
def main():
    print("Starting Main Thread")
    
    # Tạo các luồng cho Google, Yahoo, Facebook
    google_thread = threading.Thread(target=web_thread, args=("Google",))
    yahoo_thread = threading.Thread(target=web_thread, args=("Yahoo",))
    facebook_thread = threading.Thread(target=web_thread, args=("Facebook",))

    # Bắt đầu các luồng
    google_thread.start()
    yahoo_thread.start()
    facebook_thread.start()

    # Chờ các luồng hoàn thành
    google_thread.join()
    yahoo_thread.join()
    facebook_thread.join()

    print("Exiting Main Thread")

# Thực thi chương trình
if __name__ == "__main__":
    main()
