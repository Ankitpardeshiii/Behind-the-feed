# 📊 Behind the Feed

Behind the Feed is a Python-based Instagram data analysis project that extracts user information from raw Instagram profile data and generates meaningful insights such as follower statistics, category distribution, and top accounts.

## 🚀 Features

- Parse raw Instagram profile data
- Convert raw text into structured JSON
- Find the account with the highest followers
- Find the account with the highest following
- Calculate average followers and following
- Count unique profile categories
- Display category distribution
- Show Top 10 accounts by followers
- Show Top 10 accounts by following

---

## 📂 Project Structure

```
Behind-the-Feed/
│
├── data/
│   ├── initialdata.txt
│   └── Punedata.json
│
├── src/
│   ├── parser.py
│   ├── converter.py
│   ├── analyzer.py
│   ├── statistics.py
│   └── __init__.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Ankitpardeshiii/Behind-the-Feed.git
```

Move into the project directory

```bash
cd Behind-the-Feed
```

(Optional) Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

```bash
python main.py
```

---

## 📊 Example Output

```
============================================================
INSTAGRAM DATA ANALYSIS
============================================================

Total Users          : 500
Unique Categories    : 18
Average Followers    : 13,524.43
Average Following    : 425.18

Most Followed Account
------------------------------------------------------------
Username   : startuphub_blr
Followers  : 45,000
Category   : Media

Top 10 Accounts by Followers

1. startuphub_blr
2. tech_updates
3. coding_world
...
```

---

## 🛠 Technologies Used

- Python 3
- JSON
- Standard Python Libraries

---

## 📁 Modules

### parser.py
Parses each Instagram profile into a Python dictionary.

### converter.py
Reads the raw dataset and converts it into structured JSON.

### analyzer.py
Performs account-level analysis such as identifying the top followed accounts.

### statistics.py
Computes dataset-wide statistics including category counts and average followers.

### main.py
Runs the complete analysis pipeline.

---

## 📈 Future Improvements

- Streamlit Dashboard
- Interactive Charts
- CSV Export
- Search Profiles
- Profile Comparison
- Sentiment Analysis on Bio
- Word Cloud Visualization
- Follower Distribution Graphs

---

## 👨‍💻 Author

**Ankit Pardeshi**

Portfolio: https://ankitpardeshi.xyz
---

⭐ If you found this project useful, consider giving it a star!
