import socket

# Tạo socket
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Khai báo thông tin máy chủ
host= socket.gethostname()
port= 2448

# Gán địa chỉ và cổng cho socket
s.bind((host, port))
# Lắng nghe kết nối từ client
s.listen()
print(f"Listening in port {port}...")
while True:
    # Chấp nhận kết nối từ client
    c, addr =s.accept()
    print(f"Accept connect from ",addr)
    data = c.recv(2048)  # Nhận dữ liệu từ client
    
    if not data:
        break  # Ngắt kết nối nếu không nhận được dữ liệu

    received_msg = data.decode('utf-8')
    print(f"Nhận từ client: {received_msg}")
    # Chuyển chuỗi thành chữ hoa
    uppercase_msg = received_msg.upper()

    # Gửi chuỗi đã được định dạng trở lại cho client
    c.sendall(uppercase_msg.encode('utf-8'))
    # output= "Thanks for connect"
  
     # Đóng kết nối với client
    c.close()
# Đóng socket của máy chủ
s.close()
