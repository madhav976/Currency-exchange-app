# 💱 Currency Exchange Centre

A simple command-line Python application that converts currencies in real time using the **ExchangeRate API**. The application also stores conversion history locally, allowing users to view or clear previous conversions.

---

## ✨ Features

* 💱 Convert between supported world currencies
* 🌍 Fetch real-time exchange rates from an online API
* 📝 Save every conversion to a local history file
* 📖 View previous conversions
* 🗑️ Clear conversion history
* ⚠️ Basic input validation for numeric amounts
* 🖥️ Clean, menu-driven command-line interface

---

## 🛠️ Technologies Used

* Python 3
* Requests
* python-dotenv
* ExchangeRate API

---

## 📂 Project Structure

```text
Currency-Exchange-Centre/
│
├── main.py
├── .env
├── exchange_rate.txt
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Currency-Exchange-Centre.git

cd Currency-Exchange-Centre
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Create a `.env` file

```env
API_KEY=your_exchange_rate_api_key
```

---

## ▶️ Run the Application

```bash
python main.py
```

---

## 💻 Example

```text
===== CURRENCY EXCHANGE CENTRE =====

1. Exchange Currencies
2. View History
3. Clear History
4. Exit

Enter your choice: 1

Enter the base currency (e.g., USD): USD
Enter the target currency (e.g., INR): INR
Enter the amount to convert: 100

100 USD is equal to 8574.00 INR at the current exchange rate of 85.74.
```

---

## 📝 Conversion History

Every successful conversion is automatically saved to:

```text
exchange_rate.txt
```

Example:

```text
100 USD = 8574.00 INR at rate 85.74

50 EUR = 5752.15 INR at rate 115.04
```

---

## 🌍 Supported Currencies

The application supports all currencies provided by the ExchangeRate API, including:

* USD – United States Dollar
* EUR – Euro
* GBP – Pound Sterling
* INR – Indian Rupee
* JPY – Japanese Yen
* AUD – Australian Dollar
* CAD – Canadian Dollar
* AED – UAE Dirham

...and many more.

---

## 🚀 Future Improvements

* Currency code validation
* Historical exchange rates
* Currency name autocomplete
* Conversion timestamps
* AI-powered currency insights
* GUI version using Tkinter or CustomTkinter
* Web version using Flask or FastAPI
* Favorite currencies
* Currency trend charts
* Reverse conversion option

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Madhav Saini**

If you found this project useful, consider giving it a ⭐ on GitHub!
