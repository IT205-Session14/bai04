student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]

def calculate_average(st):
    return (st["math"] + st["physics"] + st["chemistry"]) / 3

def get_rank(average_score):
    if average_score >= 8.0:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

def validate_score(score_input):
    if score_input.replace(".", "", 1).isdigit():
        score = float(score_input)
        if 0 <= score <= 10:
            return score
        else:
            print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")
            return None
    else:
        print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")
        return None

def find_student_by_id(records, student_id):
    for idx, st in enumerate(records):
        if st["student_id"] == student_id:
            return idx
    return None

def display_grades(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
    else:
        print("--- BẢNG ĐIỂM SINH VIÊN ---")
        for i, st in enumerate(records, start=1):
            avg = calculate_average(st)
            rank = get_rank(avg)
            print(f"{i}. [{st['student_id']}] {st['name']} | Toán: {st['math']} | Lý: {st['physics']} | Hóa: {st['chemistry']} | ĐTB: {avg:.2f} - {rank}")

def update_student_score(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    student_id = input("Nhập mã sinh viên cần cập nhật: ").upper()
    idx = find_student_by_id(records, student_id)
    if idx is None:
        print(f"Không tìm thấy sinh viên mang mã {student_id} trong hệ thống!")
        return

    print("Chọn môn học (1-Toán, 2-Lý, 3-Hóa):")
    choice = input("Lựa chọn: ")

    if choice == "1":
        subject_key = "math"
        subject_name = "Toán"
    elif choice == "2":
        subject_key = "physics"
        subject_name = "Lý"
    elif choice == "3":
        subject_key = "chemistry"
        subject_name = "Hóa"
    else:
        print("Lựa chọn môn học không hợp lệ!")
        return

    new_score = None
    while new_score is None:
        new_score = validate_score(input("Nhập điểm mới: "))

    records[idx][subject_key] = new_score
    print(f">> Đã cập nhật điểm {subject_name} của sinh viên '{records[idx]['name']}' thành {new_score}.")

def generate_report(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total = len(records)
    passed = 0
    for st in records:
        if calculate_average(st) >= 5.0:
            passed += 1
            
    failed = total - passed
    pass_rate = (passed / total) * 100
    fail_rate = (failed / total) * 100

    print("BÁO CÁO HỌC VỤ")
    print(f"Tổng số sinh viên: {total}")
    print(f"Số lượng qua môn (ĐTB >= 5.0): {passed} sinh viên (Chiếm {pass_rate:.2f}%)")
    print(f"Số lượng trượt (ĐTB < 5.0): {failed} sinh viên (Chiếm {fail_rate:.2f}%)")

def find_valedictorian(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    max_score = -1.0
    valedictorian = None

    for st in records:
        avg = calculate_average(st)
        if avg > max_score:
            max_score = avg
            valedictorian = st

    print("VINH DANH THỦ KHOA")
    print(f"Sinh viên: {valedictorian['name']} (Mã: {valedictorian['student_id']})")
    print(f"Điểm Trung Bình: {max_score:.2f}")
    print("Chúc mừng sinh viên đã đạt thành tích xuất sắc nhất khóa!")

def display_menu():
    print("HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY")
    print("1. Xem bảng điểm và học lực")
    print("2. Cập nhật điểm thi sinh viên")
    print("3. Báo cáo thống kê (Đỗ/Trượt)")
    print("4. Tìm sinh viên Thủ khoa")
    print("5. Thoát chương trình")

while True:
    display_menu()
    choice = input("Chọn chức năng (1-5): ").strip()

    match choice:
        case "1":
            display_grades(student_records)
        case "2":
            update_student_score(student_records)
        case "3":
            generate_report(student_records)
        case "4":
            find_valedictorian(student_records)
        case "5":
            print("Thoát chương trình!")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")