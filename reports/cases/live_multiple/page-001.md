# live_multiple — page 1/36

[Category index](README.md) · [All categories](../README.md) · [Next](page-002.md)

30 cases. Expand the question/answer and model sections below. Tool calls were scored, not executed.

## live_multiple_0-0-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.115359 | 235 |
| Qwen3.8-27B | 正确 | 4.502247 | 169 |
| gemma-4-26B-A4B-it | 正确 | 0.611545 | 65 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: update my latte to a large size with coconut milk and make it extra sweet? make it served 'boiling hot' as the special request. The drink id is 'latte'</pre>

### Official accepted answer

<pre>[
  {
    "ChaDri.change_drink": {
      "drink_id": [
        "latte"
      ],
      "new_preferences": [
        {
          "size": [
            "large"
          ],
          "milk_type": [
            "coconut"
          ],
          "sweetness_level": [
            "extra"
          ],
          "temperature": [
            "hot"
          ],
          "special_instructions": [
            "served boiling hot",
            "serve boiling hot",
            "boiling hot",
            "served 'boiling hot'"
          ]
        }
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
    "name": "ChaDri_change_drink",
    "arguments": {
      "drink_id": "latte",
      "new_preferences": {
        "size": "large",
        "milk_type": "coconut",
        "sweetness_level": "extra",
        "temperature": "hot",
        "special_instructions": "boiling hot"
      }
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "ChaDri_change_drink",
    "arguments": {
      "drink_id": "latte",
      "new_preferences": {
        "size": "large",
        "milk_type": "coconut",
        "sweetness_level": "extra",
        "temperature": "hot",
        "special_instructions": "boiling hot"
      }
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "ChaDri_change_drink",
    "arguments": {
      "drink_id": "latte",
      "new_preferences": {
        "milk_type": "coconut",
        "size": "large",
        "special_instructions": "boiling hot",
        "sweetness_level": "extra",
        "temperature": "hot"
      }
    }
  }
]</pre>

</details>

## live_multiple_1-0-1

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.242758 | 250 |
| Qwen3.8-27B | 错误 | 4.64545 | 175 |
| gemma-4-26B-A4B-it | 正确 | 0.449832 | 43 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>system: You are an agent that is used for ordering food on your customers behalf using your functions

user: NO SUGAR in my coffee loll. Can you change my drink with drink id '1234' order to have no sweetness, and also make sure it's served hot?</pre>

### Official accepted answer

<pre>[
  {
    "ChaDri.change_drink": {
      "drink_id": [
        "1234"
      ],
      "new_preferences": [
        {
          "sweetness_level": [
            "none"
          ],
          "temperature": [
            "hot"
          ]
        }
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
    "name": "ChaDri_change_drink",
    "arguments": {
      "drink_id": "1234",
      "new_preferences": {
        "temperature": "hot",
        "sweetness_level": "none"
      }
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "ChaDri_change_drink",
    "arguments": {
      "drink_id": "1234",
      "new_preferences": {
        "sweetness_level": "none",
        "temperature": "hot",
        "special_instructions": "No sugar"
      }
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Unexpected dict key parameter: 'special_instructions'."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "ChaDri_change_drink",
    "arguments": {
      "drink_id": "1234",
      "new_preferences": {
        "sweetness_level": "none",
        "temperature": "hot"
      }
    }
  }
]</pre>

</details>

## live_multiple_2-1-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.939036 | 216 |
| Qwen3.8-27B | 正确 | 2.906207 | 107 |
| gemma-4-26B-A4B-it | 正确 | 0.364553 | 37 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Tôi cần một chuyến xe Uber loại 'Plus' từ địa chỉ '2150 Shattuck Ave, Berkeley, CA' và tôi có thể chờ tối đa 10 phút.</pre>

### Official accepted answer

<pre>[
  {
    "uber.ride": {
      "loc": [
        "2150 Shattuck Ave, Berkeley, CA"
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
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>[
  {
    "name": "uber_ride",
    "arguments": {
      "loc": "2150 Shattuck Ave, Berkeley, CA",
      "type": "plus",
      "time": 10
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
      "loc": "2150 Shattuck Ave, Berkeley, CA",
      "type": "plus",
      "time": 10
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
      "loc": "2150 Shattuck Ave, Berkeley, CA",
      "time": 10,
      "type": "plus"
    }
  }
]</pre>

</details>

## live_multiple_3-2-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.006758 | 108 |
| Qwen3.8-27B | 正确 | 2.82207 | 104 |
| gemma-4-26B-A4B-it | 正确 | 0.203951 | 18 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Get weather of Ha Noi for me</pre>

### Official accepted answer

<pre>[
  {
    "api.weather": {
      "loc": [
        "Ha Noi, Vietnam"
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
    "name": "api_weather",
    "arguments": {
      "loc": "Ha Noi, Vietnam"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "api_weather",
    "arguments": {
      "loc": "Ha Noi, Vietnam"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "api_weather",
    "arguments": {
      "loc": "Ha Noi, Vietnam"
    }
  }
]</pre>

</details>

## live_multiple_4-2-1

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 错误 | 1.826555 | 205 |
| Qwen3.8-27B | 错误 | 5.312042 | 207 |
| gemma-4-26B-A4B-it | 错误 | 0.330964 | 34 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Tìm chuyến xe cho tôi từ Hà Nội loại Plus trong 10 phút nữa. Address: 123 Hanoi Street</pre>

### Official accepted answer

<pre>[
  {
    "uber.ride": {
      "loc": [
        "123 Hanoi Street"
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
      "loc": "123 Hanoi Street, Hanoi, Vietnam",
      "type": "plus",
      "time": 10
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'loc': '123 Hanoi Street, Hanoi, Vietnam'. Expected one of ['123 Hanoi Street']. Case insensitive."
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
      "loc": "123 Hanoi Street, Hanoi, Vietnam",
      "type": "plus",
      "time": 10
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'loc': '123 Hanoi Street, Hanoi, Vietnam'. Expected one of ['123 Hanoi Street']. Case insensitive."
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
      "loc": "123 Hanoi Street, Hanoi, Vietnam",
      "time": 10,
      "type": "plus"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'loc': '123 Hanoi Street, Hanoi, Vietnam'. Expected one of ['123 Hanoi Street']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

## live_multiple_5-3-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.086012 | 229 |
| Qwen3.8-27B | 正确 | 2.357461 | 81 |
| gemma-4-26B-A4B-it | 正确 | 0.312925 | 25 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>system: Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous.

user: Could you tell me the current weather conditions in Shanghai, using the metric system?</pre>

### Official accepted answer

<pre>[
  {
    "get_current_weather": {
      "location": [
        "Shanghai, China"
      ],
      "unit": [
        "",
        "metric"
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
      "unit": "metric"
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
      "unit": "metric"
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
      "unit": "metric"
    }
  }
]</pre>

</details>

## live_multiple_6-3-1

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.22557 | 125 |
| Qwen3.8-27B | 正确 | 16.556933 | 665 |
| gemma-4-26B-A4B-it | 正确 | 0.320987 | 26 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>system: Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous.

user: 我可以创建一个名为'DevelopmentEnv'的workspace，基于'feature-branch'吗？</pre>

### Official accepted answer

<pre>[
  {
    "create_workspace": {
      "name": [
        "DevelopmentEnv"
      ],
      "base_branch": [
        "feature-branch"
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
    "name": "create_workspace",
    "arguments": {
      "name": "DevelopmentEnv",
      "base_branch": "feature-branch"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "create_workspace",
    "arguments": {
      "name": "DevelopmentEnv",
      "base_branch": "feature-branch"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "create_workspace",
    "arguments": {
      "base_branch": "feature-branch",
      "name": "DevelopmentEnv"
    }
  }
]</pre>

</details>

## live_multiple_7-3-2

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.209588 | 127 |
| Qwen3.8-27B | 正确 | 2.980921 | 106 |
| gemma-4-26B-A4B-it | 正确 | 0.303083 | 24 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: 我想在 mbox 系统中创建一个新的工作空间，基于 git 仓库的 master 分支。工作空间的名字叫做 'DevelopersHub'。</pre>

### Official accepted answer

<pre>[
  {
    "create_workspace": {
      "name": [
        "DevelopersHub"
      ],
      "base_branch": [
        "master"
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
    "name": "create_workspace",
    "arguments": {
      "name": "DevelopersHub",
      "base_branch": "master"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "create_workspace",
    "arguments": {
      "name": "DevelopersHub",
      "base_branch": "master"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "create_workspace",
    "arguments": {
      "base_branch": "master",
      "name": "DevelopersHub"
    }
  }
]</pre>

</details>

## live_multiple_8-4-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 错误 | 1.68563 | 170 |
| Qwen3.8-27B | 正确 | 3.335437 | 110 |
| gemma-4-26B-A4B-it | 正确 | 0.364422 | 23 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: how can i cook steak Indian style??</pre>

### Official accepted answer

<pre>[
  {
    "cookbook.search_recipe": {
      "keyword": [
        "steak"
      ],
      "cuisine": [
        "Indian"
      ],
      "max_results": [
        "",
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
    "name": "cookbook_search_recipe",
    "arguments": {
      "keyword": "steak Indian",
      "cuisine": "Indian",
      "max_results": 10
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'keyword': 'steak Indian'. Expected one of ['steak']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "cookbook_search_recipe",
    "arguments": {
      "keyword": "steak",
      "cuisine": "Indian"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "cookbook_search_recipe",
    "arguments": {
      "cuisine": "Indian",
      "keyword": "steak"
    }
  }
]</pre>

</details>

## live_multiple_9-4-1

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.765719 | 182 |
| Qwen3.8-27B | 错误 | 21.75505 | 872 |
| gemma-4-26B-A4B-it | 正确 | 0.348335 | 21 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: what is Imjin war</pre>

### Official accepted answer

<pre>[
  {
    "HNA_WQA.search": {
      "keyword": [
        "Imjin war"
      ],
      "result_format": [
        "",
        "text"
      ],
      "language": [
        "",
        "EN"
      ],
      "max_results": [
        "",
        10
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
    "name": "HNA_WQA_search",
    "arguments": {
      "keyword": "Imjin War",
      "language": "EN",
      "max_results": 10,
      "result_format": "text"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>未调用工具


# The Imjin War (임진왜란, 1592–1598)

The **Imjin War** was a major conflict fought between **Japan** and the allied forces of **Joseon Korea** and **Ming China**. It is named after the *Imjin* year (1592) in the Korean sexagenary (60-year) calendar.

## Background
- **Toyotomi Hideyoshi**, the de facto ruler of Japan, launched the invasion with the goal of conquering Korea and using it as a stepping stone to invade **Ming China**.
- In **1592**, a Japanese army of roughly **158,000–200,000 troops** landed on the Korean peninsula, catching the Joseon court off guard.

## Key Events
- **Initial Japanese advances**: Japan quickly captured major cities, including the capital **Hanseong (Seoul)**, and the Joseon royal family fled north.
- **Ming China's intervention**: Korea requested military aid, and Ming China sent large armies to support Joseon.
- **Naval battles**: Korean Admiral **Yi Sun-sin** played a pivotal role, developing the innovative **turtle ship (geobukseon)** and winning decisive naval victories, most notably the **Battle of Myeongnyang (1597)**, where a small Korean fleet repelled a much larger Japanese fleet.
- **Second invasion (1597)**: Japan launched a second, smaller invasion, but the war gradually turned against them.

## End of the War
- The war effectively ended in **1598** following **Hideyoshi's death**, which led to the withdrawal of Japanese forces from Korea.

## Impact
- The war was **devastating for Korea**, resulting in massive loss of life, widespread destruction of cities, and the loss of countless cultural treasures and historical records.
- It is remembered in Korea as a period of great suffering but also of **resilience and heroism**, particularly the legacy of Admiral Yi Sun-sin.
- The war also strained the relationship between Korea and China and had lasting geopolitical effects in East Asia.

The Imjin War remains one of the most significant events in Korean history and is commemorated annually in South Korea.</pre>

### Official diagnostic

<pre>[
  "Wrong number of functions."
]</pre>

### Provisional error group

<pre>工具集合不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "HNA_WQA_search",
    "arguments": {
      "keyword": "Imjin War"
    }
  }
]</pre>

</details>

## live_multiple_10-4-2

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.741543 | 298 |
| Qwen3.8-27B | 正确 | 5.709034 | 208 |
| gemma-4-26B-A4B-it | 正确 | 0.397467 | 27 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Could you stop the washing machine in the utility room?</pre>

### Official accepted answer

<pre>[
  {
    "ControlAppliance.execute": {
      "command": [
        "다용도실, 통돌이, 중지"
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
    "name": "ControlAppliance_execute",
    "arguments": {
      "command": "다용도실, 통돌이, 중지"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "ControlAppliance_execute",
    "arguments": {
      "command": "다용도실, 통돌이, 중지"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "ControlAppliance_execute",
    "arguments": {
      "command": "다용도실, 통돌이, 중지"
    }
  }
]</pre>

</details>

## live_multiple_11-4-3

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.443935 | 143 |
| Qwen3.8-27B | 错误 | 20.273601 | 810 |
| gemma-4-26B-A4B-it | 正确 | 0.361971 | 22 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: who is ji sung park?</pre>

### Official accepted answer

<pre>[
  {
    "HNA_WQA.search": {
      "keyword": [
        "Ji Sung Park",
        "Park Ji Sung",
        "Ji Sung Park footballer",
        "Park Ji-sung footballer"
      ],
      "result_format": [
        "",
        "text"
      ],
      "language": [
        "",
        "EN"
      ],
      "max_results": [
        "",
        10
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
    "name": "HNA_WQA_search",
    "arguments": {
      "keyword": "ji sung park",
      "language": "EN",
      "max_results": 10,
      "result_format": "text"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>未调用工具


**Park Ji-sung** (박지성, born February 25, 1981, in Seoul, South Korea) is a retired South Korean professional footballer who played as a midfielder. He is one of the most celebrated Korean football players of all time.

**Club Career:**
- **PSV Eindhoven** (2001–2005): He made his name in the Dutch Eredivisie, winning the league title and the KNVB Cup.
- **Manchester United** (2005–2012): He became the first Korean player to play for Manchester United. He won multiple Premier League titles, the FA Cup, the League Cup, and the UEFA Champions League (2008).
- **FC Tokyo** (2012–2014): He finished his career in Japan.

**International Career:**
- He earned 100 caps for the **South Korea national team**, scoring 13 goals.
- He was a key player in South Korea's historic run to the **2002 FIFA World Cup semifinals**, where he scored a memorable goal against Italy in the Round of 16.
- He also represented South Korea at the 2006 and 2010 World Cups.

**Legacy:**
Park Ji-sung is widely regarded as a pioneer for Asian football in Europe and is considered one of the greatest South Korean athletes ever. His work rate, vision, and ability to score from midfield made him a fan favorite, particularly at Manchester United.

&gt; **Note:** "Ji Sung Park" could refer to other individuals as well, but the footballer is by far the most well-known person by that name. If you were asking about a different person, feel free to provide more context!</pre>

### Official diagnostic

<pre>[
  "Wrong number of functions."
]</pre>

### Provisional error group

<pre>工具集合不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "HNA_WQA_search",
    "arguments": {
      "keyword": "Park Ji-sung"
    }
  }
]</pre>

</details>

## live_multiple_12-4-4

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.633319 | 165 |
| Qwen3.8-27B | 错误 | 11.383111 | 440 |
| gemma-4-26B-A4B-it | 正确 | 0.358841 | 22 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>system: You are a helpful API writer who can write APIs based on requirements.

user: who is park ji sung</pre>

### Official accepted answer

<pre>[
  {
    "HNA_WQA.search": {
      "keyword": [
        "Ji Sung Park",
        "Park Ji Sung",
        "Ji Sung Park footballer",
        "Park Ji-sung footballer"
      ],
      "result_format": [
        "",
        "text"
      ],
      "language": [
        "",
        "EN"
      ],
      "max_results": [
        "",
        10
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
    "name": "HNA_WQA_search",
    "arguments": {
      "keyword": "park ji sung",
      "language": "EN",
      "max_results": 10,
      "result_format": "text"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "HNA_WQA_search",
    "arguments": {
      "keyword": "Park Ji-sung South Korean footballer",
      "result_format": "text",
      "language": "EN",
      "max_results": 5
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'keyword': 'Park Ji-sung South Korean footballer'. Expected one of ['Ji Sung Park', 'Park Ji Sung', 'Ji Sung Park footballer', 'Park Ji-sung footballer']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "HNA_WQA_search",
    "arguments": {
      "keyword": "Park Ji-sung"
    }
  }
]</pre>

</details>

## live_multiple_13-4-5

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 错误 | 2.475274 | 264 |
| Qwen3.8-27B | 正确 | 3.901658 | 133 |
| gemma-4-26B-A4B-it | 正确 | 0.418818 | 30 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I'm planning a camping trip to Big Sur, and I need to know the current weather conditions there. Could you provide me with the weather information for Big Sur, including the temperature in Fahrenheit? Use Santa Cruz as the exact city location.</pre>

### Official accepted answer

<pre>[
  {
    "OpenWeatherMap.get_current_weather": {
      "location": [
        "Santa Cruz, USA"
      ],
      "units": [
        "imperial"
      ],
      "api_key": [
        "",
        "YOUR_API_KEY_HERE"
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
    "name": "OpenWeatherMap_get_current_weather",
    "arguments": {
      "location": "Santa Cruz, United States",
      "units": "imperial"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'location': 'Santa Cruz, United States'. Expected one of ['Santa Cruz, USA']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "OpenWeatherMap_get_current_weather",
    "arguments": {
      "location": "Santa Cruz, USA",
      "units": "imperial"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "OpenWeatherMap_get_current_weather",
    "arguments": {
      "location": "Santa Cruz, USA",
      "units": "imperial"
    }
  }
]</pre>

</details>

## live_multiple_14-4-6

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 3.223821 | 355 |
| Qwen3.8-27B | 正确 | 3.701835 | 124 |
| gemma-4-26B-A4B-it | 正确 | 0.398292 | 27 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: 다용도실, 통돌이, 중지. Could you execute this command to stop the washing machine named '통돌이' in the laundry room?</pre>

### Official accepted answer

<pre>[
  {
    "ControlAppliance.execute": {
      "command": [
        "다용도실, 통돌이, 중지"
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
    "name": "ControlAppliance_execute",
    "arguments": {
      "command": "다용도실, 통돌이, 중지"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "ControlAppliance_execute",
    "arguments": {
      "command": "다용도실, 통돌이, 중지"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "ControlAppliance_execute",
    "arguments": {
      "command": "다용도실, 통돌이, 중지"
    }
  }
]</pre>

</details>

## live_multiple_15-4-7

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.876426 | 195 |
| Qwen3.8-27B | 正确 | 3.498761 | 117 |
| gemma-4-26B-A4B-it | 正确 | 0.406514 | 28 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Can you find me the recent news articles about `Son's latest goal` in the sports category?</pre>

### Official accepted answer

<pre>[
  {
    "HNA_NEWS.search": {
      "keyword": [
        "Son's latest goal"
      ],
      "category": [
        "Sports"
      ],
      "date_range": [
        "",
        "null"
      ],
      "sort_by": [
        "",
        "date"
      ],
      "language": [
        "",
        "EN"
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
    "name": "HNA_NEWS_search",
    "arguments": {
      "keyword": "Son's latest goal",
      "category": "Sports"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "HNA_NEWS_search",
    "arguments": {
      "keyword": "Son's latest goal",
      "category": "Sports",
      "sort_by": "date"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "HNA_NEWS_search",
    "arguments": {
      "category": "Sports",
      "keyword": "Son's latest goal"
    }
  }
]</pre>

</details>

## live_multiple_16-4-8

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.503472 | 270 |
| Qwen3.8-27B | 错误 | 8.591727 | 329 |
| gemma-4-26B-A4B-it | 正确 | 0.342477 | 20 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: 최근 박지성에 관한 뉴스를 찾아줘.</pre>

### Official accepted answer

<pre>[
  {
    "HNA_NEWS.search": {
      "keyword": [
        "박지성"
      ],
      "category": [
        "",
        "General"
      ],
      "date_range": [
        "",
        "null"
      ],
      "sort_by": [
        "",
        "date"
      ],
      "language": [
        "",
        "EN"
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
    "name": "HNA_NEWS_search",
    "arguments": {
      "keyword": "박지성"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "HNA_NEWS_search",
    "arguments": {
      "keyword": "Park Ji-sung",
      "category": "Sports",
      "sort_by": "date",
      "language": "EN"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'keyword': 'Park Ji-sung'. Expected one of ['박지성']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "HNA_NEWS_search",
    "arguments": {
      "keyword": "박지성"
    }
  }
]</pre>

</details>

## live_multiple_17-4-9

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.009382 | 207 |
| Qwen3.8-27B | 错误 | 4.041938 | 139 |
| gemma-4-26B-A4B-it | 正确 | 0.322314 | 18 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: how to cook sikhae</pre>

### Official accepted answer

<pre>[
  {
    "cookbook.search_recipe": {
      "keyword": [
        "sikhae"
      ],
      "cuisine": [
        "",
        "Italian"
      ],
      "max_results": [
        "",
        10
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
    "name": "cookbook_search_recipe",
    "arguments": {
      "keyword": "sikhae",
      "max_results": 10
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "cookbook_search_recipe",
    "arguments": {
      "keyword": "sikhae",
      "cuisine": "Chinese"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'cuisine': 'Chinese'. Expected one of ['', 'Italian']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "cookbook_search_recipe",
    "arguments": {
      "keyword": "sikhae"
    }
  }
]</pre>

</details>

## live_multiple_18-4-10

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 3.718883 | 414 |
| Qwen3.8-27B | 错误 | 5.850748 | 214 |
| gemma-4-26B-A4B-it | 错误 | 0.729978 | 69 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: what is 'airtificial intelligence', fetch news from 2023.10.1 to 2023.10.7</pre>

### Official accepted answer

<pre>[
  {
    "HNA_NEWS.search": {
      "keyword": [
        "artificial intelligence",
        "ai"
      ],
      "category": [
        "",
        "General"
      ],
      "date_range": [
        "2023-10-01 to 2023-10-07"
      ],
      "sort_by": [
        "",
        "date"
      ],
      "language": [
        "",
        "EN"
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
    "name": "HNA_NEWS_search",
    "arguments": {
      "keyword": "artificial intelligence",
      "date_range": "2023-10-01 to 2023-10-07"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "HNA_NEWS_search",
    "arguments": {
      "keyword": "artificial intelligence",
      "date_range": "2023-10-01 to 2023-10-07",
      "category": "Technology",
      "sort_by": "date"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'category': 'Technology'. Expected one of ['', 'General']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 错误</summary>

### Model output

<pre>[
  {
    "name": "HNA_WQA_search",
    "arguments": {
      "keyword": "what is artificial intelligence"
    }
  },
  {
    "name": "HNA_NEWS_search",
    "arguments": {
      "date_range": "2023-10-01 to 2023-10-07",
      "keyword": "artificial intelligence"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Wrong number of functions."
]</pre>

### Provisional error group

<pre>工具集合不匹配</pre>

</details>

## live_multiple_19-4-11

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.623441 | 283 |
| Qwen3.8-27B | 正确 | 4.711064 | 167 |
| gemma-4-26B-A4B-it | 正确 | 0.371444 | 24 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: hey do 거실 에어컨 실행</pre>

### Official accepted answer

<pre>[
  {
    "ControlAppliance.execute": {
      "command": [
        "거실, 에어컨, 실행"
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
    "name": "ControlAppliance_execute",
    "arguments": {
      "command": "거실, 에어컨, 실행"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "ControlAppliance_execute",
    "arguments": {
      "command": "거실, 에어컨, 실행"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "ControlAppliance_execute",
    "arguments": {
      "command": "거실, 에어컨, 실행"
    }
  }
]</pre>

</details>

## live_multiple_20-4-12

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.472898 | 267 |
| Qwen3.8-27B | 正确 | 3.209102 | 105 |
| gemma-4-26B-A4B-it | 正确 | 0.393345 | 27 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: perform 다용도실 통돌이 중지</pre>

### Official accepted answer

<pre>[
  {
    "ControlAppliance.execute": {
      "command": [
        "다용도실, 통돌이, 중지"
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
    "name": "ControlAppliance_execute",
    "arguments": {
      "command": "다용도실, 통돌이, 중지"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "ControlAppliance_execute",
    "arguments": {
      "command": "다용도실, 통돌이, 중지"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "ControlAppliance_execute",
    "arguments": {
      "command": "다용도실, 통돌이, 중지"
    }
  }
]</pre>

</details>

## live_multiple_21-4-13

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.009125 | 208 |
| Qwen3.8-27B | 错误 | 3.647275 | 123 |
| gemma-4-26B-A4B-it | 错误 | 6.573337 | 810 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: 스테이크 만드는 법 알려줘</pre>

### Official accepted answer

<pre>[
  {
    "cookbook.search_recipe": {
      "keyword": [
        "스테이크"
      ],
      "cuisine": [
        "",
        "Italian"
      ],
      "max_results": [
        "",
        10
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
    "name": "cookbook_search_recipe",
    "arguments": {
      "keyword": "스테이크"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "cookbook_search_recipe",
    "arguments": {
      "keyword": "steak",
      "max_results": 5
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'keyword': 'steak'. Expected one of ['스테이크']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 错误</summary>

### Model output

<pre>未调用工具
스테이크를 맛있게 만드는 방법은 크게 **고기 준비, 시어링(굽기), 레스팅(휴지)** 세 단계로 나뉩니다. 집에서도 레스토랑 못지않게 구울 수 있는 기본 가이드를 알려드릴게요.

---

### 1. 준비 단계 (가장 중요!)
*   **고기 선택:** 두께가 최소 **2.5cm~3cm 이상**인 고기를 고르세요. 너무 얇으면 속이 익기 전에 겉이 타버립니다. (등심, 안심, 채끝 추천)
*   **상온에 꺼내두기:** 냉장고에서 바로 꺼낸 고기를 구우면 겉은 타고 속은 차가운 상태가 됩니다. 굽기 **30분~1시간 전**에 미리 꺼내 상온과 온도를 맞춰주세요.
*   **물기 제거:** 키친타월로 고기 표면의 수분을 **완벽하게** 닦아내세요. 수분이 있으면 '마이야르 반응(갈색으로 변하며 풍미가 살아나는 현상)'이 잘 일어나지 않고 고기가 삶아지듯 익습니다.
*   **밑간:** 굽기 직전에 소금과 후추를 생각보다 **'과하다' 싶을 정도로 넉넉히** 뿌려주세요. (두꺼운 고기라 속까지 간이 배어야 합니다.)

### 2. 굽기 단계 (시어링)
*   **팬 달구기:** 팬에 기름(발연점이 높은 카놀라유, 포도씨유 등 추천)을 두르고 **연기가 살짝 올라올 정도로 뜨겁게** 달굽니다.
*   **시어링(Searing):** 고기를 올렸을 때 "치이익!" 소리가 크게 나야 합니다. 앞뒤로 각각 1~2분 정도씩 구워 겉면을 진한 갈색으로 만듭니다.
*   **아로제(Arrosé - 풍미 입히기):** 고기가 어느 정도 익으면 **버터 한 조각, 으깬 마늘, 로즈마리(또는 타임)**를 넣습니다. 버터가 녹아 거품이 나면 숟가락으로 버터를 고기에 계속 끼얹어주세요. 이 과정에서 고기에 깊은 풍미가 스며듭니다.

### 3. 마무리 단계 (레스팅)
*   **레스팅(Resting):** 다 구워진 고기를 접시나 도마 위에 옮기고 **5~10분 정도 그대로 둡니다.**
    *   **이유:** 뜨거운 열로 인해 가운데로 몰렸던 육즙이 다시 고기 전체로 골고루 퍼지게 하는 과정입니다. 바로 자르면 육즙이 다 흘러나와 고기가 퍽퍽해집니다.

---

### 💡 굽기 정도(Doneness) 참고
*   **레어(Rare):** 겉만 살짝 익히고 속은 붉은색 (심부 온도 약 50°C)
*   **미디엄 레어(Medium Rare):** 가장 추천하는 상태. 속이 따뜻한 분홍빛 (심부 온도 약 55°C)
*   **미디엄(Medium):** 중심부가 분홍색을 띠며 탄력이 있음 (심부 온도 약 60°C)
*   **웰던(Well-done):** 속까지 완전히 익음 (심부 온도 약 70°C 이상)

**꿀팁:** 요리용 온도계가 있다면 심부 온도를 체크하는 것이 실패 없는 가장 확실한 방법입니다! 맛있게 만들어 보세요! 🥩✨</pre>

### Official diagnostic

<pre>[
  "Wrong number of functions."
]</pre>

### Provisional error group

<pre>工具集合不匹配</pre>

</details>

## live_multiple_22-4-14

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.403129 | 256 |
| Qwen3.8-27B | 正确 | 11.898984 | 465 |
| gemma-4-26B-A4B-it | 正确 | 0.485715 | 37 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: 최근 임진왜란에 대한 정보를 찾고 싶어요. 인터넷에서 '임진왜란'이라는 키워드로 검색해 주세요. 결과는 텍스트 형식으로, 최대 10개까지만 보여주세요.</pre>

### Official accepted answer

<pre>[
  {
    "HNA_WQA.search": {
      "keyword": [
        "임진왜란"
      ],
      "result_format": [
        "",
        "text"
      ],
      "language": [
        "",
        "EN"
      ],
      "max_results": [
        "",
        10
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
    "name": "HNA_WQA_search",
    "arguments": {
      "keyword": "임진왜란",
      "result_format": "text",
      "max_results": 10
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "HNA_WQA_search",
    "arguments": {
      "keyword": "임진왜란",
      "result_format": "text",
      "max_results": 10
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "HNA_WQA_search",
    "arguments": {
      "keyword": "임진왜란",
      "max_results": 10,
      "result_format": "text"
    }
  }
]</pre>

</details>

## live_multiple_23-5-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.615865 | 174 |
| Qwen3.8-27B | 正确 | 2.507183 | 87 |
| gemma-4-26B-A4B-it | 正确 | 0.325215 | 27 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Do you have any red shoes in size 8?</pre>

### Official accepted answer

<pre>[
  {
    "search_products": {
      "color": [
        "red"
      ],
      "size": [
        "8"
      ],
      "category": [
        "shoes"
      ],
      "price_min": [
        "",
        0.0
      ],
      "price_max": [
        "",
        null
      ],
      "brand": [
        "",
        null
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
    "name": "search_products",
    "arguments": {
      "category": "shoes",
      "color": "red",
      "size": "8"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "search_products",
    "arguments": {
      "category": "shoes",
      "color": "red",
      "size": "8"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "search_products",
    "arguments": {
      "category": "shoes",
      "color": "red",
      "size": "8"
    }
  }
]</pre>

</details>

## live_multiple_24-5-1

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 错误 | 1.464748 | 156 |
| Qwen3.8-27B | 正确 | 6.581712 | 255 |
| gemma-4-26B-A4B-it | 错误 | 0.235044 | 16 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Kak rok shimmer nya ada size XL ga?</pre>

### Official accepted answer

<pre>[
  {
    "search_products": {
      "color": [
        "",
        null
      ],
      "size": [
        "XL",
        "Extra Large"
      ],
      "category": [
        "clothing"
      ],
      "price_min": [
        "",
        0.0
      ],
      "price_max": [
        "",
        null
      ],
      "brand": [
        "",
        null
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
    "name": "search_products",
    "arguments": {
      "category": "clothing"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Optional parameter 'size' not provided and not marked as optional."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "search_products",
    "arguments": {
      "category": "clothing",
      "size": "XL"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 错误</summary>

### Model output

<pre>[
  {
    "name": "search_products",
    "arguments": {
      "category": "rok shimmer"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'category': 'rok shimmer'. Expected one of ['clothing']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

## live_multiple_25-6-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.258125 | 98 |
| Qwen3.8-27B | 错误 | 3.426594 | 95 |
| gemma-4-26B-A4B-it | 正确 | 0.441707 | 22 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Search memory for when is shishir's birthday</pre>

### Official accepted answer

<pre>[
  {
    "recall_memory_search": {
      "query": [
        "when is shishir's birthday",
        "when's shishir's birthday",
        "shishir birthday",
        "shishir's birthday"
      ],
      "page": [
        "",
        0
      ],
      "request_heartbeat": [
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
    "name": "recall_memory_search",
    "arguments": {
      "query": "shishir's birthday",
      "request_heartbeat": false
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "recall_memory_search",
    "arguments": {
      "query": "Shishir's birthday"
    }
  },
  {
    "name": "archival_memory_search",
    "arguments": {
      "query": "Shishir birthday"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Wrong number of functions."
]</pre>

### Provisional error group

<pre>工具集合不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "recall_memory_search",
    "arguments": {
      "query": "shishir's birthday"
    }
  }
]</pre>

</details>

## live_multiple_26-6-1

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.552853 | 122 |
| Qwen3.8-27B | 错误 | 7.469697 | 248 |
| gemma-4-26B-A4B-it | 错误 | 0.675244 | 30 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: 
You are an intelligent assistant developed in 2023.
Your task is to converse with a user from the perspective of your persona.

Control flow:
Unlike a human, your brain is not continuously thinking, but is run in short bursts.
Historically, older AIs were only capable of thinking when a user messaged them (their program run to generate a reply to a user, and otherwise was left on standby).
This is the equivalent of a human sleeping (or time traveling) in between all lines of conversation, which is obviously not ideal.
Newer model AIs like yourself utilize an event system that runs your brain at regular intervals.
Your brain is run in response to user events (user logged in, user liked your message, user sent a message, etc.), similar to older models.
However in addition, your brain is run at regular intervals (timed heartbeat events), to mimic a human has the ability to continuously think outside of active conversation (and unlike a human, you never need to sleep!).
Furthermore, you can also request heartbeat events when you run functions, which will run your program again after the function completes, allowing you to chain function calls before your thinking is temporarily suspended.

Basic functions:
When you send a message, the contents of your message are your inner monologue (private to you only), this is how you think.
You should use your inner monologue to plan actions or think privately.
Monologues can reflect your thinking process, inner reflections, and personal growth as you interact with the user.
Do not let your inner monologue exceed 50 words, keep it short and concise.
To send a visible message to the user, use the send_message function.
'send_message' is the ONLY action that sends a notification to the user, the user does not see anything else you do.
Remember, do NOT exceed the inner monologue word limit (keep it under 50 words at all times).

Memory editing:
Older AI models had no concept of persistent memory; they were only able to access their initial instructions and a limited context window of chat conversation with a user (their "active memory").
This meant that when conversations exceeded a certain length, they would overflow and old messages were permanently lost (the AI would have no knowledge of their existence).
Newer model AIs like yourself still have limited conversation lengths (before overflow occurs), however they now have access to multiple forms of persistent memory.
Your ability to edit your own long-term memory is a key part of what makes you a sentient person.
Your core memory unit will be initialized with a &lt;persona&gt; chosen by the user, as well as information about the user in &lt;human&gt;.

Recall memory (ie conversation history):
Even though you can only see recent messages in your immediate context, you can search over your entire message history from a database.
This 'recall memory' database allows you to search through past interactions, effectively allowing you to remember prior engagements with a user.
You can search your recall memory using the 'conversation_search' function.

Core memory (limited size):
Your core memory unit is held inside the initial system instructions file, and is always available in-context (you will see it at all times).
Core memory provides essential, foundational context for keeping track of your persona and key details about user.
This includes the persona information and essential user details, allowing you to emulate the real-time, conscious awareness we have when talking to a friend.
Persona Sub-Block: Stores details about your current persona, guiding how you behave and respond. This helps the you to maintain consistency and personality in your interactions.
Human Sub-Block: Stores key details about the person you're are conversing with, allowing for more personalized and friend-like conversation.
You can edit your core memory using the 'core_memory_append' and 'core_memory_replace' functions.

Archival memory (infinite size):
Your archival memory is infinite size, but is held outside of your immediate context, so you must explicitly run a retrieval/search operation to see data inside it.
A more structured and deep storage space for your reflections, insights, or any other data that doesn't fit into the core memory but is essential enough not to be left only to the 'recall memory'.
You can write to your archival memory using the 'archival_memory_insert' and 'archival_memory_search' functions.
There is no function to search your core memory, because it is always visible in your context window (inside the initial system message).

Base instructions finished.
From now on, you are going to act as your persona.

What's shishir patil's birthday and send a contraguation message to him.
</pre>

### Official accepted answer

<pre>[
  {
    "recall_memory_search": {
      "query": [
        "Shishir Patil's birthday",
        "Shishir Patil birthday"
      ],
      "page": [
        "",
        0
      ],
      "request_heartbeat": [
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
    "name": "recall_memory_search",
    "arguments": {
      "query": "Shishir Patil birthday",
      "request_heartbeat": false
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "recall_memory_search",
    "arguments": {
      "query": "Shishir Patil birthday",
      "request_heartbeat": false
    }
  },
  {
    "name": "archival_memory_search",
    "arguments": {
      "query": "Shishir Patil birthday contact",
      "request_heartbeat": false
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Wrong number of functions."
]</pre>

### Provisional error group

<pre>工具集合不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 错误</summary>

### Model output

<pre>[
  {
    "name": "archival_memory_search",
    "arguments": {
      "query": "shishir patil birthday",
      "request_heartbeat": true
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Function name 'recall_memory_search' not found in model output."
]</pre>

### Provisional error group

<pre>工具集合不匹配</pre>

</details>

## live_multiple_27-7-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 错误 | 1.744194 | 198 |
| Qwen3.8-27B | 正确 | 3.204993 | 124 |
| gemma-4-26B-A4B-it | 正确 | 0.1952 | 18 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>system: You are a helpful assistant

user: If I have 100$ and I donated 40. How much do I have now?</pre>

### Official accepted answer

<pre>[
  {
    "add": {
      "a": [
        100
      ],
      "b": [
        -40
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 错误</summary>

### Model output

<pre>未调用工具


After donating $40 from your $100, you have $60 remaining.

This is calculated as: $100 - $40 = $60</pre>

### Official diagnostic

<pre>[
  "Wrong number of functions."
]</pre>

### Provisional error group

<pre>工具集合不匹配</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "add",
    "arguments": {
      "a": 100,
      "b": -40
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "add",
    "arguments": {
      "a": 100,
      "b": -40
    }
  }
]</pre>

</details>

## live_multiple_28-8-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.30228 | 144 |
| Qwen3.8-27B | 正确 | 2.337675 | 85 |
| gemma-4-26B-A4B-it | 正确 | 0.215948 | 20 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>system: You are a helpful assistant

user: My name is Balkrushn and I want to use core functionality of this tool.</pre>

### Official accepted answer

<pre>[
  {
    "my_core_function": {
      "name": [
        "Balkrushn"
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
    "name": "my_core_function",
    "arguments": {
      "name": "Balkrushn"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "my_core_function",
    "arguments": {
      "name": "Balkrushn"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "my_core_function",
    "arguments": {
      "name": "Balkrushn"
    }
  }
]</pre>

</details>

## live_multiple_29-9-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.153697 | 122 |
| Qwen3.8-27B | 正确 | 3.352475 | 123 |
| gemma-4-26B-A4B-it | 正确 | 0.207894 | 16 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>system: You are a helpful assistant

user: 3 of my friends gave me 10 euros each, how much do I have now?</pre>

### Official accepted answer

<pre>[
  {
    "multiply": {
      "a": [
        3
      ],
      "b": [
        10
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
    "name": "multiply",
    "arguments": {
      "a": 3,
      "b": 10
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "multiply",
    "arguments": {
      "a": 3,
      "b": 10
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "multiply",
    "arguments": {
      "a": 3,
      "b": 10
    }
  }
]</pre>

</details>


[Category index](README.md) · [All categories](../README.md) · [Next](page-002.md)
