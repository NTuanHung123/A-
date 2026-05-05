# 🧭 A* Pathfinding Algorithm (Lab 2)

## 📌 Giới thiệu

Dự án này cài đặt thuật toán **A*** (A-star) để tìm đường đi ngắn nhất trong mê cung (grid 2D).

Thuật toán A* là một trong những thuật toán tìm kiếm tối ưu phổ biến, được sử dụng trong:

* Game (AI tìm đường)
* Robot tự hành
* Bản đồ (Google Maps,...)

---

## 🎯 Mục tiêu

* Hiểu nguyên lý hoạt động của thuật toán A*
* Cài đặt A* bằng Python
* Trực quan hóa đường đi tìm được

---

## 🧠 Nguyên lý thuật toán

A* sử dụng hàm đánh giá:

f(n) = g(n) + h(n)

Trong đó:

* g(n): chi phí từ điểm bắt đầu → node hiện tại
* h(n): heuristic (ước lượng chi phí từ node → đích)
* f(n): tổng chi phí

Thuật toán luôn chọn node có **f(n) nhỏ nhất** để mở rộng.

---

## ⚙️ Cấu trúc thư mục

```
project/
│
├── a_star.py        # File chính chứa thuật toán A*
├── README.md        # File mô tả dự án
```

---

## 🚀 Cách chạy chương trình

### 1. Cài đặt thư viện

```bash
pip install numpy matplotlib
```

### 2. Chạy chương trình

```bash
python a_star.py
```

---

## 🗺️ Mô tả bài toán

* Grid: 20x20
* Giá trị:

  * `0`: đường đi
  * `1`: vật cản
* Điểm bắt đầu: `(0, 0)`
* Điểm đích: `(19, 19)`

Chương trình sẽ:

* Tìm đường đi tối ưu
* In ra console
* Vẽ đường đi bằng matplotlib

---

## 📊 Kết quả

* Thuật toán tìm được đường đi ngắn nhất từ start đến goal
* Tránh được các vật cản
* Hiển thị trực quan đường đi

---

## 🔍 Thuật toán sử dụng

* A* Search
* Heuristic: **Khoảng cách Euclid**

---

## 🔄 Hướng phát triển

* So sánh với BFS, DFS
* Dùng heuristic Manhattan
* Áp dụng cho bản đồ lớn hơn
* Thêm animation chuyển động
