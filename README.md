BÀI TẬP TUẦN NÀY (08/02 - 15/02):
Từ notebook training Random Forest
Format lại thành: source follow theo quy trình production level (buổi học tuần này), đảm bảo chuẩn cấu trúc và serving API để call model và trả lại kết quả , sau đó upload github (branch riêng, follow conventional commit)

Có thể format lại theo structure mẫu như sau:
project-root/
│
├── data/                  # Folder chứa datasets
├── notebooks/             # Jupyter notebooks
├── src/
│   ├── data/              # Data loading và preprocessing
│   ├── features/          # Feature engineering
│   ├── models/            # Model training và evaluation
│   ├── api/               # FastAPI
│   └── utils/             # Các hàm call nggoaif
├── models/                # Lưu file model để clone ra trên các trang notebooks
├── tests/                 # Viết unit test
├── configs/               # File config (YAML/JSON)
├── requirements.txt       # Các thư viện cần cài/ đầu mục cần setup trên Python
├── Dockerfile             # Docker
├── .github/workflows/     # Tựa tựa cái này
└── README.md              # Readme
