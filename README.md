# [technical-assignment-week-8-faiz](https://github.com/impactbyte/iot-with-python-technical-assignments/tree/main/08-IoT-Software-1)
Repository for technical assignment week 8

# Week 8

## Cara Pengerjaan

Mohon menjawab pertanyaan yang ada dibawah ini, untuk menjawabnya kalian dapat membaca perintah yang telah diberikan dan upload code ke repo github kalian masing-masing, dan namakan repo tersebut sebagai technical-assignment-week-8-NAMAKALIAN. Dan kemudian silahkan copy dan share link repo github kalian dan masukkan kedalam form yang ada di google classroom!

---
## Pertanyaan

> Kalian diminta untuk membuat sebuah backend services untuk menerima sebuah data kecepatan, latitude dan longitude dalam sebuah body json. Dan kalian juga diharapkan untuk menyimpan data tersebut beserta dengan timestampnya.

### Expected Body
```json
{
    "kecepatan": 90,
    "latitude": 6.2088,
    "longitude": 106.8456
}
```

### Expected data yang disimpan dalam database mongodb
* ID transaksi
* kecepatan
* latitude
* longitude
* timestamp

## Jawab

1. Script json berada di file ```body_json.py```
2. Expected body dengan postman
![2022-08-25 21_30_12-Postman](https://user-images.githubusercontent.com/67363618/186693272-d2ac2712-65fd-428f-bb76-174164361617.png)
3. Script menyimpan data mongodb berada di ```db_location.py```
4. Tampilan web MongoDB
![mongodbtampilan](https://user-images.githubusercontent.com/67363618/186693283-ce28300c-9593-457f-949d-fda5ccd174c4.png)

