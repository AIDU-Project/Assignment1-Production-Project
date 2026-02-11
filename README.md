BÀI TẬP TUẦN NÀY (08/02 - 15/02): <br>
Từ notebook training Random Forest <br>
Format lại thành: source follow theo quy trình production level (buổi học tuần này), đảm bảo chuẩn cấu trúc và serving API để call model và trả lại kết quả , sau đó upload github (branch riêng, follow conventional commit)

Yêu cầu 1: tự tạo một branch mới, KHÔNG COMMIT VÀO MAIN BRANCH.

Có thể format lại theo structure mẫu như sau: <br>
project-root/ <br>
│ <br>
├── data/                  # Folder chứa datasets <br>
├── notebooks/             # Jupyter notebooks <br>
├── src/ <br>
│   ├── data/              # Data loading và preprocessing <br>
│   ├── features/          # Feature engineering <br>
│   ├── models/            # Model training và evaluation <br>
│   ├── api/               # FastAPI <br>
│   └── utils/             # Các hàm call ngoài <br>
├── models/                # Lưu file model để clone ra trên các trang notebooks <br>
├── tests/                 # Viết unit test <br>
├── configs/               # File config (YAML/JSON) <br>
├── requirements.txt       # Các thư viện cần cài/ đầu mục cần setup trên Python <br>
├── Dockerfile             # Docker <br>
├── .github/workflows/     # Tựa tựa cái này <br>
└── README.md              # File hướng dẫn
