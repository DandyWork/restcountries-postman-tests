# RESTCountries API Test Collection

This repository contains a **Postman Collection** for testing the public [RESTCountries API](https://restcountries.com/#api-endpoints-v3-all). The collection is designed to validate responses and behaviors across the following endpoints:

- `/v3.1/name/{name}`
- `/v3.1/currency/{currency}`
- `/v3.1/lang/{language}`

---

##  Purpose

To provide a comprehensive suite of test cases that verify:

- API response status codes
- Input validation (valid/invalid formats)
- JSON structure consistency
- Country-level data lookup based on name, currency, and language

---

## Collection Structure

The Postman collection is divided into three folders:

| Folder      | Endpoint Pattern             | Description                          |
|-------------|------------------------------|--------------------------------------|
| `NAME`      | `/v3.1/name/{name}`          | Test country lookups by name         |
| `CURRENCY`  | `/v3.1/currency/{currency}`  | Test country lookups by currency     |
| `LANGUAGE`  | `/v3.1/lang/{language}`      | Test country lookups by language     |

Each folder includes 6–8 individual test cases covering:
- Valid input
- Invalid input
- Case sensitivity
- Special characters
- Empty or malformed input

---

## ▶How to Use

1. Open [Postman](https://www.postman.com/)
2. Click **Import**
3. Upload one of the provided `.json` files (or all)
4. Run each folder using **Collection Runner**
5. Review tests and responses in Postman

---

## Files Included

- `RESTCountries_NAME_Postman_Collection.json`
- `RESTCountries_CURRENCY_Postman_Collection.json`
- `RESTCountries_LANGUAGE_Postman_Collection.json`

Each file contains:
- Test case names with clear ID and description
- Test scripts to check status code and response body

---

## Author

**Dandy E. Purwanto**  
Manual QA Engineer  
Tools used: Postman v10.x, RESTCountries API

---
