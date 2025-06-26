# RESTCountries API Test Collection

This repository contains a **Postman Collection** that tests the public [RESTCountries API](https://restcountries.com/#api-endpoints-v3-all). It includes organized test cases for validating country information via:

- `/v3.1/name/{name}`
- `/v3.1/currency/{currency}`
- `/v3.1/lang/{language}`

---

## Purpose

To validate that the RESTCountries API handles:
- Valid and invalid inputs
- Case sensitivity
- Special characters
- Empty and malformed requests
- Proper JSON structure and response codes

---

## Structure

The collection is grouped into three logical folders:

| Folder      | Endpoint Pattern             | Description                          |
|-------------|------------------------------|--------------------------------------|
| `NAME`      | `/v3.1/name/{name}`          | Lookup countries by name             |
| `CURRENCY`  | `/v3.1/currency/{currency}`  | Lookup countries by currency code    |
| `LANGUAGE`  | `/v3.1/lang/{language}`      | Lookup countries by language         |

Each folder includes multiple test cases using:
- Valid examples (`canada`, `usd`, `english`)
- Edge cases and invalid data (`xyz`, `12345`, empty input)
- Test scripts for status code and basic content validation

---

## ▶How to Use

1. Download the Postman collection JSON file from this repo.
2. Open [Postman](https://www.postman.com/)
3. Click **Import**
4. Upload the `.json` file
5. Explore the folders and run the test cases using **Collection Runner**

---

## File Included

- `RESTCountries_API_Test_Collection.json`

This single file includes all test cases and organized folders with:
- Descriptive request names
- Test scripts validating status codes and response contents

---

## Author

**Dandy E. Purwanto**  
Manual QA Engineer  
Tools used: Postman v10.x, RESTCountries API

---
