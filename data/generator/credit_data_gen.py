import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Số lượng quan sát
n = 60081

# Tạo mã khách hàng
makhachhang = [f"KH{str(i).zfill(6)}" for i in range(1, n + 1)]

# Tạo dữ liệu FICO score (điểm tín dụng)
fico = np.random.normal(680, 100, n)
fico = np.clip(fico, 300, 850).astype(int)


# Xếp hạng dựa trên FICO
def get_xephang(fico_score):
    if fico_score >= 750:
        return 1
    elif fico_score >= 700:
        return 2
    elif fico_score >= 650:
        return 3
    elif fico_score >= 600:
        return 4
    elif fico_score >= 550:
        return 5
    else:
        return 6


xephang = [get_xephang(score) for score in fico]

# Tạo thu nhập với phân phối log-normal
thunhap = np.random.lognormal(mean=11, sigma=0.5, size=n)
thunhap = np.round(thunhap).astype(int)

# Kinh nghiệm làm việc (0-10 năm)
kinhnghiem = np.random.randint(0, 11, n)

# Tài sản đảm bảo (0-3)
tsdb = np.random.choice([0, 1, 2, 3], size=n, p=[0.3, 0.3, 0.3, 0.1])

# Xác minh KYC (0-2)
xacminh = np.random.choice([0, 1, 2], size=n, p=[0.6, 0.3, 0.1])

# Mục đích vay (0-12)
mucdich = np.random.choice(
    range(13),
    size=n,
    p=[0.1, 0.15, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.1, 0.05, 0.05],
)

# Địa phương (50 bang)
states = [
    "AL",
    "AK",
    "AZ",
    "AR",
    "CA",
    "CO",
    "CT",
    "DE",
    "FL",
    "GA",
    "HI",
    "ID",
    "IL",
    "IN",
    "IA",
    "KS",
    "KY",
    "LA",
    "ME",
    "MD",
    "MA",
    "MI",
    "MN",
    "MS",
    "MO",
    "MT",
    "NE",
    "NV",
    "NH",
    "NJ",
    "NM",
    "NY",
    "NC",
    "ND",
    "OH",
    "OK",
    "OR",
    "PA",
    "RI",
    "SC",
    "SD",
    "TN",
    "TX",
    "UT",
    "VT",
    "VA",
    "WA",
    "WV",
    "WI",
    "WY",
]
diaphuong = np.random.choice(states, size=n)

# Số tài khoản (1-10)
sotk = np.random.randint(1, 11, n)

# Số tiền vay (dựa trên thu nhập và điểm tín dụng)
tienvay = np.round(thunhap * np.random.uniform(0.5, 2.5, n) * (fico / 700))
tienvay = np.clip(tienvay, 1000, 1000000)


# Lãi suất (dựa trên điểm tín dụng và xếp hạng)
def get_interest_rate(fico_score, rank):
    base_rate = 10
    fico_adjustment = (750 - fico_score) / 100
    rank_adjustment = rank - 1
    rate = base_rate + fico_adjustment + rank_adjustment
    return np.clip(rate, 5, 25)


laisuat = np.array([get_interest_rate(f, r) for f, r in zip(fico, xephang)])


# Khoản trả góp (PMT calculation)
def calculate_pmt(loan_amount, interest_rate, term_years=3):
    rate = interest_rate / 100 / 12
    term_months = term_years * 12
    pmt = (
        loan_amount
        * (rate * (1 + rate) ** term_months)
        / ((1 + rate) ** term_months - 1)
    )
    return round(pmt, 2)


khoantragop = np.array([calculate_pmt(p, r) for p, r in zip(tienvay, laisuat)])


# Xác định trạng thái vỡ nợ dựa trên các yếu tố rủi ro - đã điều chỉnh để có tỷ lệ vỡ nợ ~15%
def calculate_default_probability(row):
    # Giảm base probability xuống
    base_prob = 0.02

    # Điều chỉnh theo FICO - giảm tác động
    fico_adj = (700 - row["fico"]) / 2000

    # Điều chỉnh theo thu nhập - giảm tác động
    income_adj = np.log(100000 / row["thunhap"]) / 20 if row["thunhap"] > 0 else 0.05

    # Điều chỉnh theo tỷ lệ trả góp/thu nhập
    pti_ratio = (row["khoantragop"] * 12) / row["thunhap"]
    pti_adj = pti_ratio * 0.2

    # Các điều chỉnh khác - giảm tác động
    other_adj = (
        0.01 * (row["xephang"] - 1)  # Giảm tác động của xếp hạng
        + -0.005 * row["kinhnghiem"]  # Giảm tác động của kinh nghiệm
        + 0.01 * row["xacminh"]  # Giảm tác động của xác minh
        + -0.005 * row["sotk"]  # Giảm tác động của số tài khoản
    )

    # Thêm điều chỉnh theo tài sản đảm bảo
    tsdb_adj = -0.01 if row["tsdb"] in [0, 1] else 0.01

    prob = base_prob + fico_adj + income_adj + pti_adj + other_adj + tsdb_adj
    return np.clip(prob, 0, 1)


# Tạo DataFrame
df = pd.DataFrame(
    {
        "makhachhang": makhachhang,
        "fico": fico,
        "xephang": xephang,
        "thunhap": thunhap,
        "kinhnghiem": kinhnghiem,
        "tsdb": tsdb,
        "xacminh": xacminh,
        "mucdich": mucdich,
        "diaphuong": diaphuong,
        "sotk": sotk,
        "tienvay": tienvay,
        "laisuat": laisuat,
        "khoantragop": khoantragop,
    }
)

# Tính xác suất vỡ nợ và tạo biến trạng thái
default_probs = df.apply(calculate_default_probability, axis=1)
df["trangthai"] = np.random.binomial(1, default_probs)

# Làm tròn các giá trị số
df["tienvay"] = df["tienvay"].round(2)
df["laisuat"] = df["laisuat"].round(2)
df["khoantragop"] = df["khoantragop"].round(2)
df["thunhap"] = df["thunhap"].round(2)

print("Tỷ lệ vỡ nợ:", df["trangthai"].mean())
print("\nPhân phối các biến chính:")
print("\nThống kê mô tả:")
print(df.describe())
print("\nMẫu 5 quan sát đầu tiên:")
print(df.head())

# Xuất dữ liệu ra file CSV
df.to_csv("./data/raw/credit_risk_data.csv", index=False)
