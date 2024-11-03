# Made by Claude Sonnet 3.5

Tôi muốn tạo ra một bộ data credit risk, gồm có 14 biến và khoảng 60081 quan sát:
* `makhachhang`: mã định danh khách hàng, ngẫu nhiên theo thứ tự
* `trangthai`: khách không trả nợ đúng cam kết (1), còn lại 0
* `tienvay`: số tiền khách được duyệt vay, đơn vị USD
* `laisuat`: lãi suất áp dụng cho khoản vay, đơn vị %
* `khoantragop`: số tiền gốc và lãi trả định kì, đơn gì USD (lưu ý nó liên quan đến tienvay, laisuat)
* `xephang`: xếp hạng tín dụng của khách hàng, 6 bậc, theo tín nhiệm giảm dần
* `kinhnghiem`: kinh nghiệm làm việc cho tới hiện tại của cv gần nhất, từ 0- 10
* `tsdb`: thể hiện loại tài sản đảm bảo cho khoản vay, 4 nhóm từ 0 đến 3 - (1 - Sở hữu nhà, 1-Nhà đang được thế chấp, 2-Thuê, 3-khác)
* `thunhap`: thu nhập năm của khách, tính theo usd
* `xacminh`: cung cấp tính xác thực kyc của khách hàng (0 - đã xác minh; 1 - đáng tinh cậy; 2- chưa xác minh) 
* `mucdich`: mục đích vay (0 - mua ô tô, 1- trả nợ thẻ tín dụng, 2-gộp nợ, trả khoản nợ khác, 3-sửa chữa cải tạo nhà cửa, 4-mua nhà mới, 5-mua thiết bị điện tử, 6-chi trả y tế, điều trị bệnh, 7-chuyển nhà, di dời, 8-đám cưới, 9-đầu tư vào năng lượng tái tạo,10-khởi nghiệp kinh doanh nhỏ, 11-du lịch nghỉ dưỡng, 12-khác)
* `diaphuong`: địa phương lưu trú và thực hiện khoản vay, 50 lớp gồm 50 bang của hoa kì
* `fico`: điểm tín dụng, tương tự xephang nhưng là một con số từ 200-800 điểm, cụ thể hơn
* `sotk`: số lượng tài khoản khách hàng duy trì trong hệ thống tài chính

Hãy xây dựng dư liệu theo hiểu biết của bạn về các đặc tính - đi kèm với mức rủi ro một cách hợp lí.