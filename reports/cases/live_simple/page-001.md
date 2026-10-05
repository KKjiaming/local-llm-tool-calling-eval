# live_simple — page 1/9

[Category index](README.md) · [All categories](../README.md) · [Next](page-002.md)

30 cases. Expand the question/answer and model sections below. Tool calls were scored, not executed.

## live_simple_0-0-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.585486 | 179 |
| Qwen3.8-27B | 正确 | 2.444786 | 92 |
| gemma-4-26B-A4B-it | 正确 | 0.256097 | 26 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Can you retrieve the details for the user with the ID 7890, who has black as their special request?</pre>

### Official accepted answer

<pre>[
  {
    "get_user_info": {
      "user_id": [
        7890
      ],
      "special": [
        "black"
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
    "name": "get_user_info",
    "arguments": {
      "user_id": 7890,
      "special": "black"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_user_info",
    "arguments": {
      "user_id": 7890,
      "special": "black"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_user_info",
    "arguments": {
      "special": "black",
      "user_id": 7890
    }
  }
]</pre>

</details>

## live_simple_1-1-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.646372 | 183 |
| Qwen3.8-27B | 正确 | 3.600573 | 139 |
| gemma-4-26B-A4B-it | 正确 | 0.343421 | 37 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I want to see the star history of ShishirPatil/gorilla and gorilla-llm/gorilla-cli, with the timelines aligned, so that I can more clearly observe the rate of change from their initial releases.</pre>

### Official accepted answer

<pre>[
  {
    "github_star": {
      "repos": [
        "ShishirPatil/gorilla,gorilla-llm/gorilla-cli"
      ],
      "aligned": [
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
    "name": "github_star",
    "arguments": {
      "repos": "ShishirPatil/gorilla,gorilla-llm/gorilla-cli",
      "aligned": true
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "github_star",
    "arguments": {
      "repos": "ShishirPatil/gorilla,gorilla-llm/gorilla-cli",
      "aligned": true
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "github_star",
    "arguments": {
      "aligned": true,
      "repos": "ShishirPatil/gorilla,gorilla-llm/gorilla-cli"
    }
  }
]</pre>

</details>

## live_simple_2-2-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.856993 | 208 |
| Qwen3.8-27B | 正确 | 3.838432 | 149 |
| gemma-4-26B-A4B-it | 正确 | 0.347417 | 38 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I need a Comfort Uber ride from 2020 Addison Street, Berkeley, CA, USA, and I can wait up to 600 seconds for it.</pre>

### Official accepted answer

<pre>[
  {
    "uber.ride": {
      "loc": [
        "2020 Addison Street, Berkeley, CA, USA"
      ],
      "type": [
        "comfort"
      ],
      "time": [
        600
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
    "name": "uber_ride",
    "arguments": {
      "loc": "2020 Addison Street, Berkeley, CA, USA",
      "type": "comfort",
      "time": 600
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "uber_ride",
    "arguments": {
      "loc": "2020 Addison Street, Berkeley, CA, USA",
      "type": "comfort",
      "time": 600
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "uber_ride",
    "arguments": {
      "loc": "2020 Addison Street, Berkeley, CA, USA",
      "time": 600,
      "type": "comfort"
    }
  }
]</pre>

</details>

## live_simple_3-2-1

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.893223 | 216 |
| Qwen3.8-27B | 正确 | 5.172078 | 204 |
| gemma-4-26B-A4B-it | 正确 | 0.344973 | 38 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I need a 'Plus' type Uber from 221B Baker Street, Berkeley, CA, USA, and I can wait up to 600 seconds for it. </pre>

### Official accepted answer

<pre>[
  {
    "uber.ride": {
      "loc": [
        "221B Baker Street, Berkeley, CA, USA"
      ],
      "type": [
        "plus"
      ],
      "time": [
        600
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
    "name": "uber_ride",
    "arguments": {
      "loc": "221B Baker Street, Berkeley, CA, USA",
      "type": "plus",
      "time": 600
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "uber_ride",
    "arguments": {
      "loc": "221B Baker Street, Berkeley, CA, USA",
      "type": "plus",
      "time": 600
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "uber_ride",
    "arguments": {
      "loc": "221B Baker Street, Berkeley, CA, USA",
      "time": 600,
      "type": "plus"
    }
  }
]</pre>

</details>

## live_simple_4-3-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.753573 | 195 |
| Qwen3.8-27B | 正确 | 2.929105 | 112 |
| gemma-4-26B-A4B-it | 正确 | 0.26036 | 27 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What are the current weather conditions in Tel Aviv, and could you provide that in Fahrenheit, please?</pre>

### Official accepted answer

<pre>[
  {
    "get_current_weather": {
      "location": [
        "Tel Aviv, Israel"
      ],
      "unit": [
        "fahrenheit",
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
    "name": "get_current_weather",
    "arguments": {
      "location": "Tel Aviv, Israel",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Tel Aviv, Israel",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Tel Aviv, Israel",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

## live_simple_5-3-1

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.479097 | 164 |
| Qwen3.8-27B | 正确 | 3.956589 | 154 |
| gemma-4-26B-A4B-it | 正确 | 0.267753 | 28 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Qual a temperatura atual em Divinópolis, MG? fahrenheit</pre>

### Official accepted answer

<pre>[
  {
    "get_current_weather": {
      "location": [
        "Divinópolis, MG"
      ],
      "unit": [
        "fahrenheit",
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
    "name": "get_current_weather",
    "arguments": {
      "location": "Divinópolis, MG",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Divinópolis, MG",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Divinópolis, MG",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

## live_simple_6-3-2

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.166743 | 128 |
| Qwen3.8-27B | 正确 | 2.381112 | 89 |
| gemma-4-26B-A4B-it | 正确 | 0.263995 | 27 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Can you tell me the weather in fahrenheit so that I decide if I need to wear a jacket today? San Francisco</pre>

### Official accepted answer

<pre>[
  {
    "get_current_weather": {
      "location": [
        "San Francisco, CA"
      ],
      "unit": [
        "fahrenheit",
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
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

## live_simple_7-3-3

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.656999 | 187 |
| Qwen3.8-27B | 正确 | 2.960072 | 113 |
| gemma-4-26B-A4B-it | 正确 | 0.198239 | 19 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Im at Riga, Latvia, Can you tell me the current temperature?</pre>

### Official accepted answer

<pre>[
  {
    "get_current_weather": {
      "location": [
        "Riga, Latvia"
      ],
      "unit": [
        "fahrenheit",
        "",
        "celsius"
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
    "name": "get_current_weather",
    "arguments": {
      "location": "Riga, Latvia"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Riga, Latvia",
      "unit": "celsius"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Riga, Latvia"
    }
  }
]</pre>

</details>

## live_simple_8-3-4

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.752478 | 198 |
| Qwen3.8-27B | 正确 | 2.87984 | 110 |
| gemma-4-26B-A4B-it | 正确 | 0.251664 | 26 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I want to know weather conditions? I'm at London, UK in fahr</pre>

### Official accepted answer

<pre>[
  {
    "get_current_weather": {
      "location": [
        "London, UK",
        "London, England"
      ],
      "unit": [
        "fahrenheit",
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
    "name": "get_current_weather",
    "arguments": {
      "location": "London, UK",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "London, UK",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "London, UK",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

## live_simple_9-3-5

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.921606 | 219 |
| Qwen3.8-27B | 正确 | 2.654931 | 100 |
| gemma-4-26B-A4B-it | 正确 | 0.252937 | 26 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What's weather in Hyderabad in Fahrenheit</pre>

### Official accepted answer

<pre>[
  {
    "get_current_weather": {
      "location": [
        "Hyderabad, India"
      ],
      "unit": [
        "fahrenheit",
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
    "name": "get_current_weather",
    "arguments": {
      "location": "Hyderabad, India",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Hyderabad, India",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Hyderabad, India",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

## live_simple_10-3-6

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 错误 | 1.544096 | 173 |
| Qwen3.8-27B | 正确 | 2.707706 | 102 |
| gemma-4-26B-A4B-it | 正确 | 0.262685 | 27 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Could you tell me the current weather in Yosemite National Park which locates at Mariposa, CA, and make sure to give me the temperature in Celsius?</pre>

### Official accepted answer

<pre>[
  {
    "get_current_weather": {
      "location": [
        "Mariposa, CA"
      ],
      "unit": [
        "celsius"
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
    "name": "get_current_weather",
    "arguments": {
      "location": "Yosemite National Park, CA",
      "unit": "celsius"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'location': 'Yosemite National Park, CA'. Expected one of ['Mariposa, CA']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Mariposa, CA",
      "unit": "celsius"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Mariposa, CA",
      "unit": "celsius"
    }
  }
]</pre>

</details>

## live_simple_11-3-7

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.299011 | 144 |
| Qwen3.8-27B | 正确 | 1.756009 | 63 |
| gemma-4-26B-A4B-it | 正确 | 0.207392 | 20 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Could you tell me the current weather conditions in Naples, Florida?</pre>

### Official accepted answer

<pre>[
  {
    "get_current_weather": {
      "location": [
        "Naples, FL",
        "Naples, Florida"
      ],
      "unit": [
        "",
        "fahrenheit"
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
    "name": "get_current_weather",
    "arguments": {
      "location": "Naples, FL"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Naples, FL"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Naples, FL"
    }
  }
]</pre>

</details>

## live_simple_12-3-8

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.100194 | 120 |
| Qwen3.8-27B | 正确 | 2.336952 | 87 |
| gemma-4-26B-A4B-it | 正确 | 0.262837 | 27 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I'm planning a trip to New York, NY in December and will be staying for 5 days. Could you tell me the current weather conditions, and provide the temperature in Celsius?</pre>

### Official accepted answer

<pre>[
  {
    "get_current_weather": {
      "location": [
        "New York, NY"
      ],
      "unit": [
        "celsius"
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
    "name": "get_current_weather",
    "arguments": {
      "location": "New York, NY",
      "unit": "celsius"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "New York, NY",
      "unit": "celsius"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "New York, NY",
      "unit": "celsius"
    }
  }
]</pre>

</details>

## live_simple_13-3-9

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.376574 | 150 |
| Qwen3.8-27B | 正确 | 2.409455 | 90 |
| gemma-4-26B-A4B-it | 正确 | 0.255644 | 26 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: 我想知道上海目前的天气状况，可以帮我查询吗？顺便使用摄氏度来显示温度。</pre>

### Official accepted answer

<pre>[
  {
    "get_current_weather": {
      "location": [
        "Shanghai, China",
        "\\u4e0a\\u6d77,\\u4e2d\\u56fd"
      ],
      "unit": [
        "celsius"
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
    "name": "get_current_weather",
    "arguments": {
      "location": "Shanghai, China",
      "unit": "celsius"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Shanghai, China",
      "unit": "celsius"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Shanghai, China",
      "unit": "celsius"
    }
  }
]</pre>

</details>

## live_simple_14-3-10

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.570576 | 175 |
| Qwen3.8-27B | 正确 | 2.430804 | 91 |
| gemma-4-26B-A4B-it | 正确 | 0.262997 | 27 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I have a busy day today. Can you tell me what the temperature is going to be in Bangkok, Thailand. I prefer the fahrenheit unit.</pre>

### Official accepted answer

<pre>[
  {
    "get_current_weather": {
      "location": [
        "Bangkok, Thailand"
      ],
      "unit": [
        "",
        "fahrenheit"
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
    "name": "get_current_weather",
    "arguments": {
      "location": "Bangkok, Thailand",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Bangkok, Thailand",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Bangkok, Thailand",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

## live_simple_15-3-11

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.416346 | 159 |
| Qwen3.8-27B | 错误 | 3.04418 | 116 |
| gemma-4-26B-A4B-it | 错误 | 0.255313 | 26 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I'm at Bengaluru. Tell me the current weather conditions in Chennai, Tamil Nadu in fahrenheit?</pre>

### Official accepted answer

<pre>[
  {
    "get_current_weather": {
      "location": [
        "Chennai, Tamil Nadu"
      ],
      "unit": [
        "",
        "fahrenheit"
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
    "name": "get_current_weather",
    "arguments": {
      "location": "Chennai, Tamil Nadu",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Chennai, TN",
      "unit": "fahrenheit"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'location': 'Chennai, TN'. Expected one of ['Chennai, Tamil Nadu']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 错误</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Chennai, TN",
      "unit": "fahrenheit"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'location': 'Chennai, TN'. Expected one of ['Chennai, Tamil Nadu']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

## live_simple_16-3-12

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.758331 | 196 |
| Qwen3.8-27B | 正确 | 2.503684 | 94 |
| gemma-4-26B-A4B-it | 正确 | 0.267025 | 27 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Could you tell me the current weather in Lang Son in fahrenheit?</pre>

### Official accepted answer

<pre>[
  {
    "get_current_weather": {
      "location": [
        "Lang Son, Vietnam"
      ],
      "unit": [
        "",
        "fahrenheit"
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
    "name": "get_current_weather",
    "arguments": {
      "location": "Lang Son, Vietnam",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Lang Son, Vietnam",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Lang Son, Vietnam",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

## live_simple_17-3-13

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.514186 | 170 |
| Qwen3.8-27B | 正确 | 1.997743 | 73 |
| gemma-4-26B-A4B-it | 正确 | 0.254265 | 26 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: weather today in Boston in fahrenheit?</pre>

### Official accepted answer

<pre>[
  {
    "get_current_weather": {
      "location": [
        "Boston, MA"
      ],
      "unit": [
        "",
        "fahrenheit"
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
    "name": "get_current_weather",
    "arguments": {
      "location": "Boston, MA",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Boston, MA",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Boston, MA",
      "unit": "fahrenheit"
    }
  }
]</pre>

</details>

## live_simple_18-3-14

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.756906 | 196 |
| Qwen3.8-27B | 正确 | 2.768185 | 105 |
| gemma-4-26B-A4B-it | 正确 | 0.25647 | 26 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Can you tell me the current weather in Moscow, specifying the temperature in Celsius?</pre>

### Official accepted answer

<pre>[
  {
    "get_current_weather": {
      "location": [
        "Moscow, Russia"
      ],
      "unit": [
        "celsius"
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
    "name": "get_current_weather",
    "arguments": {
      "location": "Moscow, Russia",
      "unit": "celsius"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Moscow, Russia",
      "unit": "celsius"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Moscow, Russia",
      "unit": "celsius"
    }
  }
]</pre>

</details>

## live_simple_19-3-15

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.465341 | 282 |
| Qwen3.8-27B | 正确 | 5.899278 | 234 |
| gemma-4-26B-A4B-it | 正确 | 0.269756 | 28 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What's the weather in Quintana Roo, Mexico. Please tell me the answer in the superior units of temperature, by that I mean Celsius.</pre>

### Official accepted answer

<pre>[
  {
    "get_current_weather": {
      "location": [
        "Quintana Roo, Mexico"
      ],
      "unit": [
        "celsius"
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
    "name": "get_current_weather",
    "arguments": {
      "location": "Quintana Roo, Mexico",
      "unit": "celsius"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Quintana Roo, Mexico",
      "unit": "celsius"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Quintana Roo, Mexico",
      "unit": "celsius"
    }
  }
]</pre>

</details>

## live_simple_20-4-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.533367 | 175 |
| Qwen3.8-27B | 正确 | 13.409943 | 546 |
| gemma-4-26B-A4B-it | 正确 | 0.279679 | 29 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I would like to order a burger with the following modification verbatim: no onions, extra cheese</pre>

### Official accepted answer

<pre>[
  {
    "change_food": {
      "food_item": [
        "burger"
      ],
      "modification_request": [
        "no onions, extra cheese"
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
    "name": "change_food",
    "arguments": {
      "food_item": "burger",
      "modification_request": "no onions, extra cheese"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "change_food",
    "arguments": {
      "food_item": "burger",
      "modification_request": "no onions, extra cheese"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "change_food",
    "arguments": {
      "food_item": "burger",
      "modification_request": "no onions,extra cheese"
    }
  }
]</pre>

</details>

## live_simple_21-4-1

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.040726 | 114 |
| Qwen3.8-27B | 正确 | 2.938394 | 112 |
| gemma-4-26B-A4B-it | 正确 | 0.264146 | 27 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I'd like to modify my order by making the dish called 'chicken dish' to a new spice level 'extra spicy', please.</pre>

### Official accepted answer

<pre>[
  {
    "change_food": {
      "food_item": [
        "chicken dish"
      ],
      "modification_request": [
        "extra spicy"
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
    "name": "change_food",
    "arguments": {
      "food_item": "chicken dish",
      "modification_request": "extra spicy"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "change_food",
    "arguments": {
      "food_item": "chicken dish",
      "modification_request": "extra spicy"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "change_food",
    "arguments": {
      "food_item": "chicken dish",
      "modification_request": "extra spicy"
    }
  }
]</pre>

</details>

## live_simple_22-5-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.032913 | 232 |
| Qwen3.8-27B | 正确 | 3.370414 | 130 |
| gemma-4-26B-A4B-it | 正确 | 0.19562 | 18 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I need Whopper also known old folks as the burger.</pre>

### Official accepted answer

<pre>[
  {
    "ChaFod": {
      "TheFod": [
        "BURGER"
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
    "name": "ChaFod",
    "arguments": {
      "TheFod": "BURGER"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "ChaFod",
    "arguments": {
      "TheFod": "BURGER"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "ChaFod",
    "arguments": {
      "TheFod": "BURGER"
    }
  }
]</pre>

</details>

## live_simple_23-5-1

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.213239 | 135 |
| Qwen3.8-27B | 正确 | 1.9939 | 73 |
| gemma-4-26B-A4B-it | 正确 | 0.197074 | 19 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Order me pizza</pre>

### Official accepted answer

<pre>[
  {
    "ChaFod": {
      "TheFod": [
        "PIZZA"
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
    "name": "ChaFod",
    "arguments": {
      "TheFod": "PIZZA"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "ChaFod",
    "arguments": {
      "TheFod": "PIZZA"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "ChaFod",
    "arguments": {
      "TheFod": "PIZZA"
    }
  }
]</pre>

</details>

## live_simple_24-5-2

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.846673 | 210 |
| Qwen3.8-27B | 正确 | 2.422006 | 91 |
| gemma-4-26B-A4B-it | 正确 | 0.189057 | 18 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I would like to switch my order from pizza to a BURGER.</pre>

### Official accepted answer

<pre>[
  {
    "ChaFod": {
      "TheFod": [
        "BURGER"
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
    "name": "ChaFod",
    "arguments": {
      "TheFod": "BURGER"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "ChaFod",
    "arguments": {
      "TheFod": "BURGER"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "ChaFod",
    "arguments": {
      "TheFod": "BURGER"
    }
  }
]</pre>

</details>

## live_simple_25-5-3

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.355565 | 270 |
| Qwen3.8-27B | 正确 | 3.341134 | 129 |
| gemma-4-26B-A4B-it | 正确 | 0.192118 | 18 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I've changed my mind, can I get a greens instead of what I previously ordered?</pre>

### Official accepted answer

<pre>[
  {
    "ChaFod": {
      "TheFod": [
        "SALAD"
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
    "name": "ChaFod",
    "arguments": {
      "TheFod": "SALAD"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "ChaFod",
    "arguments": {
      "TheFod": "SALAD"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "ChaFod",
    "arguments": {
      "TheFod": "SALAD"
    }
  }
]</pre>

</details>

## live_simple_26-6-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 错误 | 1.722134 | 193 |
| Qwen3.8-27B | 错误 | 5.833762 | 231 |
| gemma-4-26B-A4B-it | 错误 | 0.37228 | 41 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Tôi cần một chuyến Uber loại 'Plus' từ địa chỉ 123 Đường Đại học, Berkeley, CA 94704 và tôi không muốn chờ quá 10 phút.</pre>

### Official accepted answer

<pre>[
  {
    "uber.ride": {
      "loc": [
        "123 Đường Đại học, Berkeley, CA",
        "123 University Street, Berkeley, CA"
      ],
      "type": [
        "plus"
      ],
      "time": [
        10
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
    "name": "uber_ride",
    "arguments": {
      "loc": "123 Đường Đại học, Berkeley, CA 94704",
      "type": "plus",
      "time": 10
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'loc': '123 Đường Đại học, Berkeley, CA 94704'. Expected one of ['123 Đường Đại học, Berkeley, CA', '123 University Street, Berkeley, CA']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "uber_ride",
    "arguments": {
      "loc": "123 Đường Đại học, Berkeley, CA 94704",
      "type": "plus",
      "time": 10
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'loc': '123 Đường Đại học, Berkeley, CA 94704'. Expected one of ['123 Đường Đại học, Berkeley, CA', '123 University Street, Berkeley, CA']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 错误</summary>

### Model output

<pre>[
  {
    "name": "uber_ride",
    "arguments": {
      "loc": "123 Đường Đại học, Berkeley, CA 94704",
      "time": 10,
      "type": "plus"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'loc': '123 Đường Đại học, Berkeley, CA 94704'. Expected one of ['123 Đường Đại học, Berkeley, CA', '123 University Street, Berkeley, CA']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

## live_simple_27-7-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.947486 | 220 |
| Qwen3.8-27B | 正确 | 4.201962 | 164 |
| gemma-4-26B-A4B-it | 正确 | 0.346679 | 38 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I want to order five 'burgers' and six 'chicken wings' from uber pitada</pre>

### Official accepted answer

<pre>[
  {
    "uber.eat.order": {
      "restaurant": [
        "uber pitada"
      ],
      "items": [
        [
          "burgers",
          "chicken wings"
        ]
      ],
      "quantities": [
        [
          5,
          6
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
    "name": "uber_eat_order",
    "arguments": {
      "restaurant": "uber pitada",
      "items": [
        "burgers",
        "chicken wings"
      ],
      "quantities": [
        5,
        6
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
    "name": "uber_eat_order",
    "arguments": {
      "restaurant": "uber pitada",
      "items": [
        "burgers",
        "chicken wings"
      ],
      "quantities": [
        5,
        6
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
    "name": "uber_eat_order",
    "arguments": {
      "items": [
        "burgers",
        "chicken wings"
      ],
      "quantities": [
        5,
        6
      ],
      "restaurant": "uber pitada"
    }
  }
]</pre>

</details>

## live_simple_28-7-1

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.533123 | 171 |
| Qwen3.8-27B | 正确 | 5.484286 | 217 |
| gemma-4-26B-A4B-it | 正确 | 0.548842 | 63 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: 我想在肯德基买10个麦辣鸡腿堡，50杯可口可乐，30个油炸鸡翅，90根薯条</pre>

### Official accepted answer

<pre>[
  {
    "uber.eat.order": {
      "restaurant": [
        "肯德基",
        "KFC"
      ],
      "items": [
        [
          "麦辣鸡腿堡",
          "可口可乐",
          "油炸鸡翅",
          "薯条"
        ]
      ],
      "quantities": [
        [
          10,
          50,
          30,
          90
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
    "name": "uber_eat_order",
    "arguments": {
      "restaurant": "肯德基",
      "items": [
        "麦辣鸡腿堡",
        "可口可乐",
        "油炸鸡翅",
        "薯条"
      ],
      "quantities": [
        10,
        50,
        30,
        90
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
    "name": "uber_eat_order",
    "arguments": {
      "restaurant": "肯德基",
      "items": [
        "麦辣鸡腿堡",
        "可口可乐",
        "油炸鸡翅",
        "薯条"
      ],
      "quantities": [
        10,
        50,
        30,
        90
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
    "name": "uber_eat_order",
    "arguments": {
      "items": [
        "麦辣鸡腿堡",
        "可口可乐",
        "油炸鸡翅",
        "薯条"
      ],
      "quantities": [
        10,
        50,
        30,
        90
      ],
      "restaurant": "肯德基"
    }
  }
]</pre>

</details>

## live_simple_29-7-2

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.513455 | 169 |
| Qwen3.8-27B | 正确 | 19.527589 | 795 |
| gemma-4-26B-A4B-it | 错误 | 0.342321 | 37 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I want to go to McDonald's and buy a pizza.</pre>

### Official accepted answer

<pre>[
  {
    "uber.eat.order": {
      "restaurant": [
        "McDonald's"
      ],
      "items": [
        [
          "pizza"
        ]
      ],
      "quantities": [
        [
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
    "name": "uber_eat_order",
    "arguments": {
      "restaurant": "McDonald's",
      "items": [
        "pizza"
      ],
      "quantities": [
        1
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>文本回复：


I'll place an order for one pizza from McDonald's on Uber Eats for you.



工具调用：
[
  {
    "name": "uber_eat_order",
    "arguments": {
      "restaurant": "McDonald's",
      "items": [
        "pizza"
      ],
      "quantities": [
        1
      ]
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 错误</summary>

### Model output

<pre>未调用工具
I'm sorry, but McDonald's doesn't typically serve pizza. Would you like to try ordering from a different restaurant, or perhaps look for a pizza place instead?</pre>

### Official diagnostic

<pre>[
  "Wrong number of functions."
]</pre>

### Provisional error group

<pre>工具集合不匹配</pre>

</details>


[Category index](README.md) · [All categories](../README.md) · [Next](page-002.md)
