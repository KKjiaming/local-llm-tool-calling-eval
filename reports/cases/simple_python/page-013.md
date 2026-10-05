# simple_python — page 13/14

[Category index](README.md) · [All categories](../README.md) · [Previous](page-012.md) · [Next](page-014.md)

30 cases. Expand the question/answer and model sections below. Tool calls were scored, not executed.

## simple_python_360

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.406335 | 158 |
| Qwen3.8-27B | 错误 | 5.483966 | 212 |
| gemma-4-26B-A4B-it | 错误 | 0.244044 | 25 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find a recipe for pasta carbonara which contains only less than 500 calories.</pre>

### Official accepted answer

<pre>[
  {
    "find_recipe": {
      "recipeName": [
        "pasta carbonara"
      ],
      "maxCalories": [
        500
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
    "name": "find_recipe",
    "arguments": {
      "recipeName": "pasta carbonara",
      "maxCalories": 500
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "find_recipe",
    "arguments": {
      "recipeName": "pasta carbonara",
      "maxCalories": 499
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'maxCalories': 499. Expected one of [500]."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 错误</summary>

### Model output

<pre>[
  {
    "name": "find_recipe",
    "arguments": {
      "maxCalories": 499,
      "recipeName": "pasta carbonara"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'maxCalories': 499. Expected one of [500]."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

## simple_python_361

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.359401 | 152 |
| Qwen3.8-27B | 正确 | 3.136169 | 118 |
| gemma-4-26B-A4B-it | 正确 | 0.296564 | 32 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find Italian restaurants near New York city that serves gluten-free options.</pre>

### Official accepted answer

<pre>[
  {
    "restaurant_finder": {
      "city": [
        "New York City",
        "New York City, NY",
        "NYC",
        "New York"
      ],
      "cuisine": [
        "Italian"
      ],
      "diet": [
        "Gluten-free"
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
    "name": "restaurant_finder",
    "arguments": {
      "city": "New York",
      "cuisine": "Italian",
      "diet": "Gluten-free"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "restaurant_finder",
    "arguments": {
      "city": "New York",
      "cuisine": "Italian",
      "diet": "Gluten-free"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "restaurant_finder",
    "arguments": {
      "city": "New York City",
      "cuisine": "Italian",
      "diet": "Gluten-free"
    }
  }
]</pre>

</details>

## simple_python_362

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.521079 | 152 |
| Qwen3.8-27B | 正确 | 3.776654 | 143 |
| gemma-4-26B-A4B-it | 正确 | 0.281628 | 30 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What are the top five sushi restaurants with high reviews i.e. above 4/5 in Tokyo?</pre>

### Official accepted answer

<pre>[
  {
    "get_best_sushi_places": {
      "city": [
        "Tokyo"
      ],
      "top": [
        5
      ],
      "review_rate": [
        4.0
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
    "name": "get_best_sushi_places",
    "arguments": {
      "city": "Tokyo",
      "top": 5,
      "review_rate": 4
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_best_sushi_places",
    "arguments": {
      "city": "Tokyo",
      "top": 5,
      "review_rate": 4
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_best_sushi_places",
    "arguments": {
      "city": "Tokyo",
      "review_rate": 4,
      "top": 5
    }
  }
]</pre>

</details>

## simple_python_363

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.353424 | 150 |
| Qwen3.8-27B | 正确 | 3.163013 | 118 |
| gemma-4-26B-A4B-it | 正确 | 0.321713 | 35 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find the closest sushi restaurant with a patio in Boston.</pre>

### Official accepted answer

<pre>[
  {
    "restaurant_search.find_closest": {
      "location": [
        "Boston",
        "Boston, MA"
      ],
      "cuisine": [
        "Sushi",
        "sushi"
      ],
      "amenities": [
        [
          "Patio"
        ]
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
    "name": "restaurant_search_find_closest",
    "arguments": {
      "location": "Boston",
      "cuisine": "Sushi",
      "amenities": [
        "Patio"
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "restaurant_search_find_closest",
    "arguments": {
      "location": "Boston, MA",
      "cuisine": "Sushi",
      "amenities": [
        "Patio"
      ]
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "restaurant_search_find_closest",
    "arguments": {
      "amenities": [
        "Patio"
      ],
      "cuisine": "Sushi",
      "location": "Boston, MA"
    }
  }
]</pre>

</details>

## simple_python_364

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.408166 | 158 |
| Qwen3.8-27B | 正确 | 2.675686 | 95 |
| gemma-4-26B-A4B-it | 正确 | 0.296853 | 32 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Can I find an Italian restaurant with Gluten-free options near Brooklyn?</pre>

### Official accepted answer

<pre>[
  {
    "find_restaurant": {
      "location": [
        "Brooklyn",
        "Brooklyn, NY"
      ],
      "type": [
        "Italian"
      ],
      "diet_option": [
        "Gluten-free"
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
    "name": "find_restaurant",
    "arguments": {
      "location": "Brooklyn",
      "type": "Italian",
      "diet_option": "Gluten-free"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "find_restaurant",
    "arguments": {
      "location": "Brooklyn",
      "type": "Italian",
      "diet_option": "Gluten-free"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "find_restaurant",
    "arguments": {
      "diet_option": "Gluten-free",
      "location": "Brooklyn",
      "type": "Italian"
    }
  }
]</pre>

</details>

## simple_python_365

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.396518 | 156 |
| Qwen3.8-27B | 正确 | 3.588695 | 135 |
| gemma-4-26B-A4B-it | 正确 | 0.336063 | 37 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: How many ounces in 2 pounds of butter?</pre>

### Official accepted answer

<pre>[
  {
    "cooking_conversion.convert": {
      "quantity": [
        2
      ],
      "from_unit": [
        "pound",
        "pounds",
        "lb",
        "lbs"
      ],
      "to_unit": [
        "ounce",
        "ounces",
        "oz"
      ],
      "item": [
        "butter"
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
    "name": "cooking_conversion_convert",
    "arguments": {
      "quantity": 2,
      "from_unit": "pounds",
      "to_unit": "ounces",
      "item": "butter"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "cooking_conversion_convert",
    "arguments": {
      "quantity": 2,
      "from_unit": "pounds",
      "to_unit": "ounces",
      "item": "butter"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "cooking_conversion_convert",
    "arguments": {
      "from_unit": "pounds",
      "item": "butter",
      "quantity": 2,
      "to_unit": "ounces"
    }
  }
]</pre>

</details>

## simple_python_366

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.169832 | 128 |
| Qwen3.8-27B | 正确 | 5.151701 | 197 |
| gemma-4-26B-A4B-it | 正确 | 0.313796 | 34 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: How many teaspoons are in 2 tablespoons for measurement in my recipe?</pre>

### Official accepted answer

<pre>[
  {
    "recipe.unit_conversion": {
      "value": [
        2
      ],
      "from_unit": [
        "tablespoon",
        "tbsp"
      ],
      "to_unit": [
        "teaspoon",
        "tsp"
      ],
      "precision": [
        1,
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
    "name": "recipe_unit_conversion",
    "arguments": {
      "value": 2,
      "from_unit": "tablespoon",
      "to_unit": "teaspoon"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "recipe_unit_conversion",
    "arguments": {
      "value": 2,
      "from_unit": "tablespoon",
      "to_unit": "teaspoon"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "recipe_unit_conversion",
    "arguments": {
      "from_unit": "tablespoon",
      "to_unit": "teaspoon",
      "value": 2
    }
  }
]</pre>

</details>

## simple_python_367

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.403692 | 157 |
| Qwen3.8-27B | 正确 | 3.541437 | 134 |
| gemma-4-26B-A4B-it | 正确 | 0.296746 | 32 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find me a vegan recipe for brownies which prep time is under 30 minutes.</pre>

### Official accepted answer

<pre>[
  {
    "find_recipe": {
      "dietary_restrictions": [
        "vegan"
      ],
      "recipe_type": [
        "dessert"
      ],
      "time": [
        30
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
    "name": "find_recipe",
    "arguments": {
      "dietary_restrictions": "vegan",
      "recipe_type": "dessert",
      "time": 30
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "find_recipe",
    "arguments": {
      "dietary_restrictions": "vegan",
      "recipe_type": "dessert",
      "time": 30
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "find_recipe",
    "arguments": {
      "dietary_restrictions": "vegan",
      "recipe_type": "dessert",
      "time": 30
    }
  }
]</pre>

</details>

## simple_python_368

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.41059 | 158 |
| Qwen3.8-27B | 正确 | 2.33684 | 85 |
| gemma-4-26B-A4B-it | 正确 | 0.198441 | 19 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: How much time will it take to cook a roast chicken of 1.5 kg?</pre>

### Official accepted answer

<pre>[
  {
    "calculate_cooking_time": {
      "weight_kg": [
        1.5
      ],
      "cooking_method": [
        "",
        "roast"
      ],
      "temp_celsius": [
        "",
        180
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
    "name": "calculate_cooking_time",
    "arguments": {
      "weight_kg": 1.5
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_cooking_time",
    "arguments": {
      "weight_kg": 1.5
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_cooking_time",
    "arguments": {
      "weight_kg": 1.5
    }
  }
]</pre>

</details>

## simple_python_369

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.303235 | 145 |
| Qwen3.8-27B | 正确 | 2.91759 | 108 |
| gemma-4-26B-A4B-it | 正确 | 0.328315 | 36 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find a grocery store near me with organic fruits and vegetables in Houston.</pre>

### Official accepted answer

<pre>[
  {
    "grocery_store.find_nearby": {
      "location": [
        "Houston",
        "Houston, TX"
      ],
      "categories": [
        [
          "Organic",
          "Vegetables",
          "Fruits"
        ],
        [
          "Organic",
          "Fruits",
          "Vegetables"
        ],
        [
          "Vegetables",
          "Fruits",
          "Organic"
        ],
        [
          "Fruits",
          "Vegetables",
          "Organic"
        ],
        [
          "Fruits",
          "Organic",
          "Vegetables"
        ],
        [
          "Vegetables",
          "Organic",
          "Fruits"
        ]
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
    "name": "grocery_store_find_nearby",
    "arguments": {
      "location": "Houston",
      "categories": [
        "Organic",
        "Fruits",
        "Vegetables"
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "grocery_store_find_nearby",
    "arguments": {
      "location": "Houston, TX",
      "categories": [
        "Organic",
        "Fruits",
        "Vegetables"
      ]
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "grocery_store_find_nearby",
    "arguments": {
      "categories": [
        "Organic",
        "Fruits",
        "Vegetables"
      ],
      "location": "Houston, TX"
    }
  }
]</pre>

</details>

## simple_python_370

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.52068 | 171 |
| Qwen3.8-27B | 错误 | 5.273505 | 203 |
| gemma-4-26B-A4B-it | 错误 | 0.376026 | 42 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Order three bottles of olive oil and a five pound bag of rice from Safeway in Palo Alto.</pre>

### Official accepted answer

<pre>[
  {
    "safeway.order": {
      "location": [
        "Palo Alto",
        "Palo Alto, CA"
      ],
      "items": [
        [
          "olive oil",
          "rice"
        ],
        [
          "olive oil",
          "bag of rice"
        ]
      ],
      "quantity": [
        [
          3,
          1
        ]
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
    "name": "safeway_order",
    "arguments": {
      "location": "Palo Alto, CA",
      "items": [
        "olive oil",
        "rice"
      ],
      "quantity": [
        3,
        1
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "safeway_order",
    "arguments": {
      "location": "Palo Alto, CA",
      "items": [
        "olive oil",
        "5 lb bag of rice"
      ],
      "quantity": [
        3,
        1
      ]
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'items': ['olive oil', '5 lb bag of rice']. Expected one of [['olive oil', 'rice'], ['olive oil', 'bag of rice']]."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 错误</summary>

### Model output

<pre>[
  {
    "name": "safeway_order",
    "arguments": {
      "items": [
        "olive oil",
        "rice (5lb bag)"
      ],
      "location": "Palo Alto, CA",
      "quantity": [
        3,
        1
      ]
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'items': ['olive oil', 'rice (5lb bag)']. Expected one of [['olive oil', 'rice'], ['olive oil', 'bag of rice']]."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

## simple_python_371

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.3743 | 154 |
| Qwen3.8-27B | 正确 | 2.936732 | 110 |
| gemma-4-26B-A4B-it | 正确 | 0.305446 | 33 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Check the price of tomatoes and lettuce at the Whole Foods in Los Angeles.</pre>

### Official accepted answer

<pre>[
  {
    "whole_foods.check_price": {
      "location": [
        "Los Angeles",
        "LA"
      ],
      "items": [
        [
          "tomatoes",
          "lettuce"
        ]
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
    "name": "whole_foods_check_price",
    "arguments": {
      "location": "Los Angeles",
      "items": [
        "tomatoes",
        "lettuce"
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "whole_foods_check_price",
    "arguments": {
      "location": "Los Angeles",
      "items": [
        "tomatoes",
        "lettuce"
      ]
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "whole_foods_check_price",
    "arguments": {
      "items": [
        "tomatoes",
        "lettuce"
      ],
      "location": "Los Angeles"
    }
  }
]</pre>

</details>

## simple_python_372

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.369712 | 153 |
| Qwen3.8-27B | 正确 | 3.474866 | 130 |
| gemma-4-26B-A4B-it | 正确 | 0.285853 | 30 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find the top five organic bananas brands on the basis of rating from Whole Foods store.</pre>

### Official accepted answer

<pre>[
  {
    "whole_foods.find_top_brands": {
      "product": [
        "bananas"
      ],
      "number": [
        5,
        ""
      ],
      "organic": [
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
    "name": "whole_foods_find_top_brands",
    "arguments": {
      "product": "bananas",
      "number": 5,
      "organic": true
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "whole_foods_find_top_brands",
    "arguments": {
      "product": "bananas",
      "number": 5,
      "organic": true
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "whole_foods_find_top_brands",
    "arguments": {
      "number": 5,
      "organic": true,
      "product": "bananas"
    }
  }
]</pre>

</details>

## simple_python_373

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 错误 | 4.190494 | 484 |
| Qwen3.8-27B | 错误 | 3.964137 | 150 |
| gemma-4-26B-A4B-it | 错误 | 0.377323 | 42 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I want to buy apples, rice, and 12 pack of bottled water from a Walmart near San Jose. Show me the product information and stock availability.</pre>

### Official accepted answer

<pre>[
  {
    "walmart.purchase": {
      "loc": [
        "San Jose",
        "San Jose, CA"
      ],
      "product_list": [
        [
          "apples",
          "rice",
          "bottled water"
        ],
        [
          "apples",
          "rice",
          "water"
        ]
      ],
      "pack_size": [
        [
          1,
          1,
          12
        ]
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 错误</summary>

### Model output

<pre>[
  {
    "name": "walmart_purchase",
    "arguments": {
      "loc": "San Jose",
      "product_list": [
        "apples",
        "rice",
        "12 pack of bottled water"
      ]
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'product_list': ['apples', 'rice', '12 pack of bottled water']. Expected one of [['apples', 'rice', 'bottled water'], ['apples', 'rice', 'water']]."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "walmart_purchase",
    "arguments": {
      "loc": "San Jose",
      "product_list": [
        "apples",
        "rice",
        "12 pack of bottled water"
      ]
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'product_list': ['apples', 'rice', '12 pack of bottled water']. Expected one of [['apples', 'rice', 'bottled water'], ['apples', 'rice', 'water']]."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 错误</summary>

### Model output

<pre>[
  {
    "name": "walmart_purchase",
    "arguments": {
      "loc": "San Jose",
      "pack_size": [
        12
      ],
      "product_list": [
        "apples",
        "rice",
        "bottled water"
      ]
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'pack_size': [12]. Expected one of [[1, 1, 12]]."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

## simple_python_374

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.477036 | 163 |
| Qwen3.8-27B | 正确 | 3.753292 | 143 |
| gemma-4-26B-A4B-it | 正确 | 0.384099 | 43 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Check the amount of protein, calories and carbs in an avocado from Walmart.</pre>

### Official accepted answer

<pre>[
  {
    "grocery_info.nutritional_info": {
      "store": [
        "Walmart"
      ],
      "food": [
        "avocado",
        "Avocado"
      ],
      "information": [
        [
          "Protein",
          "Calories",
          "Carbohydrates"
        ]
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
    "name": "grocery_info_nutritional_info",
    "arguments": {
      "store": "Walmart",
      "food": "avocado",
      "information": [
        "Protein",
        "Calories",
        "Carbohydrates"
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "grocery_info_nutritional_info",
    "arguments": {
      "store": "Walmart",
      "food": "avocado",
      "information": [
        "Protein",
        "Calories",
        "Carbohydrates"
      ]
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "grocery_info_nutritional_info",
    "arguments": {
      "food": "avocado",
      "information": [
        "Protein",
        "Calories",
        "Carbohydrates"
      ],
      "store": "Walmart"
    }
  }
]</pre>

</details>

## simple_python_375

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 4.160739 | 480 |
| Qwen3.8-27B | 错误 | 10.953783 | 431 |
| gemma-4-26B-A4B-it | 正确 | 0.283273 | 30 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Check the total price for three pumpkins and two dozen eggs at Walmart.</pre>

### Official accepted answer

<pre>[
  {
    "walmart.check_price": {
      "items": [
        [
          "pumpkins",
          "eggs"
        ],
        [
          "pumpkin",
          "dozen eggs"
        ]
      ],
      "quantities": [
        [
          3,
          24
        ],
        [
          3,
          2
        ]
      ],
      "store_location": [
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
    "name": "walmart_check_price",
    "arguments": {
      "items": [
        "pumpkins",
        "eggs"
      ],
      "quantities": [
        3,
        24
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "walmart_check_price",
    "arguments": {
      "items": [
        "pumpkin",
        "eggs"
      ],
      "quantities": [
        3,
        24
      ]
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'items': ['pumpkin', 'eggs']. Expected one of [['pumpkins', 'eggs'], ['pumpkin', 'dozen eggs']]."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "walmart_check_price",
    "arguments": {
      "items": [
        "pumpkin",
        "dozen eggs"
      ],
      "quantities": [
        3,
        2
      ]
    }
  }
]</pre>

</details>

## simple_python_376

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.387288 | 156 |
| Qwen3.8-27B | 正确 | 2.691744 | 100 |
| gemma-4-26B-A4B-it | 正确 | 0.301966 | 33 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What time is it currently in London, UK in 24 hour format?</pre>

### Official accepted answer

<pre>[
  {
    "time_zone_converter": {
      "city": [
        "London"
      ],
      "country": [
        "UK",
        "United Kingdom"
      ],
      "display_format": [
        "24h",
        "24 hour"
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
    "name": "time_zone_converter",
    "arguments": {
      "city": "London",
      "country": "UK",
      "display_format": "24h"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "time_zone_converter",
    "arguments": {
      "city": "London",
      "country": "UK",
      "display_format": "24h"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "time_zone_converter",
    "arguments": {
      "city": "London",
      "country": "UK",
      "display_format": "24h"
    }
  }
]</pre>

</details>

## simple_python_377

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.088003 | 119 |
| Qwen3.8-27B | 正确 | 3.237148 | 122 |
| gemma-4-26B-A4B-it | 正确 | 0.226441 | 23 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What is the current time in Sydney, Australia?</pre>

### Official accepted answer

<pre>[
  {
    "get_current_time": {
      "city": [
        "Sydney"
      ],
      "country": [
        "Australia"
      ],
      "format": [
        "",
        "HH:MM:SS"
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
    "name": "get_current_time",
    "arguments": {
      "city": "Sydney",
      "country": "Australia"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_time",
    "arguments": {
      "city": "Sydney",
      "country": "Australia"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_time",
    "arguments": {
      "city": "Sydney",
      "country": "Australia"
    }
  }
]</pre>

</details>

## simple_python_378

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.106663 | 121 |
| Qwen3.8-27B | 正确 | 2.265684 | 83 |
| gemma-4-26B-A4B-it | 正确 | 0.341018 | 38 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Convert time 3pm from New York time zone to London time zone.</pre>

### Official accepted answer

<pre>[
  {
    "timezone.convert": {
      "time": [
        "3pm"
      ],
      "from_timezone": [
        "America/New_York",
        "New York",
        "NYC",
        "New York City"
      ],
      "to_timezone": [
        "Europe/London",
        "London"
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
    "name": "timezone_convert",
    "arguments": {
      "time": "3pm",
      "from_timezone": "New York",
      "to_timezone": "London"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "timezone_convert",
    "arguments": {
      "time": "3pm",
      "from_timezone": "New York",
      "to_timezone": "London"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "timezone_convert",
    "arguments": {
      "from_timezone": "America/New_York",
      "time": "3pm",
      "to_timezone": "Europe/London"
    }
  }
]</pre>

</details>

## simple_python_379

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.091835 | 120 |
| Qwen3.8-27B | 正确 | 2.064214 | 75 |
| gemma-4-26B-A4B-it | 正确 | 0.228003 | 23 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What's the current time in Sydney, Australia?</pre>

### Official accepted answer

<pre>[
  {
    "get_current_time": {
      "location": [
        "Sydney"
      ],
      "country": [
        "Australia",
        "Australia/Sydney"
      ],
      "timezone": [
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
    "name": "get_current_time",
    "arguments": {
      "location": "Sydney",
      "country": "Australia"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_time",
    "arguments": {
      "location": "Sydney",
      "country": "Australia"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_time",
    "arguments": {
      "country": "Australia",
      "location": "Sydney"
    }
  }
]</pre>

</details>

## simple_python_380

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.233349 | 252 |
| Qwen3.8-27B | 正确 | 4.282862 | 158 |
| gemma-4-26B-A4B-it | 正确 | 0.496753 | 56 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Book a single room at a pet friendly hotel near Manhattan, New York for 3 nights starting from March 10th, 2023.</pre>

### Official accepted answer

<pre>[
  {
    "hotel_booking": {
      "location": [
        "Manhattan, New York",
        "Manhattan, NY",
        "NYC",
        "New York City"
      ],
      "room_type": [
        "single"
      ],
      "duration": [
        3
      ],
      "start_date": [
        "2023-03-10",
        "03/10/2023",
        "Mar.10,2023",
        "March 10th, 2023",
        "March 10th,2023",
        "March10th, 2023",
        "March10th,2023"
      ],
      "preferences": [
        [
          "pet_friendly"
        ]
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
    "name": "hotel_booking",
    "arguments": {
      "location": "Manhattan, New York",
      "room_type": "single",
      "duration": 3,
      "start_date": "2023-03-10",
      "preferences": [
        "pet_friendly"
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "hotel_booking",
    "arguments": {
      "location": "Manhattan, New York",
      "room_type": "single",
      "duration": 3,
      "start_date": "2023-03-10",
      "preferences": [
        "pet_friendly"
      ]
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "hotel_booking",
    "arguments": {
      "duration": 3,
      "location": "Manhattan, New York",
      "preferences": [
        "pet_friendly"
      ],
      "room_type": "single",
      "start_date": "2023-03-10"
    }
  }
]</pre>

</details>

## simple_python_381

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.31288 | 262 |
| Qwen3.8-27B | 正确 | 5.739939 | 222 |
| gemma-4-26B-A4B-it | 正确 | 0.642972 | 76 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Check if any Hilton Hotel is available for two adults in Paris from 2023 April 4th to April 8th?</pre>

### Official accepted answer

<pre>[
  {
    "hilton_hotel.check_availability": {
      "location": [
        "Paris"
      ],
      "check_in_date": [
        "2023-04-04"
      ],
      "check_out_date": [
        "2023-04-08"
      ],
      "no_of_adults": [
        2
      ],
      "hotel_chain": [
        "Hilton",
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
    "name": "hilton_hotel_check_availability",
    "arguments": {
      "location": "Paris",
      "check_in_date": "2023-04-04",
      "check_out_date": "2023-04-08",
      "no_of_adults": 2,
      "hotel_chain": "Hilton"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "hilton_hotel_check_availability",
    "arguments": {
      "location": "Paris",
      "check_in_date": "2023-04-04",
      "check_out_date": "2023-04-08",
      "no_of_adults": 2,
      "hotel_chain": "Hilton"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "hilton_hotel_check_availability",
    "arguments": {
      "check_in_date": "2023-04-04",
      "check_out_date": "2023-04-08",
      "hotel_chain": "Hilton",
      "location": "Paris",
      "no_of_adults": 2
    }
  }
]</pre>

</details>

## simple_python_382

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 错误 | 2.235477 | 253 |
| Qwen3.8-27B | 错误 | 4.779664 | 183 |
| gemma-4-26B-A4B-it | 错误 | 0.478092 | 55 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Book a single room for two nights at the Hilton Hotel in Chicago, starting from 10th December 2022.</pre>

### Official accepted answer

<pre>[
  {
    "book_hotel": {
      "hotel_name": [
        "Hilton Hotel",
        "Hilton"
      ],
      "location": [
        "Chicago"
      ],
      "room_type": [
        "single"
      ],
      "start_date": [
        "2022-12-10",
        "10/12/2022",
        "Dec 10, 2022",
        "December 10, 2022"
      ],
      "nights": [
        2
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 错误</summary>

### Model output

<pre>[
  {
    "name": "book_hotel",
    "arguments": {
      "hotel_name": "Hilton Hotel",
      "location": "Chicago",
      "room_type": "Single room",
      "start_date": "2022-12-10",
      "nights": 2
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'room_type': 'Single room'. Expected one of ['single']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "book_hotel",
    "arguments": {
      "hotel_name": "Hilton Hotel",
      "location": "Chicago",
      "room_type": "single room",
      "start_date": "2022-12-10",
      "nights": 2
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'room_type': 'single room'. Expected one of ['single']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 错误</summary>

### Model output

<pre>[
  {
    "name": "book_hotel",
    "arguments": {
      "hotel_name": "Hilton Hotel",
      "location": "Chicago",
      "nights": 2,
      "room_type": "single room",
      "start_date": "2022-12-10"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'room_type': 'single room'. Expected one of ['single']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

## simple_python_383

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 错误 | 1.287252 | 143 |
| Qwen3.8-27B | 错误 | 3.318672 | 125 |
| gemma-4-26B-A4B-it | 错误 | 0.313611 | 34 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I would like to book a single room for two nights at The Plaza hotel.</pre>

### Official accepted answer

<pre>[
  {
    "book_room": {
      "hotel_name": [
        "The Plaza"
      ],
      "room_type": [
        "Single",
        "single"
      ],
      "num_nights": [
        2
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 错误</summary>

### Model output

<pre>[
  {
    "name": "book_room",
    "arguments": {
      "hotel_name": "The Plaza hotel",
      "room_type": "single room",
      "num_nights": 2
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'hotel_name': 'The Plaza hotel'. Expected one of ['The Plaza']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "book_room",
    "arguments": {
      "hotel_name": "The Plaza",
      "room_type": "single room",
      "num_nights": 2
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'room_type': 'single room'. Expected one of ['Single', 'single']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 错误</summary>

### Model output

<pre>[
  {
    "name": "book_room",
    "arguments": {
      "hotel_name": "The Plaza hotel",
      "num_nights": 2,
      "room_type": "single room"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'hotel_name': 'The Plaza hotel'. Expected one of ['The Plaza']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

## simple_python_384

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.261715 | 255 |
| Qwen3.8-27B | 正确 | 4.865999 | 184 |
| gemma-4-26B-A4B-it | 正确 | 0.540119 | 62 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Book a hotel room for two adults and one child in Paris, France from July 10, 2022 to July 20, 2022.</pre>

### Official accepted answer

<pre>[
  {
    "hotel_booking.book": {
      "city": [
        "Paris",
        "Paris, France"
      ],
      "from_date": [
        "07-10-2022",
        "2022-07-10",
        "10/07/2022",
        "Jul.10,2022"
      ],
      "to_date": [
        "07-20-2022",
        "2022-07-20",
        "20/07/2022",
        "Jul.20,2022"
      ],
      "adults": [
        2
      ],
      "children": [
        1
      ],
      "room_type": [
        "Standard",
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
    "name": "hotel_booking_book",
    "arguments": {
      "city": "Paris, France",
      "from_date": "07-10-2022",
      "to_date": "07-20-2022",
      "adults": 2,
      "children": 1,
      "room_type": "Standard"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "hotel_booking_book",
    "arguments": {
      "city": "Paris, France",
      "from_date": "07-10-2022",
      "to_date": "07-20-2022",
      "adults": 2,
      "children": 1
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "hotel_booking_book",
    "arguments": {
      "adults": 2,
      "children": 1,
      "city": "Paris, France",
      "from_date": "07-10-2022",
      "to_date": "07-20-2022"
    }
  }
]</pre>

</details>

## simple_python_385

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.489431 | 282 |
| Qwen3.8-27B | 正确 | 5.220133 | 197 |
| gemma-4-26B-A4B-it | 正确 | 0.509656 | 58 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Book a hotel room with king size bed in Los Angeles for 2 nights starting from 15th October,2023.</pre>

### Official accepted answer

<pre>[
  {
    "hotel_bookings.book_room": {
      "location": [
        "Los Angeles",
        "Los Angeles, CA",
        "LA"
      ],
      "room_type": [
        "King Size",
        "king size"
      ],
      "check_in_date": [
        "15-10-2023",
        "15th October",
        "2023-10-15",
        "10/15/2023",
        "Oct.15,2023"
      ],
      "no_of_nights": [
        2
      ],
      "no_of_rooms": [
        "",
        1
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
    "name": "hotel_bookings_book_room",
    "arguments": {
      "location": "Los Angeles, CA",
      "room_type": "king size",
      "check_in_date": "15-10-2023",
      "no_of_nights": 2
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "hotel_bookings_book_room",
    "arguments": {
      "location": "Los Angeles, CA",
      "room_type": "king size",
      "check_in_date": "15-10-2023",
      "no_of_nights": 2
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "hotel_bookings_book_room",
    "arguments": {
      "check_in_date": "15-10-2023",
      "location": "Los Angeles, CA",
      "no_of_nights": 2,
      "room_type": "king size"
    }
  }
]</pre>

</details>

## simple_python_386

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 错误 | 2.503688 | 283 |
| Qwen3.8-27B | 错误 | 5.569582 | 214 |
| gemma-4-26B-A4B-it | 错误 | 0.553188 | 64 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Book a luxury room in Hotel Paradise, Las Vegas, with a city view for 3 days starting from May 12, 2022.</pre>

### Official accepted answer

<pre>[
  {
    "book_hotel": {
      "hotel_name": [
        "Hotel Paradise"
      ],
      "location": [
        "Las Vegas",
        "LV"
      ],
      "room_type": [
        "luxury",
        "Luxury"
      ],
      "start_date": [
        "05-12-2022",
        "2022-05-12",
        "12/05/2022",
        "May.12,2022",
        "May 12, 2022"
      ],
      "stay_duration": [
        3
      ],
      "view": [
        "city view",
        "city"
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 错误</summary>

### Model output

<pre>[
  {
    "name": "book_hotel",
    "arguments": {
      "hotel_name": "Hotel Paradise",
      "location": "Las Vegas",
      "room_type": "luxury room",
      "start_date": "05-12-2022",
      "stay_duration": 3,
      "view": "city view"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'room_type': 'luxury room'. Expected one of ['luxury', 'Luxury']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "book_hotel",
    "arguments": {
      "hotel_name": "Hotel Paradise",
      "location": "Las Vegas",
      "room_type": "luxury room",
      "start_date": "05-12-2022",
      "stay_duration": 3,
      "view": "city view"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'room_type': 'luxury room'. Expected one of ['luxury', 'Luxury']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 错误</summary>

### Model output

<pre>[
  {
    "name": "book_hotel",
    "arguments": {
      "hotel_name": "Hotel Paradise",
      "location": "Las Vegas",
      "room_type": "luxury room",
      "start_date": "05-12-2022",
      "stay_duration": 3,
      "view": "city view"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'room_type': 'luxury room'. Expected one of ['luxury', 'Luxury']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

## simple_python_387

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.874879 | 326 |
| Qwen3.8-27B | 正确 | 5.250018 | 204 |
| gemma-4-26B-A4B-it | 正确 | 0.559943 | 66 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Book a hotel room at the Plaza Hotel in New York for 3 nights starting from 1st June 2022</pre>

### Official accepted answer

<pre>[
  {
    "hotel_booking": {
      "hotel_name": [
        "Plaza Hotel"
      ],
      "location": [
        "New York City, NY",
        "New York, NY"
      ],
      "start_date": [
        "2022-06-01",
        "06/01/2022",
        "Jun.1,2022"
      ],
      "end_date": [
        "2022-06-04",
        "06/04/2022",
        "Jun.4,2022"
      ],
      "rooms": [
        1,
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
    "name": "hotel_booking",
    "arguments": {
      "hotel_name": "Plaza Hotel",
      "location": "New York, NY",
      "start_date": "2022-06-01",
      "end_date": "2022-06-04"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "hotel_booking",
    "arguments": {
      "hotel_name": "Plaza Hotel",
      "location": "New York, NY",
      "start_date": "2022-06-01",
      "end_date": "2022-06-04",
      "rooms": 1
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "hotel_booking",
    "arguments": {
      "end_date": "2022-06-04",
      "hotel_name": "Plaza Hotel",
      "location": "New York, NY",
      "rooms": 1,
      "start_date": "2022-06-01"
    }
  }
]</pre>

</details>

## simple_python_388

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.211956 | 133 |
| Qwen3.8-27B | 正确 | 2.234719 | 82 |
| gemma-4-26B-A4B-it | 正确 | 0.305849 | 33 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: How many Canadian dollars can I get for 500 US dollars?</pre>

### Official accepted answer

<pre>[
  {
    "currency_exchange.convert": {
      "base_currency": [
        "USD"
      ],
      "target_currency": [
        "CAD"
      ],
      "amount": [
        500
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
    "name": "currency_exchange_convert",
    "arguments": {
      "base_currency": "USD",
      "target_currency": "CAD",
      "amount": 500
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "currency_exchange_convert",
    "arguments": {
      "base_currency": "USD",
      "target_currency": "CAD",
      "amount": 500
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "currency_exchange_convert",
    "arguments": {
      "amount": 500,
      "base_currency": "USD",
      "target_currency": "CAD"
    }
  }
]</pre>

</details>

## simple_python_389

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.240779 | 136 |
| Qwen3.8-27B | 正确 | 3.332428 | 124 |
| gemma-4-26B-A4B-it | 正确 | 0.291787 | 31 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Calculate the current cost in British Pounds if I need to convert 200 US dollars.</pre>

### Official accepted answer

<pre>[
  {
    "currency_converter": {
      "base_currency": [
        "USD"
      ],
      "target_currency": [
        "GBP"
      ],
      "amount": [
        200.0
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
    "name": "currency_converter",
    "arguments": {
      "base_currency": "USD",
      "target_currency": "GBP",
      "amount": 200
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "currency_converter",
    "arguments": {
      "base_currency": "USD",
      "target_currency": "GBP",
      "amount": 200
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "currency_converter",
    "arguments": {
      "amount": 200,
      "base_currency": "USD",
      "target_currency": "GBP"
    }
  }
]</pre>

</details>


[Category index](README.md) · [All categories](../README.md) · [Previous](page-012.md) · [Next](page-014.md)
