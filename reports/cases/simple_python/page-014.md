# simple_python — page 14/14

[Category index](README.md) · [All categories](../README.md) · [Previous](page-013.md)

10 cases. Expand the question/answer and model sections below. Tool calls were scored, not executed.

## simple_python_390

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.155869 | 127 |
| Qwen3.8-27B | 正确 | 2.208542 | 81 |
| gemma-4-26B-A4B-it | 正确 | 0.302063 | 33 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Convert 150 Euros to Canadian dollars.</pre>

### Official accepted answer

<pre>[
  {
    "currency_conversion.convert": {
      "amount": [
        150
      ],
      "from_currency": [
        "EUR",
        "Euros"
      ],
      "to_currency": [
        "CAD",
        "Canadian dollars"
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>[
  {
    "name": "currency_conversion_convert",
    "arguments": {
      "amount": 150,
      "from_currency": "EUR",
      "to_currency": "CAD"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "currency_conversion_convert",
    "arguments": {
      "amount": 150,
      "from_currency": "EUR",
      "to_currency": "CAD"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "currency_conversion_convert",
    "arguments": {
      "amount": 150,
      "from_currency": "EUR",
      "to_currency": "CAD"
    }
  }
]</pre>

</details>

## simple_python_391

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.467371 | 163 |
| Qwen3.8-27B | 正确 | 3.619346 | 138 |
| gemma-4-26B-A4B-it | 正确 | 0.341456 | 38 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Get the exchange rate from British pounds to Japanese yen with the fee 0.02 included.</pre>

### Official accepted answer

<pre>[
  {
    "get_exchange_rate_with_fee": {
      "base_currency": [
        "GBP"
      ],
      "target_currency": [
        "JPY"
      ],
      "fee": [
        0.02
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_exchange_rate_with_fee",
    "arguments": {
      "base_currency": "GBP",
      "target_currency": "JPY",
      "fee": 0.02
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_exchange_rate_with_fee",
    "arguments": {
      "base_currency": "GBP",
      "target_currency": "JPY",
      "fee": 0.02
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_exchange_rate_with_fee",
    "arguments": {
      "base_currency": "GBP",
      "fee": 0.02,
      "target_currency": "JPY"
    }
  }
]</pre>

</details>

## simple_python_392

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.202967 | 134 |
| Qwen3.8-27B | 正确 | 3.08204 | 116 |
| gemma-4-26B-A4B-it | 正确 | 0.258284 | 27 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Get me the latest exchange rate from British Pounds to Japanese Yen.</pre>

### Official accepted answer

<pre>[
  {
    "latest_exchange_rate": {
      "source_currency": [
        "GBP",
        "British Pounds",
        "Pounds Sterling"
      ],
      "target_currency": [
        "JPY",
        "Japanese Yen"
      ],
      "amount": [
        "",
        1.0
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>[
  {
    "name": "latest_exchange_rate",
    "arguments": {
      "source_currency": "GBP",
      "target_currency": "JPY"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "latest_exchange_rate",
    "arguments": {
      "source_currency": "GBP",
      "target_currency": "JPY"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "latest_exchange_rate",
    "arguments": {
      "source_currency": "GBP",
      "target_currency": "JPY"
    }
  }
]</pre>

</details>

## simple_python_393

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.229615 | 136 |
| Qwen3.8-27B | 错误 | 2.36914 | 87 |
| gemma-4-26B-A4B-it | 正确 | 0.303264 | 33 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: How much will 20000 Japanese Yen be in United States Dollar?</pre>

### Official accepted answer

<pre>[
  {
    "convert_currency": {
      "base_currency": [
        "JPY"
      ],
      "target_currency": [
        "USD"
      ],
      "amount": [
        20000
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>[
  {
    "name": "convert_currency",
    "arguments": {
      "base_currency": "JPY",
      "target_currency": "USD",
      "amount": 20000
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "convert_currency",
    "arguments": {
      "base_currency": "Japanese Yen",
      "target_currency": "United States Dollar",
      "amount": 20000
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'base_currency': 'Japanese Yen'. Expected one of ['JPY']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "convert_currency",
    "arguments": {
      "amount": 20000,
      "base_currency": "JPY",
      "target_currency": "USD"
    }
  }
]</pre>

</details>

## simple_python_394

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.353204 | 148 |
| Qwen3.8-27B | 正确 | 2.893153 | 108 |
| gemma-4-26B-A4B-it | 正确 | 0.323011 | 33 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Get me the travel distance and duration from the Eiffel Tower to the Louvre Museum</pre>

### Official accepted answer

<pre>[
  {
    "maps.get_distance_duration": {
      "start_location": [
        "Eiffel Tower"
      ],
      "end_location": [
        "Louvre Museum"
      ],
      "traffic": [
        "",
        false
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>[
  {
    "name": "maps_get_distance_duration",
    "arguments": {
      "start_location": "Eiffel Tower",
      "end_location": "Louvre Museum"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "maps_get_distance_duration",
    "arguments": {
      "start_location": "Eiffel Tower",
      "end_location": "Louvre Museum"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "maps_get_distance_duration",
    "arguments": {
      "end_location": "Louvre Museum",
      "start_location": "Eiffel Tower"
    }
  }
]</pre>

</details>

## simple_python_395

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.76002 | 198 |
| Qwen3.8-27B | 错误 | 2.990303 | 112 |
| gemma-4-26B-A4B-it | 正确 | 0.250944 | 26 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find the nearest parking lot within 2 miles of Central Park in New York.</pre>

### Official accepted answer

<pre>[
  {
    "parking_lot.find_nearest": {
      "location": [
        "Central Park, NY"
      ],
      "radius": [
        2
      ],
      "type": [
        "public",
        ""
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>[
  {
    "name": "parking_lot_find_nearest",
    "arguments": {
      "location": "Central Park, NY",
      "radius": 2
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "parking_lot_find_nearest",
    "arguments": {
      "location": "Central Park, New York",
      "radius": 2
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'location': 'Central Park, New York'. Expected one of ['Central Park, NY']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "parking_lot_find_nearest",
    "arguments": {
      "location": "Central Park, NY",
      "radius": 2
    }
  }
]</pre>

</details>

## simple_python_396

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.471486 | 163 |
| Qwen3.8-27B | 正确 | 2.846512 | 106 |
| gemma-4-26B-A4B-it | 正确 | 0.268785 | 28 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find a hospital within 5 km radius around Denver, Colorado with pediatrics department.</pre>

### Official accepted answer

<pre>[
  {
    "hospital.locate": {
      "location": [
        "Denver, Colorado",
        "Denver, CO"
      ],
      "radius": [
        5
      ],
      "department": [
        "Pediatrics"
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>[
  {
    "name": "hospital_locate",
    "arguments": {
      "location": "Denver, CO",
      "radius": 5,
      "department": "Pediatrics"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "hospital_locate",
    "arguments": {
      "location": "Denver, CO",
      "radius": 5,
      "department": "Pediatrics"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "hospital_locate",
    "arguments": {
      "department": "Pediatrics",
      "location": "Denver, CO",
      "radius": 5
    }
  }
]</pre>

</details>

## simple_python_397

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.26282 | 142 |
| Qwen3.8-27B | 正确 | 3.275264 | 124 |
| gemma-4-26B-A4B-it | 正确 | 0.280314 | 30 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find the distance between New York and Boston, accounting for terrain.</pre>

### Official accepted answer

<pre>[
  {
    "distance_calculator.calculate": {
      "origin": [
        "New York",
        "New York City",
        "New York City, NY",
        "New York, NY",
        "NYC"
      ],
      "destination": [
        "Boston"
      ],
      "consider_terrain": [
        true
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>[
  {
    "name": "distance_calculator_calculate",
    "arguments": {
      "origin": "New York",
      "destination": "Boston",
      "consider_terrain": true
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "distance_calculator_calculate",
    "arguments": {
      "origin": "New York",
      "destination": "Boston",
      "consider_terrain": true
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "distance_calculator_calculate",
    "arguments": {
      "consider_terrain": true,
      "destination": "Boston",
      "origin": "New York"
    }
  }
]</pre>

</details>

## simple_python_398

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.210837 | 133 |
| Qwen3.8-27B | 正确 | 2.191919 | 80 |
| gemma-4-26B-A4B-it | 正确 | 0.274844 | 29 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What are the opening hours of the Metropolitan Museum of Art on Saturday?</pre>

### Official accepted answer

<pre>[
  {
    "get_museum_hours": {
      "museum_name": [
        "Metropolitan Museum of Art",
        "The Met"
      ],
      "day": [
        "Saturday"
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_museum_hours",
    "arguments": {
      "museum_name": "Metropolitan Museum of Art",
      "day": "Saturday"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_museum_hours",
    "arguments": {
      "museum_name": "Metropolitan Museum of Art",
      "day": "Saturday"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_museum_hours",
    "arguments": {
      "day": "Saturday",
      "museum_name": "Metropolitan Museum of Art"
    }
  }
]</pre>

</details>

## simple_python_399

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.982243 | 221 |
| Qwen3.8-27B | 正确 | 6.25036 | 241 |
| gemma-4-26B-A4B-it | 正确 | 0.344327 | 38 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find me the best Italian restaurants in New York City with average customer ratings of more than 4 and accepts credit cards.</pre>

### Official accepted answer

<pre>[
  {
    "restaurant_search": {
      "location": [
        "New York City",
        "New York City, NY",
        "NYC"
      ],
      "cuisine": [
        "Italian"
      ],
      "rating": [
        4
      ],
      "accepts_credit_cards": [
        true
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>[
  {
    "name": "restaurant_search",
    "arguments": {
      "location": "New York City, NY",
      "cuisine": "Italian",
      "rating": 4,
      "accepts_credit_cards": true
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "restaurant_search",
    "arguments": {
      "location": "New York City, NY",
      "cuisine": "Italian",
      "rating": 4,
      "accepts_credit_cards": true
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "restaurant_search",
    "arguments": {
      "accepts_credit_cards": true,
      "cuisine": "Italian",
      "location": "New York City, NY",
      "rating": 4
    }
  }
]</pre>

</details>


[Category index](README.md) · [All categories](../README.md) · [Previous](page-013.md)
