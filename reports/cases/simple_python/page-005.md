# simple_python — page 5/14

[Category index](README.md) · [All categories](../README.md) · [Previous](page-004.md) · [Next](page-006.md)

30 cases. Expand the question/answer and model sections below. Tool calls were scored, not executed.

## simple_python_120

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.963565 | 226 |
| Qwen3.8-27B | 正确 | 3.870055 | 147 |
| gemma-4-26B-A4B-it | 正确 | 0.393569 | 46 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Run a two sample T-test to compare the average of Group A [3, 4, 5, 6, 4] and Group B [7, 8, 9, 8, 7] assuming equal variance.</pre>

### Official accepted answer

<pre>[
  {
    "run_two_sample_ttest": {
      "group1": [
        [
          3,
          4,
          5,
          6,
          4
        ]
      ],
      "group2": [
        [
          7,
          8,
          9,
          8,
          7
        ]
      ],
      "equal_variance": [
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
    "name": "run_two_sample_ttest",
    "arguments": {
      "group1": [
        3,
        4,
        5,
        6,
        4
      ],
      "group2": [
        7,
        8,
        9,
        8,
        7
      ],
      "equal_variance": true
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "run_two_sample_ttest",
    "arguments": {
      "group1": [
        3,
        4,
        5,
        6,
        4
      ],
      "group2": [
        7,
        8,
        9,
        8,
        7
      ],
      "equal_variance": true
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "run_two_sample_ttest",
    "arguments": {
      "equal_variance": true,
      "group1": [
        3,
        4,
        5,
        6,
        4
      ],
      "group2": [
        7,
        8,
        9,
        8,
        7
      ]
    }
  }
]</pre>

</details>

## simple_python_121

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.580727 | 178 |
| Qwen3.8-27B | 正确 | 3.805016 | 142 |
| gemma-4-26B-A4B-it | 正确 | 0.31382 | 34 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Calculate the probability of observing 60 heads if I flip a coin 100 times with probability of heads 0.5.</pre>

### Official accepted answer

<pre>[
  {
    "calc_binomial_prob": {
      "num_trials": [
        100
      ],
      "num_success": [
        60
      ],
      "prob_success": [
        0.5
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
    "name": "calc_binomial_prob",
    "arguments": {
      "num_trials": 100,
      "num_success": 60,
      "prob_success": 0.5
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "calc_binomial_prob",
    "arguments": {
      "num_trials": 100,
      "num_success": 60,
      "prob_success": 0.5
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "calc_binomial_prob",
    "arguments": {
      "num_success": 60,
      "num_trials": 100,
      "prob_success": 0.5
    }
  }
]</pre>

</details>

## simple_python_122

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.455413 | 165 |
| Qwen3.8-27B | 正确 | 2.674683 | 96 |
| gemma-4-26B-A4B-it | 正确 | 0.271036 | 27 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Perform a Chi-Squared test for independence on a 2x2 contingency table [ [10, 20], [30, 40] ]</pre>

### Official accepted answer

<pre>[
  {
    "chi_squared_test": {
      "table": [
        [
          [
            10,
            20
          ],
          [
            30,
            40
          ]
        ]
      ],
      "alpha": [
        0.05,
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
    "name": "chi_squared_test",
    "arguments": {
      "table": [
        [
          10,
          20
        ],
        [
          30,
          40
        ]
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
    "name": "chi_squared_test",
    "arguments": {
      "table": [
        [
          10,
          20
        ],
        [
          30,
          40
        ]
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
    "name": "chi_squared_test",
    "arguments": {
      "table": [
        [
          10,
          20
        ],
        [
          30,
          40
        ]
      ]
    }
  }
]</pre>

</details>

## simple_python_123

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.592218 | 301 |
| Qwen3.8-27B | 正确 | 7.700142 | 299 |
| gemma-4-26B-A4B-it | 正确 | 0.575377 | 69 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Perform a two-sample t-test to determine if there is a significant difference between the mean of group1 (e.g., 12.4, 15.6, 11.2, 18.9) and group2 (e.g., 10.5, 9.8, 15.2, 13.8) at the significance level 0.05.</pre>

### Official accepted answer

<pre>[
  {
    "hypothesis_testing.two_sample_t_test": {
      "group1": [
        [
          12.4,
          15.6,
          11.2,
          18.9
        ]
      ],
      "group2": [
        [
          10.5,
          9.8,
          15.2,
          13.8
        ]
      ],
      "alpha": [
        0.05,
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
    "name": "hypothesis_testing_two_sample_t_test",
    "arguments": {
      "group1": [
        12.4,
        15.6,
        11.2,
        18.9
      ],
      "group2": [
        10.5,
        9.8,
        15.2,
        13.8
      ],
      "alpha": 0.05
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "hypothesis_testing_two_sample_t_test",
    "arguments": {
      "group1": [
        12.4,
        15.6,
        11.2,
        18.9
      ],
      "group2": [
        10.5,
        9.8,
        15.2,
        13.8
      ],
      "alpha": 0.05
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "hypothesis_testing_two_sample_t_test",
    "arguments": {
      "alpha": 0.05,
      "group1": [
        12.4,
        15.6,
        11.2,
        18.9
      ],
      "group2": [
        10.5,
        9.8,
        15.2,
        13.8
      ]
    }
  }
]</pre>

</details>

## simple_python_124

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.82098 | 211 |
| Qwen3.8-27B | 正确 | 3.306343 | 122 |
| gemma-4-26B-A4B-it | 正确 | 0.323689 | 35 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find the statistical significance between two set of variables, dataset_A with the values 12, 24, 36 and dataset_B with the values 15, 30, 45.</pre>

### Official accepted answer

<pre>[
  {
    "t_test": {
      "dataset_A": [
        [
          12,
          24,
          36
        ]
      ],
      "dataset_B": [
        [
          15,
          30,
          45
        ]
      ],
      "alpha": [
        0.05,
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
    "name": "t_test",
    "arguments": {
      "dataset_A": [
        12,
        24,
        36
      ],
      "dataset_B": [
        15,
        30,
        45
      ],
      "alpha": 0.05
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "t_test",
    "arguments": {
      "dataset_A": [
        12,
        24,
        36
      ],
      "dataset_B": [
        15,
        30,
        45
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
    "name": "t_test",
    "arguments": {
      "dataset_A": [
        12,
        24,
        36
      ],
      "dataset_B": [
        15,
        30,
        45
      ]
    }
  }
]</pre>

</details>

## simple_python_125

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.718893 | 197 |
| Qwen3.8-27B | 正确 | 3.179645 | 119 |
| gemma-4-26B-A4B-it | 正确 | 0.329065 | 36 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Predict house price in San Francisco based on its area of 2500 square feet, number of rooms as 5 and year of construction is 1990.</pre>

### Official accepted answer

<pre>[
  {
    "predict_house_price": {
      "area": [
        2500
      ],
      "rooms": [
        5
      ],
      "year": [
        1990
      ],
      "location": [
        "San Francisco",
        "SF"
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
    "name": "predict_house_price",
    "arguments": {
      "area": 2500,
      "rooms": 5,
      "year": 1990,
      "location": "San Francisco"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "predict_house_price",
    "arguments": {
      "area": 2500,
      "rooms": 5,
      "year": 1990,
      "location": "San Francisco"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "predict_house_price",
    "arguments": {
      "area": 2500,
      "location": "San Francisco",
      "rooms": 5,
      "year": 1990
    }
  }
]</pre>

</details>

## simple_python_126

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.820464 | 207 |
| Qwen3.8-27B | 正确 | 5.976171 | 231 |
| gemma-4-26B-A4B-it | 正确 | 0.469752 | 55 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What is the coefficient of determination (R-squared) for a model using engine size and fuel economy variables to predict car_price with a dataset in path C:/data/cars.csv?</pre>

### Official accepted answer

<pre>[
  {
    "linear_regression.get_r_squared": {
      "dataset_path": [
        "C:/data/cars.csv"
      ],
      "independent_variables": [
        [
          "engine_size",
          "fuel_economy"
        ]
      ],
      "dependent_variable": [
        "car_price"
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
    "name": "linear_regression_get_r_squared",
    "arguments": {
      "dataset_path": "C:/data/cars.csv",
      "independent_variables": [
        "engine size",
        "fuel economy"
      ],
      "dependent_variable": "car_price"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "linear_regression_get_r_squared",
    "arguments": {
      "dataset_path": "C:/data/cars.csv",
      "independent_variables": [
        "engine_size",
        "fuel_economy"
      ],
      "dependent_variable": "car_price"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "linear_regression_get_r_squared",
    "arguments": {
      "dataset_path": "C:/data/cars.csv",
      "dependent_variable": "car_price",
      "independent_variables": [
        "engine_size",
        "fuel_economy"
      ]
    }
  }
]</pre>

</details>

## simple_python_127

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.941107 | 223 |
| Qwen3.8-27B | 正确 | 4.079978 | 154 |
| gemma-4-26B-A4B-it | 正确 | 0.412693 | 47 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find the Net Present Value (NPV) of an investment, given cash_flows=[200,300,400,500], a discount rate of 10%, and an initial investment of $2000.</pre>

### Official accepted answer

<pre>[
  {
    "calculate_NPV": {
      "cash_flows": [
        [
          200,
          300,
          400,
          500
        ]
      ],
      "discount_rate": [
        0.1
      ],
      "initial_investment": [
        2000
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
    "name": "calculate_NPV",
    "arguments": {
      "cash_flows": [
        200,
        300,
        400,
        500
      ],
      "discount_rate": 0.1,
      "initial_investment": 2000
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_NPV",
    "arguments": {
      "cash_flows": [
        200,
        300,
        400,
        500
      ],
      "discount_rate": 0.1,
      "initial_investment": 2000
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_NPV",
    "arguments": {
      "cash_flows": [
        200,
        300,
        400,
        500
      ],
      "discount_rate": 0.1,
      "initial_investment": 2000
    }
  }
]</pre>

</details>

## simple_python_128

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.040374 | 238 |
| Qwen3.8-27B | 正确 | 3.816002 | 144 |
| gemma-4-26B-A4B-it | 正确 | 0.404995 | 46 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What's the quarterly dividend per share of a company with 100 million outstanding shares and total dividend payout of 50 million USD?</pre>

### Official accepted answer

<pre>[
  {
    "finance.calculate_quarterly_dividend_per_share": {
      "total_payout": [
        50000000
      ],
      "outstanding_shares": [
        100000000
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
    "name": "finance_calculate_quarterly_dividend_per_share",
    "arguments": {
      "total_payout": 50000000,
      "outstanding_shares": 100000000
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "finance_calculate_quarterly_dividend_per_share",
    "arguments": {
      "total_payout": 50000000,
      "outstanding_shares": 100000000
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "finance_calculate_quarterly_dividend_per_share",
    "arguments": {
      "outstanding_shares": 100000000,
      "total_payout": 50000000
    }
  }
]</pre>

</details>

## simple_python_129

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.97213 | 228 |
| Qwen3.8-27B | 正确 | 12.098539 | 476 |
| gemma-4-26B-A4B-it | 正确 | 0.322246 | 35 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Calculate the discounted cash flow of a bond that is giving a coupon payment of $100 annually for next 5 years with discount rate 4%.</pre>

### Official accepted answer

<pre>[
  {
    "calculate_discounted_cash_flow": {
      "coupon_payment": [
        100
      ],
      "period": [
        5
      ],
      "discount_rate": [
        0.04
      ],
      "face_value": [
        "",
        1000
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
    "name": "calculate_discounted_cash_flow",
    "arguments": {
      "coupon_payment": 100,
      "period": 5,
      "discount_rate": 0.04,
      "face_value": 1000
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_discounted_cash_flow",
    "arguments": {
      "coupon_payment": 100,
      "period": 5,
      "discount_rate": 0.04
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_discounted_cash_flow",
    "arguments": {
      "coupon_payment": 100,
      "discount_rate": 0.04,
      "period": 5
    }
  }
]</pre>

</details>

## simple_python_130

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.822965 | 328 |
| Qwen3.8-27B | 错误 | 6.867944 | 265 |
| gemma-4-26B-A4B-it | 正确 | 0.522621 | 62 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What's the NPV (Net Present Value) of a series of cash flows: [-50000, 10000, 15000, 20000, 25000, 30000] discounted at 8% annually?</pre>

### Official accepted answer

<pre>[
  {
    "finance_calculator.npv": {
      "cash_flows": [
        [
          -50000,
          10000,
          15000,
          20000,
          25000,
          30000
        ]
      ],
      "discount_rate": [
        0.08
      ],
      "years": [
        "",
        []
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
    "name": "finance_calculator_npv",
    "arguments": {
      "cash_flows": [
        -50000,
        10000,
        15000,
        20000,
        25000,
        30000
      ],
      "discount_rate": 0.08
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "finance_calculator_npv",
    "arguments": {
      "cash_flows": [
        -50000,
        10000,
        15000,
        20000,
        25000,
        30000
      ],
      "discount_rate": 0.08,
      "years": [
        0,
        1,
        2,
        3,
        4,
        5
      ]
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'years': [0, 1, 2, 3, 4, 5]. Expected one of ['', []]."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "finance_calculator_npv",
    "arguments": {
      "cash_flows": [
        -50000,
        10000,
        15000,
        20000,
        25000,
        30000
      ],
      "discount_rate": 0.08
    }
  }
]</pre>

</details>

## simple_python_131

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.922267 | 221 |
| Qwen3.8-27B | 正确 | 3.570158 | 133 |
| gemma-4-26B-A4B-it | 正确 | 0.324612 | 35 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Calculate the compound interest for an initial principal amount of $10000, with an annual interest rate of 5% and the number of times interest applied per time period is 4 and the time the money is invested for 10 years.</pre>

### Official accepted answer

<pre>[
  {
    "calculate_compound_interest": {
      "principal": [
        10000
      ],
      "rate": [
        0.05
      ],
      "time": [
        10
      ],
      "n": [
        4
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
    "name": "calculate_compound_interest",
    "arguments": {
      "principal": 10000,
      "rate": 0.05,
      "time": 10,
      "n": 4
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_compound_interest",
    "arguments": {
      "principal": 10000,
      "rate": 0.05,
      "time": 10,
      "n": 4
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_compound_interest",
    "arguments": {
      "n": 4,
      "principal": 10000,
      "rate": 0.05,
      "time": 10
    }
  }
]</pre>

</details>

## simple_python_132

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.110119 | 245 |
| Qwen3.8-27B | 正确 | 4.867264 | 184 |
| gemma-4-26B-A4B-it | 正确 | 0.443556 | 51 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Calculate the company's return on equity given its net income of $2,000,000, shareholder's equity of $10,000,000, and dividends paid of $200,000.</pre>

### Official accepted answer

<pre>[
  {
    "calculate_return_on_equity": {
      "net_income": [
        2000000
      ],
      "shareholder_equity": [
        10000000
      ],
      "dividends_paid": [
        200000
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
    "name": "calculate_return_on_equity",
    "arguments": {
      "net_income": 2000000,
      "shareholder_equity": 10000000,
      "dividends_paid": 200000
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_return_on_equity",
    "arguments": {
      "net_income": 2000000,
      "shareholder_equity": 10000000,
      "dividends_paid": 200000
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_return_on_equity",
    "arguments": {
      "dividends_paid": 200000,
      "net_income": 2000000,
      "shareholder_equity": 10000000
    }
  }
]</pre>

</details>

## simple_python_133

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.004926 | 229 |
| Qwen3.8-27B | 正确 | 4.470286 | 170 |
| gemma-4-26B-A4B-it | 正确 | 0.442691 | 51 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Predict the future value of a $5000 investment with an annual interest rate of 5% in 3 years with monthly compounding.</pre>

### Official accepted answer

<pre>[
  {
    "finance.predict_future_value": {
      "present_value": [
        5000
      ],
      "annual_interest_rate": [
        0.05
      ],
      "compounding_periods_per_year": [
        12
      ],
      "time_years": [
        3
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
    "name": "finance_predict_future_value",
    "arguments": {
      "present_value": 5000,
      "annual_interest_rate": 0.05,
      "time_years": 3,
      "compounding_periods_per_year": 12
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "finance_predict_future_value",
    "arguments": {
      "present_value": 5000,
      "annual_interest_rate": 0.05,
      "compounding_periods_per_year": 12,
      "time_years": 3
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "finance_predict_future_value",
    "arguments": {
      "annual_interest_rate": 0.05,
      "compounding_periods_per_year": 12,
      "present_value": 5000,
      "time_years": 3
    }
  }
]</pre>

</details>

## simple_python_134

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.505675 | 173 |
| Qwen3.8-27B | 正确 | 4.972867 | 191 |
| gemma-4-26B-A4B-it | 正确 | 0.299716 | 32 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Predict the total expected profit of stocks XYZ in 5 years given I have invested $5000 and annual return rate is 7%.</pre>

### Official accepted answer

<pre>[
  {
    "investment.predictProfit": {
      "investment_amount": [
        5000
      ],
      "annual_return": [
        0.07
      ],
      "years": [
        5
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
    "name": "investment_predictProfit",
    "arguments": {
      "investment_amount": 5000,
      "annual_return": 0.07,
      "years": 5
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "investment_predictProfit",
    "arguments": {
      "investment_amount": 5000,
      "annual_return": 0.07,
      "years": 5
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "investment_predictProfit",
    "arguments": {
      "annual_return": 0.07,
      "investment_amount": 5000,
      "years": 5
    }
  }
]</pre>

</details>

## simple_python_135

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.372106 | 157 |
| Qwen3.8-27B | 正确 | 3.667598 | 134 |
| gemma-4-26B-A4B-it | 正确 | 0.295985 | 31 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Calculate the return on investment for a stock bought at $20, sold at $25, with a dividend of $2.</pre>

### Official accepted answer

<pre>[
  {
    "calculate_return_on_investment": {
      "purchase_price": [
        20
      ],
      "sale_price": [
        25
      ],
      "dividend": [
        2
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
    "name": "calculate_return_on_investment",
    "arguments": {
      "purchase_price": 20,
      "sale_price": 25,
      "dividend": 2
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_return_on_investment",
    "arguments": {
      "purchase_price": 20,
      "sale_price": 25,
      "dividend": 2
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_return_on_investment",
    "arguments": {
      "dividend": 2,
      "purchase_price": 20,
      "sale_price": 25
    }
  }
]</pre>

</details>

## simple_python_136

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.754163 | 202 |
| Qwen3.8-27B | 正确 | 4.273321 | 162 |
| gemma-4-26B-A4B-it | 正确 | 0.393836 | 40 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find the compound interest for an investment of $10000 with an annual interest rate of 5% compounded monthly for 5 years.</pre>

### Official accepted answer

<pre>[
  {
    "compound_interest": {
      "principal": [
        10000
      ],
      "annual_rate": [
        5.0
      ],
      "compounding_freq": [
        "monthly"
      ],
      "time_in_years": [
        5
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
    "name": "compound_interest",
    "arguments": {
      "principal": 10000,
      "annual_rate": 5,
      "compounding_freq": "monthly",
      "time_in_years": 5
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "compound_interest",
    "arguments": {
      "principal": 10000,
      "annual_rate": 5,
      "compounding_freq": "monthly",
      "time_in_years": 5
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "compound_interest",
    "arguments": {
      "annual_rate": 5,
      "compounding_freq": "monthly",
      "principal": 10000,
      "time_in_years": 5
    }
  }
]</pre>

</details>

## simple_python_137

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.376232 | 156 |
| Qwen3.8-27B | 正确 | 5.208033 | 199 |
| gemma-4-26B-A4B-it | 正确 | 0.340353 | 37 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Calculate the projected return on a $5000 investment in ABC company's stock, if the expected annual growth rate is 6% and the holding period is 5 years.</pre>

### Official accepted answer

<pre>[
  {
    "calculate_stock_return": {
      "investment_amount": [
        5000
      ],
      "annual_growth_rate": [
        0.06
      ],
      "holding_period": [
        5
      ],
      "dividends": [
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
    "name": "calculate_stock_return",
    "arguments": {
      "investment_amount": 5000,
      "annual_growth_rate": 0.06,
      "holding_period": 5
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_stock_return",
    "arguments": {
      "investment_amount": 5000,
      "annual_growth_rate": 0.06,
      "holding_period": 5
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_stock_return",
    "arguments": {
      "annual_growth_rate": 0.06,
      "holding_period": 5,
      "investment_amount": 5000
    }
  }
]</pre>

</details>

## simple_python_138

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.774889 | 204 |
| Qwen3.8-27B | 正确 | 3.721638 | 141 |
| gemma-4-26B-A4B-it | 正确 | 0.376523 | 42 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Calculate the future value of my portfolio if I invest $5000 in stock 'X' with an expected annual return of 5% for 7 years.</pre>

### Official accepted answer

<pre>[
  {
    "portfolio_future_value": {
      "stock": [
        "X"
      ],
      "invested_amount": [
        5000
      ],
      "expected_annual_return": [
        0.05
      ],
      "years": [
        7
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
    "name": "portfolio_future_value",
    "arguments": {
      "stock": "X",
      "invested_amount": 5000,
      "expected_annual_return": 0.05,
      "years": 7
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "portfolio_future_value",
    "arguments": {
      "stock": "X",
      "invested_amount": 5000,
      "expected_annual_return": 0.05,
      "years": 7
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "portfolio_future_value",
    "arguments": {
      "expected_annual_return": 0.05,
      "invested_amount": 5000,
      "stock": "X",
      "years": 7
    }
  }
]</pre>

</details>

## simple_python_139

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.713577 | 194 |
| Qwen3.8-27B | 正确 | 3.414353 | 123 |
| gemma-4-26B-A4B-it | 正确 | 0.319904 | 32 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What is the estimated return on a mutual fund, given that it has a yearly yield of 5%, an investment amount of $2000 and a time period of 3 years?</pre>

### Official accepted answer

<pre>[
  {
    "estimate_mutual_fund_return": {
      "yearly_yield": [
        5.0
      ],
      "investment_amount": [
        2000
      ],
      "years": [
        3
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
    "name": "estimate_mutual_fund_return",
    "arguments": {
      "yearly_yield": 5,
      "investment_amount": 2000,
      "years": 3
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "estimate_mutual_fund_return",
    "arguments": {
      "yearly_yield": 5,
      "investment_amount": 2000,
      "years": 3
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "estimate_mutual_fund_return",
    "arguments": {
      "investment_amount": 2000,
      "yearly_yield": 5,
      "years": 3
    }
  }
]</pre>

</details>

## simple_python_140

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.241944 | 141 |
| Qwen3.8-27B | 正确 | 3.001758 | 112 |
| gemma-4-26B-A4B-it | 正确 | 0.323634 | 36 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Calculate the Compound Annual Growth Rate (CAGR) for an initial investment of $2000, final value of $3000 in a period of 4 years.</pre>

### Official accepted answer

<pre>[
  {
    "calculate_cagr": {
      "initial_value": [
        2000
      ],
      "final_value": [
        3000
      ],
      "period_in_years": [
        4
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
    "name": "calculate_cagr",
    "arguments": {
      "initial_value": 2000,
      "final_value": 3000,
      "period_in_years": 4
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_cagr",
    "arguments": {
      "initial_value": 2000,
      "final_value": 3000,
      "period_in_years": 4
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_cagr",
    "arguments": {
      "final_value": 3000,
      "initial_value": 2000,
      "period_in_years": 4
    }
  }
]</pre>

</details>

## simple_python_141

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 0.910298 | 101 |
| Qwen3.8-27B | 正确 | 2.199437 | 80 |
| gemma-4-26B-A4B-it | 正确 | 0.223697 | 23 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Get current Gold price per ounce.</pre>

### Official accepted answer

<pre>[
  {
    "get_metal_price": {
      "metal": [
        "Gold",
        "gold"
      ],
      "measure": [
        "ounce"
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
    "name": "get_metal_price",
    "arguments": {
      "metal": "Gold",
      "measure": "ounce"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_metal_price",
    "arguments": {
      "metal": "Gold",
      "measure": "ounce"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_metal_price",
    "arguments": {
      "measure": "ounce",
      "metal": "Gold"
    }
  }
]</pre>

</details>

## simple_python_142

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.382218 | 157 |
| Qwen3.8-27B | 正确 | 3.266389 | 122 |
| gemma-4-26B-A4B-it | 正确 | 0.349622 | 40 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find the NASDAQ stock price for the company Amazon at closing March.11, 2022.</pre>

### Official accepted answer

<pre>[
  {
    "get_stock_price": {
      "company_name": [
        "Amazon",
        "AMZN"
      ],
      "date": [
        "2022-03-11"
      ],
      "exchange": [
        "NASDAQ",
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
    "name": "get_stock_price",
    "arguments": {
      "company_name": "Amazon",
      "date": "2022-03-11",
      "exchange": "NASDAQ"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_stock_price",
    "arguments": {
      "company_name": "Amazon",
      "date": "2022-03-11",
      "exchange": "NASDAQ"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_stock_price",
    "arguments": {
      "company_name": "Amazon",
      "date": "2022-03-11",
      "exchange": "NASDAQ"
    }
  }
]</pre>

</details>

## simple_python_143

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.286761 | 145 |
| Qwen3.8-27B | 正确 | 2.589472 | 94 |
| gemma-4-26B-A4B-it | 正确 | 0.253202 | 27 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: 'Get stock price of Apple for the last 5 days in NASDAQ.'</pre>

### Official accepted answer

<pre>[
  {
    "get_stock_price": {
      "company": [
        "AAPL"
      ],
      "days": [
        5
      ],
      "exchange": [
        "NASDAQ",
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
    "name": "get_stock_price",
    "arguments": {
      "company": "AAPL",
      "days": 5,
      "exchange": "NASDAQ"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_stock_price",
    "arguments": {
      "company": "AAPL",
      "days": 5,
      "exchange": "NASDAQ"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_stock_price",
    "arguments": {
      "company": "AAPL",
      "days": 5,
      "exchange": "NASDAQ"
    }
  }
]</pre>

</details>

## simple_python_144

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.640064 | 186 |
| Qwen3.8-27B | 正确 | 4.115829 | 156 |
| gemma-4-26B-A4B-it | 正确 | 0.307076 | 34 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find the market performance of the S&amp;P 500 and the Dow Jones over the past 5 days.</pre>

### Official accepted answer

<pre>[
  {
    "market_performance.get_data": {
      "indexes": [
        [
          "S&amp;P 500",
          "Dow Jones"
        ]
      ],
      "days": [
        5
      ],
      "detailed": [
        "",
        true,
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
    "name": "market_performance_get_data",
    "arguments": {
      "indexes": [
        "S&amp;P 500",
        "Dow Jones"
      ],
      "days": 5,
      "detailed": false
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "market_performance_get_data",
    "arguments": {
      "indexes": [
        "S&amp;P 500",
        "Dow Jones"
      ],
      "days": 5
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "market_performance_get_data",
    "arguments": {
      "days": 5,
      "indexes": [
        "S&amp;P 500",
        "Dow Jones"
      ]
    }
  }
]</pre>

</details>

## simple_python_145

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 错误 | 1.513938 | 171 |
| Qwen3.8-27B | 正确 | 3.605773 | 132 |
| gemma-4-26B-A4B-it | 正确 | 0.299869 | 33 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Calculate the compounded interest for an initial principal of $5000, annual interest rate of 5%, and compounding period of 10 years.</pre>

### Official accepted answer

<pre>[
  {
    "calculate_compounded_interest": {
      "principal": [
        5000
      ],
      "interest_rate": [
        0.05
      ],
      "period": [
        10
      ],
      "compounding_frequency": [
        "Annually",
        ""
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
    "name": "calculate_compounded_interest",
    "arguments": {
      "principal": 5000,
      "interest_rate": 5,
      "period": 10,
      "compounding_frequency": "Annually"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'interest_rate': 5.0. Expected one of [0.05]."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_compounded_interest",
    "arguments": {
      "principal": 5000,
      "interest_rate": 0.05,
      "period": 10
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_compounded_interest",
    "arguments": {
      "interest_rate": 0.05,
      "period": 10,
      "principal": 5000
    }
  }
]</pre>

</details>

## simple_python_146

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.234743 | 141 |
| Qwen3.8-27B | 正确 | 2.262236 | 83 |
| gemma-4-26B-A4B-it | 正确 | 0.194967 | 19 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What's the price of Amazon stock for the last 3 days?</pre>

### Official accepted answer

<pre>[
  {
    "stock_price": {
      "company": [
        "Amazon",
        "AMZN"
      ],
      "days": [
        3
      ],
      "data_type": [
        "Close",
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
    "name": "stock_price",
    "arguments": {
      "company": "Amazon",
      "days": 3
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "stock_price",
    "arguments": {
      "company": "Amazon",
      "days": 3
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "stock_price",
    "arguments": {
      "company": "Amazon",
      "days": 3
    }
  }
]</pre>

</details>

## simple_python_147

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.315826 | 151 |
| Qwen3.8-27B | 正确 | 2.406669 | 88 |
| gemma-4-26B-A4B-it | 正确 | 0.261748 | 28 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Retrieve stock prices of Microsoft and Google for the last 2 weeks.</pre>

### Official accepted answer

<pre>[
  {
    "get_stock_prices": {
      "companies": [
        [
          "Microsoft",
          "Google"
        ]
      ],
      "duration": [
        "2 weeks"
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
    "name": "get_stock_prices",
    "arguments": {
      "companies": [
        "Microsoft",
        "Google"
      ],
      "duration": "2 weeks"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_stock_prices",
    "arguments": {
      "companies": [
        "Microsoft",
        "Google"
      ],
      "duration": "2 weeks"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_stock_prices",
    "arguments": {
      "companies": [
        "Microsoft",
        "Google"
      ],
      "duration": "2 weeks"
    }
  }
]</pre>

</details>

## simple_python_148

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.885432 | 218 |
| Qwen3.8-27B | 正确 | 3.849746 | 145 |
| gemma-4-26B-A4B-it | 正确 | 0.336302 | 38 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Calculate the future value of an investment with an annual rate of return of 8%, an initial investment of $20000, and a time frame of 5 years.</pre>

### Official accepted answer

<pre>[
  {
    "finance.calculate_future_value": {
      "initial_investment": [
        20000
      ],
      "rate_of_return": [
        0.08
      ],
      "years": [
        5
      ],
      "contribution": [
        "",
        0
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
    "name": "finance_calculate_future_value",
    "arguments": {
      "initial_investment": 20000,
      "rate_of_return": 0.08,
      "years": 5
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "finance_calculate_future_value",
    "arguments": {
      "initial_investment": 20000,
      "rate_of_return": 0.08,
      "years": 5
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "finance_calculate_future_value",
    "arguments": {
      "initial_investment": 20000,
      "rate_of_return": 0.08,
      "years": 5
    }
  }
]</pre>

</details>

## simple_python_149

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 0.811337 | 90 |
| Qwen3.8-27B | 正确 | 2.541821 | 94 |
| gemma-4-26B-A4B-it | 正确 | 0.222597 | 23 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What's the current stock price of Apple and Microsoft?</pre>

### Official accepted answer

<pre>[
  {
    "get_stock_price": {
      "company_names": [
        [
          "Apple",
          "Microsoft"
        ],
        [
          [
            "Apple"
          ],
          [
            "Microsoft"
          ]
        ],
        [
          "AAPL",
          "MSFT"
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
    "name": "get_stock_price",
    "arguments": {
      "company_names": [
        "Apple",
        "Microsoft"
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
    "name": "get_stock_price",
    "arguments": {
      "company_names": [
        "Apple",
        "Microsoft"
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
    "name": "get_stock_price",
    "arguments": {
      "company_names": [
        "Apple",
        "Microsoft"
      ]
    }
  }
]</pre>

</details>


[Category index](README.md) · [All categories](../README.md) · [Previous](page-004.md) · [Next](page-006.md)
