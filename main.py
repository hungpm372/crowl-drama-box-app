import re

def extract_https_urls(input_file, output_file):
    with open(input_file, 'rb') as file:  # Mở file ở chế độ đọc nhị phân 'rb'
        byte_data = file.read()  # Đọc toàn bộ dữ liệu từ file
    
        # Giải mã dữ liệu từ byte thành chuỗi Unicode
        decoded_str = byte_data.decode('utf-16le')
        
        # Tìm các URL HTTPS bằng regex
        pattern = r'https://\S+'
        urls = re.findall(pattern, decoded_str)
        
        # Lấy các URL duy nhất theo thứ tự xuất hiện
        unique_urls = []
        seen_urls = set()  # Tập hợp để kiểm tra các URL đã xuất hiện
        
        for url in urls:
            if url not in seen_urls:
                seen_urls.add(url)
                unique_urls.append(url)
        
        # Ghi các URL vào file mới
        with open(output_file, 'w') as out_file:
            for url in unique_urls:
                out_file.write(url + "\n")
        
        print(f"Đã ghi {len(unique_urls)} URL duy nhất vào file: {output_file}")

# Thử chạy lại hàm để xem kết quả
input_file = 'all_logfile.txt'
output_file = 'D:/Source/anndroid/out_put.txt'

extract_https_urls(input_file, output_file)
