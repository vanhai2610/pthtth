import socket

# Tạo socket
c= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Khai báo thông tin máy chủ
host= socket.gethostname()
port=2448

# Kết nối tới máy chủ
c.connect((host,port))
while True:
    msg = input("Nhập chuỗi để gửi đến máy chủ (nhập 'exit' để thoát): ")
    
    if msg.lower() == 'exit':
        break

    # Gửi dữ liệu đến máy chủ
    c.sendall(msg.encode('utf-8'))

    # Nhận dữ liệu từ máy chủ và hiển thị lên màn hình
    data= c.recv(2048)
    received_msg=data.decode('utf-8')

    print(f"Received from server: {received_msg}")

# Đóng kết nối với máy chủ
c.close()