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

## 🌍 Supported Currencies

This application supports **160+ currencies** provided by the ExchangeRate API.

Click below to view the complete list.

<details>
<summary><strong>📋 View All Supported Currencies</strong></summary>

| Code | Currency                      | Country/Region                           |
| ---- | ----------------------------- | ---------------------------------------- |
| AED  | UAE Dirham                    | United Arab Emirates                     |
| AFN  | Afghan Afghani                | Afghanistan                              |
| ALL  | Albanian Lek                  | Albania                                  |
| AMD  | Armenian Dram                 | Armenia                                  |
| ANG  | Netherlands Antillian Guilder | Netherlands Antilles                     |
| AOA  | Angolan Kwanza                | Angola                                   |
| ARS  | Argentine Peso                | Argentina                                |
| AUD  | Australian Dollar             | Australia                                |
| AWG  | Aruban Florin                 | Aruba                                    |
| AZN  | Azerbaijani Manat             | Azerbaijan                               |
| BAM  | Bosnia and Herzegovina Mark   | Bosnia and Herzegovina                   |
| BBD  | Barbados Dollar               | Barbados                                 |
| BDT  | Bangladeshi Taka              | Bangladesh                               |
| BGN  | Bulgarian Lev                 | Bulgaria                                 |
| BHD  | Bahraini Dinar                | Bahrain                                  |
| BIF  | Burundian Franc               | Burundi                                  |
| BMD  | Bermudian Dollar              | Bermuda                                  |
| BND  | Brunei Dollar                 | Brunei                                   |
| BOB  | Bolivian Boliviano            | Bolivia                                  |
| BRL  | Brazilian Real                | Brazil                                   |
| BSD  | Bahamian Dollar               | Bahamas                                  |
| BTN  | Bhutanese Ngultrum            | Bhutan                                   |
| BWP  | Botswana Pula                 | Botswana                                 |
| BYN  | Belarusian Ruble              | Belarus                                  |
| BZD  | Belize Dollar                 | Belize                                   |
| CAD  | Canadian Dollar               | Canada                                   |
| CDF  | Congolese Franc               | Democratic Republic of the Congo         |
| CHF  | Swiss Franc                   | Switzerland                              |
| CLF  | Chilean Unidad de Fomento     | Chile                                    |
| CLP  | Chilean Peso                  | Chile                                    |
| CNH  | Offshore Chinese Renminbi     | China                                    |
| CNY  | Chinese Renminbi              | China                                    |
| COP  | Colombian Peso                | Colombia                                 |
| CRC  | Costa Rican Colon             | Costa Rica                               |
| CUP  | Cuban Peso                    | Cuba                                     |
| CVE  | Cape Verdean Escudo           | Cape Verde                               |
| CZK  | Czech Koruna                  | Czech Republic                           |
| DJF  | Djiboutian Franc              | Djibouti                                 |
| DKK  | Danish Krone                  | Denmark                                  |
| DOP  | Dominican Peso                | Dominican Republic                       |
| DZD  | Algerian Dinar                | Algeria                                  |
| EGP  | Egyptian Pound                | Egypt                                    |
| ERN  | Eritrean Nakfa                | Eritrea                                  |
| ETB  | Ethiopian Birr                | Ethiopia                                 |
| EUR  | Euro                          | European Union                           |
| FJD  | Fiji Dollar                   | Fiji                                     |
| FKP  | Falkland Islands Pound        | Falkland Islands                         |
| FOK  | Faroese Króna                 | Faroe Islands                            |
| GBP  | Pound Sterling                | United Kingdom                           |
| GEL  | Georgian Lari                 | Georgia                                  |
| GGP  | Guernsey Pound                | Guernsey                                 |
| GHS  | Ghanaian Cedi                 | Ghana                                    |
| GIP  | Gibraltar Pound               | Gibraltar                                |
| GMD  | Gambian Dalasi                | The Gambia                               |
| GNF  | Guinean Franc                 | Guinea                                   |
| GTQ  | Guatemalan Quetzal            | Guatemala                                |
| GYD  | Guyanese Dollar               | Guyana                                   |
| HKD  | Hong Kong Dollar              | Hong Kong                                |
| HNL  | Honduran Lempira              | Honduras                                 |
| HRK  | Croatian Kuna                 | Croatia                                  |
| HTG  | Haitian Gourde                | Haiti                                    |
| HUF  | Hungarian Forint              | Hungary                                  |
| IDR  | Indonesian Rupiah             | Indonesia                                |
| ILS  | Israeli New Shekel            | Israel                                   |
| IMP  | Manx Pound                    | Isle of Man                              |
| INR  | Indian Rupee                  | India                                    |
| IQD  | Iraqi Dinar                   | Iraq                                     |
| ISK  | Icelandic Króna               | Iceland                                  |
| JEP  | Jersey Pound                  | Jersey                                   |
| JMD  | Jamaican Dollar               | Jamaica                                  |
| JOD  | Jordanian Dinar               | Jordan                                   |
| JPY  | Japanese Yen                  | Japan                                    |
| KES  | Kenyan Shilling               | Kenya                                    |
| KGS  | Kyrgyzstani Som               | Kyrgyzstan                               |
| KHR  | Cambodian Riel                | Cambodia                                 |
| KID  | Kiribati Dollar               | Kiribati                                 |
| KMF  | Comorian Franc                | Comoros                                  |
| KRW  | South Korean Won              | South Korea                              |
| KWD  | Kuwaiti Dinar                 | Kuwait                                   |
| KYD  | Cayman Islands Dollar         | Cayman Islands                           |
| KZT  | Kazakhstani Tenge             | Kazakhstan                               |
| LAK  | Lao Kip                       | Laos                                     |
| LBP  | Lebanese Pound                | Lebanon                                  |
| LKR  | Sri Lanka Rupee               | Sri Lanka                                |
| LRD  | Liberian Dollar               | Liberia                                  |
| LSL  | Lesotho Loti                  | Lesotho                                  |
| LYD  | Libyan Dinar                  | Libya                                    |
| MAD  | Moroccan Dirham               | Morocco                                  |
| MDL  | Moldovan Leu                  | Moldova                                  |
| MGA  | Malagasy Ariary               | Madagascar                               |
| MKD  | Macedonian Denar              | North Macedonia                          |
| MMK  | Burmese Kyat                  | Myanmar                                  |
| MNT  | Mongolian Tögrög              | Mongolia                                 |
| MOP  | Macanese Pataca               | Macau                                    |
| MRU  | Mauritanian Ouguiya           | Mauritania                               |
| MUR  | Mauritian Rupee               | Mauritius                                |
| MVR  | Maldivian Rufiyaa             | Maldives                                 |
| MWK  | Malawian Kwacha               | Malawi                                   |
| MXN  | Mexican Peso                  | Mexico                                   |
| MYR  | Malaysian Ringgit             | Malaysia                                 |
| MZN  | Mozambican Metical            | Mozambique                               |
| NAD  | Namibian Dollar               | Namibia                                  |
| NGN  | Nigerian Naira                | Nigeria                                  |
| NIO  | Nicaraguan Córdoba            | Nicaragua                                |
| NOK  | Norwegian Krone               | Norway                                   |
| NPR  | Nepalese Rupee                | Nepal                                    |
| NZD  | New Zealand Dollar            | New Zealand                              |
| OMR  | Omani Rial                    | Oman                                     |
| PAB  | Panamanian Balboa             | Panama                                   |
| PEN  | Peruvian Sol                  | Peru                                     |
| PGK  | Papua New Guinean Kina        | Papua New Guinea                         |
| PHP  | Philippine Peso               | Philippines                              |
| PKR  | Pakistani Rupee               | Pakistan                                 |
| PLN  | Polish Złoty                  | Poland                                   |
| PYG  | Paraguayan Guaraní            | Paraguay                                 |
| QAR  | Qatari Riyal                  | Qatar                                    |
| RON  | Romanian Leu                  | Romania                                  |
| RSD  | Serbian Dinar                 | Serbia                                   |
| RUB  | Russian Ruble                 | Russia                                   |
| RWF  | Rwandan Franc                 | Rwanda                                   |
| SAR  | Saudi Riyal                   | Saudi Arabia                             |
| SBD  | Solomon Islands Dollar        | Solomon Islands                          |
| SCR  | Seychellois Rupee             | Seychelles                               |
| SDG  | Sudanese Pound                | Sudan                                    |
| SEK  | Swedish Krona                 | Sweden                                   |
| SGD  | Singapore Dollar              | Singapore                                |
| SHP  | Saint Helena Pound            | Saint Helena                             |
| SLE  | Sierra Leonean Leone          | Sierra Leone                             |
| SOS  | Somali Shilling               | Somalia                                  |
| SRD  | Surinamese Dollar             | Suriname                                 |
| SSP  | South Sudanese Pound          | South Sudan                              |
| STN  | São Tomé and Príncipe Dobra   | São Tomé and Príncipe                    |
| SYP  | Syrian Pound                  | Syria                                    |
| SZL  | Eswatini Lilangeni            | Eswatini                                 |
| THB  | Thai Baht                     | Thailand                                 |
| TJS  | Tajikistani Somoni            | Tajikistan                               |
| TMT  | Turkmenistan Manat            | Turkmenistan                             |
| TND  | Tunisian Dinar                | Tunisia                                  |
| TOP  | Tongan Paʻanga                | Tonga                                    |
| TRY  | Turkish Lira                  | Turkey                                   |
| TTD  | Trinidad and Tobago Dollar    | Trinidad and Tobago                      |
| TVD  | Tuvaluan Dollar               | Tuvalu                                   |
| TWD  | New Taiwan Dollar             | Taiwan                                   |
| TZS  | Tanzanian Shilling            | Tanzania                                 |
| UAH  | Ukrainian Hryvnia             | Ukraine                                  |
| UGX  | Ugandan Shilling              | Uganda                                   |
| USD  | United States Dollar          | United States                            |
| UYU  | Uruguayan Peso                | Uruguay                                  |
| UZS  | Uzbekistani So'm              | Uzbekistan                               |
| VES  | Venezuelan Bolívar Soberano   | Venezuela                                |
| VND  | Vietnamese Đồng               | Vietnam                                  |
| VUV  | Vanuatu Vatu                  | Vanuatu                                  |
| WST  | Samoan Tālā                   | Samoa                                    |
| XAF  | Central African CFA Franc     | CEMAC                                    |
| XCD  | East Caribbean Dollar         | Organisation of Eastern Caribbean States |
| XDR  | Special Drawing Rights        | International Monetary Fund              |
| XOF  | West African CFA Franc        | CFA                                      |
| XPF  | CFP Franc                     | Collectivités d'Outre-Mer                |
| YER  | Yemeni Rial                   | Yemen                                    |
| ZAR  | South African Rand            | South Africa                             |
| ZMW  | Zambian Kwacha                | Zambia                                   |
| ZWL  | Zimbabwean Dollar             | Zimbabwe                                 |

</details>


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
#   C u r r e n c y - e x c h a n g e - a p p  
 