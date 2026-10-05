# live_parallel — page 1/1

[Category index](README.md) · [All categories](../README.md)

16 cases. Expand the question/answer and model sections below. Tool calls were scored, not executed.

## live_parallel_0-0-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.2679 | 143 |
| Qwen3.8-27B | 错误 | 6.398292 | 255 |
| gemma-4-26B-A4B-it | 正确 | 0.336281 | 37 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: 请问北京的当前天气状况如何？还有，上海的天气情况是怎样的？</pre>

### Official accepted answer

<pre>[
  {
    "get_current_weather": {
      "location": [
        "Beijing, China"
      ],
      "unit": [
        "",
        "fahrenheit"
      ]
    }
  },
  {
    "get_current_weather": {
      "location": [
        "Shanghai, China"
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
      "location": "Beijing, China"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Shanghai, China"
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
      "location": "Beijing, China",
      "unit": "celsius"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Shanghai, China",
      "unit": "celsius"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Could not find a matching function among index [0, 1] of model output for index 0 of possible answers.",
  {
    "Model Result Index 0": {
      "sub_error": [
        "Invalid value for parameter 'unit': 'celsius'. Expected one of ['', 'fahrenheit']. Case insensitive."
      ],
      "sub_error_type": "value_error:string",
      "model_output_item": {
        "get_current_weather": {
          "location": "Beijing, China",
          "unit": "celsius"
        }
      },
      "possible_answer_item": {
        "get_current_weather": {
          "location": [
            "Beijing, China"
          ],
          "unit": [
            "",
            "fahrenheit"
          ]
        }
      }
    }
  },
  {
    "Model Result Index 1": {
      "sub_error": [
        "Invalid value for parameter 'location': 'Shanghai, China'. Expected one of ['Beijing, China']. Case insensitive."
      ],
      "sub_error_type": "value_error:string",
      "model_output_item": {
        "get_current_weather": {
          "location": "Shanghai, China",
          "unit": "celsius"
        }
      },
      "possible_answer_item": {
        "get_current_weather": {
          "location": [
            "Beijing, China"
          ],
          "unit": [
            "",
            "fahrenheit"
          ]
        }
      }
    }
  }
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Beijing, China"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Shanghai, China"
    }
  }
]</pre>

</details>

## live_parallel_1-0-1

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.842441 | 211 |
| Qwen3.8-27B | 正确 | 3.298127 | 127 |
| gemma-4-26B-A4B-it | 正确 | 0.344744 | 38 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Could you tell me the current weather conditions for Boston, MA and also for San Francisco?</pre>

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
  },
  {
    "get_current_weather": {
      "location": [
        "San Francisco, CA"
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
      "location": "Boston, MA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>文本回复：


I'll get the current weather for both cities for you.



工具调用：
[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Boston, MA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA"
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
      "location": "Boston, MA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA"
    }
  }
]</pre>

</details>

## live_parallel_2-0-2

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.877782 | 212 |
| Qwen3.8-27B | 正确 | 2.674989 | 101 |
| gemma-4-26B-A4B-it | 正确 | 0.343809 | 38 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: &lt;&lt;question&gt;&gt; What\'s the weather like in the two cities of Boston and San Francisco?</pre>

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
  },
  {
    "get_current_weather": {
      "location": [
        "San Francisco, CA"
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
      "location": "Boston, MA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA"
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
      "location": "Boston, MA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA"
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
      "location": "Boston, MA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA"
    }
  }
]</pre>

</details>

## live_parallel_3-0-3

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 3.008868 | 349 |
| Qwen3.8-27B | 错误 | 7.865589 | 314 |
| gemma-4-26B-A4B-it | 正确 | 0.51813 | 60 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>system: Eres un asistente IA. Has sido capacitado con una superinteligencia, formidable para comunicar con usuarios en español, interpretar sus necesidades y actuar a travez de ellos.

user: ¿Podrías decirme las condiciones actuales del clima en Cancún, QR, Playa del Carmen, QR y Tulum, QR?</pre>

### Official accepted answer

<pre>[
  {
    "get_current_weather": {
      "location": [
        "Cancún, QR",
        "Canc\\u00fan, QR"
      ],
      "unit": [
        "",
        "fahrenheit"
      ]
    }
  },
  {
    "get_current_weather": {
      "location": [
        "Playa del Carmen, QR"
      ],
      "unit": [
        "",
        "fahrenheit"
      ]
    }
  },
  {
    "get_current_weather": {
      "location": [
        "Tulum, QR"
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
      "location": "Cancún, QR"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Playa del Carmen, QR"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Tulum, QR"
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
      "location": "Cancún, QR",
      "unit": "celsius"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Playa del Carmen, QR",
      "unit": "celsius"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Tulum, QR",
      "unit": "celsius"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Could not find a matching function among index [0, 1, 2] of model output for index 0 of possible answers.",
  {
    "Model Result Index 0": {
      "sub_error": [
        "Invalid value for parameter 'unit': 'celsius'. Expected one of ['', 'fahrenheit']. Case insensitive."
      ],
      "sub_error_type": "value_error:string",
      "model_output_item": {
        "get_current_weather": {
          "location": "Cancún, QR",
          "unit": "celsius"
        }
      },
      "possible_answer_item": {
        "get_current_weather": {
          "location": [
            "Cancún, QR",
            "Canc\\u00fan, QR"
          ],
          "unit": [
            "",
            "fahrenheit"
          ]
        }
      }
    }
  },
  {
    "Model Result Index 1": {
      "sub_error": [
        "Invalid value for parameter 'location': 'Playa del Carmen, QR'. Expected one of ['Cancún, QR', 'Canc\\\\u00fan, QR']. Case insensitive."
      ],
      "sub_error_type": "value_error:string",
      "model_output_item": {
        "get_current_weather": {
          "location": "Playa del Carmen, QR",
          "unit": "celsius"
        }
      },
      "possible_answer_item": {
        "get_current_weather": {
          "location": [
            "Cancún, QR",
            "Canc\\u00fan, QR"
          ],
          "unit": [
            "",
            "fahrenheit"
          ]
        }
      }
    }
  },
  {
    "Model Result Index 2": {
      "sub_error": [
        "Invalid value for parameter 'location': 'Tulum, QR'. Expected one of ['Cancún, QR', 'Canc\\\\u00fan, QR']. Case insensitive."
      ],
      "sub_error_type": "value_error:string",
      "model_output_item": {
        "get_current_weather": {
          "location": "Tulum, QR",
          "unit": "celsius"
        }
      },
      "possible_answer_item": {
        "get_current_weather": {
          "location": [
            "Cancún, QR",
            "Canc\\u00fan, QR"
          ],
          "unit": [
            "",
            "fahrenheit"
          ]
        }
      }
    }
  }
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Cancún, QR"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Playa del Carmen, QR"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "Tulum, QR"
    }
  }
]</pre>

</details>

## live_parallel_4-1-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.043183 | 234 |
| Qwen3.8-27B | 正确 | 2.537342 | 95 |
| gemma-4-26B-A4B-it | 正确 | 0.345889 | 38 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Could you tell me the current weather in Boston, USA and also in San Francisco, USA?</pre>

### Official accepted answer

<pre>[
  {
    "get_current_weather": {
      "location": [
        "Boston, USA"
      ],
      "url": [
        "",
        "https://api.open-meteo.com/v1/forecast"
      ]
    }
  },
  {
    "get_current_weather": {
      "location": [
        "San Francisco, USA"
      ],
      "url": [
        "",
        "https://api.open-meteo.com/v1/forecast"
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
      "location": "Boston, USA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, USA"
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
      "location": "Boston, USA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, USA"
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
      "location": "Boston, USA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, USA"
    }
  }
]</pre>

</details>

## live_parallel_5-2-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.096379 | 240 |
| Qwen3.8-27B | 正确 | 3.538562 | 136 |
| gemma-4-26B-A4B-it | 正确 | 0.345221 | 38 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Could you tell me the current temperature in Boston, MA and San Francisco, please?</pre>

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
      ],
      "url": [
        "",
        "https://api.open-meteo.com/v1/forecast"
      ]
    }
  },
  {
    "get_current_weather": {
      "location": [
        "San Francisco, CA"
      ],
      "unit": [
        "",
        "fahrenheit"
      ],
      "url": [
        "",
        "https://api.open-meteo.com/v1/forecast"
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
      "location": "Boston, MA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA"
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
      "location": "Boston, MA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA"
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
      "location": "Boston, MA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA"
    }
  }
]</pre>

</details>

## live_parallel_6-3-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.576076 | 176 |
| Qwen3.8-27B | 正确 | 3.529842 | 132 |
| gemma-4-26B-A4B-it | 正确 | 0.358498 | 38 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What's the snow like in the two cities of Paris and Bordeaux?</pre>

### Official accepted answer

<pre>[
  {
    "get_snow_report": {
      "location": [
        "Paris, France"
      ],
      "unit": [
        "",
        "fahrenheit"
      ]
    }
  },
  {
    "get_snow_report": {
      "location": [
        "Bordeaux, France"
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
    "name": "get_snow_report",
    "arguments": {
      "location": "Paris, France"
    }
  },
  {
    "name": "get_snow_report",
    "arguments": {
      "location": "Bordeaux, France"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_snow_report",
    "arguments": {
      "location": "Paris, France"
    }
  },
  {
    "name": "get_snow_report",
    "arguments": {
      "location": "Bordeaux, France"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_snow_report",
    "arguments": {
      "location": "Paris, France"
    }
  },
  {
    "name": "get_snow_report",
    "arguments": {
      "location": "Bordeaux, France"
    }
  }
]</pre>

</details>

## live_parallel_7-3-1

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.641918 | 184 |
| Qwen3.8-27B | 正确 | 2.810524 | 104 |
| gemma-4-26B-A4B-it | 正确 | 0.35518 | 38 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What's the weather like in the two cities of Boston and San Francisco?</pre>

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
  },
  {
    "get_current_weather": {
      "location": [
        "San Francisco, CA"
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
      "location": "Boston, MA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA"
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
      "location": "Boston, MA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA"
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
      "location": "Boston, MA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA"
    }
  }
]</pre>

</details>

## live_parallel_8-4-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.033113 | 234 |
| Qwen3.8-27B | 正确 | 4.030667 | 156 |
| gemma-4-26B-A4B-it | 正确 | 0.369037 | 41 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Hi there! Could you please help me manage my tasks? I need to add a task called 'Machine Learning Study Session'. Also, I have completed one of my tasks named 'todo random', and I would like to delete it from my list.</pre>

### Official accepted answer

<pre>[
  {
    "todo": {
      "type": [
        "add"
      ],
      "content": [
        "Machine Learning Study Session"
      ]
    }
  },
  {
    "todo": {
      "type": [
        "delete"
      ],
      "content": [
        "todo random"
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
    "name": "todo",
    "arguments": {
      "type": "add",
      "content": "Machine Learning Study Session"
    }
  },
  {
    "name": "todo",
    "arguments": {
      "type": "delete",
      "content": "todo random"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>文本回复：


I'll help you with both tasks! Let me add the new task and delete the completed one.



工具调用：
[
  {
    "name": "todo",
    "arguments": {
      "type": "add",
      "content": "Machine Learning Study Session"
    }
  },
  {
    "name": "todo",
    "arguments": {
      "type": "delete",
      "content": "todo random"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "todo",
    "arguments": {
      "content": "Machine Learning Study Session",
      "type": "add"
    }
  },
  {
    "name": "todo",
    "arguments": {
      "content": "todo random",
      "type": "delete"
    }
  }
]</pre>

</details>

## live_parallel_9-5-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.2687 | 260 |
| Qwen3.8-27B | 正确 | 4.775789 | 186 |
| gemma-4-26B-A4B-it | 正确 | 0.375299 | 41 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What's cost of 2 and 4 gb ram machine on aws ec2 with one CPU?</pre>

### Official accepted answer

<pre>[
  {
    "get_aws_pricing": {
      "memory": [
        2
      ],
      "cpu": [
        "single"
      ],
      "region": [
        "",
        "us-east-1"
      ],
      "operating_system": [
        "",
        "Linux"
      ]
    }
  },
  {
    "get_aws_pricing": {
      "memory": [
        4
      ],
      "cpu": [
        "single"
      ],
      "region": [
        "",
        "us-east-1"
      ],
      "operating_system": [
        "",
        "Linux"
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
    "name": "get_aws_pricing",
    "arguments": {
      "memory": 2,
      "cpu": "single"
    }
  },
  {
    "name": "get_aws_pricing",
    "arguments": {
      "memory": 4,
      "cpu": "single"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_aws_pricing",
    "arguments": {
      "memory": 2,
      "cpu": "single"
    }
  },
  {
    "name": "get_aws_pricing",
    "arguments": {
      "memory": 4,
      "cpu": "single"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_aws_pricing",
    "arguments": {
      "cpu": "single",
      "memory": 2
    }
  },
  {
    "name": "get_aws_pricing",
    "arguments": {
      "cpu": "single",
      "memory": 4
    }
  }
]</pre>

</details>

## live_parallel_10-6-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 4.218625 | 491 |
| Qwen3.8-27B | 正确 | 9.973455 | 397 |
| gemma-4-26B-A4B-it | 正确 | 1.184895 | 144 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I need to make a couple of hotel reservations. First, secure a room for 2 adults and 1 child at the Sheraton Hotel in New York with check-in on May 1, 2022, and check-out on May 5, 2022. Then, reserve a room for 1 adult and 2 children at the Marriott in Los Angeles, checking in on June 1, 2022, and checking out on June 10, 2022.</pre>

### Official accepted answer

<pre>[
  {
    "hotel_booking_book": {
      "hotel_name": [
        "Sheraton Hotel",
        "Sheraton",
        "Hotel Sheraton"
      ],
      "location": [
        "New York, NY"
      ],
      "check_in": [
        "2022-05-01"
      ],
      "check_out": [
        "2022-05-05"
      ],
      "adults": [
        2
      ],
      "children": [
        1
      ]
    }
  },
  {
    "hotel_booking_book": {
      "hotel_name": [
        "Marriott"
      ],
      "location": [
        "Los Angeles, CA"
      ],
      "check_in": [
        "2022-06-01"
      ],
      "check_out": [
        "2022-06-10"
      ],
      "adults": [
        1
      ],
      "children": [
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
    "name": "hotel_booking_book",
    "arguments": {
      "hotel_name": "Sheraton Hotel",
      "location": "New York, NY",
      "check_in": "2022-05-01",
      "check_out": "2022-05-05",
      "adults": 2,
      "children": 1
    }
  },
  {
    "name": "hotel_booking_book",
    "arguments": {
      "hotel_name": "Marriott",
      "location": "Los Angeles, CA",
      "check_in": "2022-06-01",
      "check_out": "2022-06-10",
      "adults": 1,
      "children": 2
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
      "hotel_name": "Sheraton Hotel",
      "location": "New York, NY",
      "check_in": "2022-05-01",
      "check_out": "2022-05-05",
      "adults": 2,
      "children": 1
    }
  },
  {
    "name": "hotel_booking_book",
    "arguments": {
      "hotel_name": "Marriott",
      "location": "Los Angeles, CA",
      "check_in": "2022-06-01",
      "check_out": "2022-06-10",
      "adults": 1,
      "children": 2
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
      "check_in": "2022-05-01",
      "check_out": "2022-05-05",
      "children": 1,
      "hotel_name": "Sheraton Hotel",
      "location": "New York, NY"
    }
  },
  {
    "name": "hotel_booking_book",
    "arguments": {
      "adults": 1,
      "check_in": "2022-06-01",
      "check_out": "2022-06-10",
      "children": 2,
      "hotel_name": "Marriott",
      "location": "Los Angeles, CA"
    }
  }
]</pre>

</details>

## live_parallel_11-7-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 5.880684 | 688 |
| Qwen3.8-27B | 错误 | 40.834116 | 1663 |
| gemma-4-26B-A4B-it | 正确 | 1.026335 | 125 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I had 8 pieces of frozen mango and a chai tea.

Earlier I had two slices of pepperoni pizza and a coffee</pre>

### Official accepted answer

<pre>[
  {
    "log_food": {
      "food_name": [
        "frozen mango"
      ],
      "portion_amount": [
        8.0
      ],
      "portion_unit": [
        "piece"
      ],
      "meal_type": [
        "",
        "snack"
      ]
    }
  },
  {
    "log_food": {
      "food_name": [
        "chai tea"
      ],
      "portion_amount": [
        1.0
      ],
      "portion_unit": [
        "cup"
      ],
      "meal_type": [
        "",
        "snack"
      ]
    }
  },
  {
    "log_food": {
      "food_name": [
        "pepperoni pizza"
      ],
      "portion_amount": [
        2.0
      ],
      "portion_unit": [
        "slice"
      ],
      "meal_type": [
        "",
        "snack"
      ]
    }
  },
  {
    "log_food": {
      "food_name": [
        "coffee"
      ],
      "portion_amount": [
        1.0
      ],
      "portion_unit": [
        "cup"
      ],
      "meal_type": [
        "",
        "snack"
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
    "name": "log_food",
    "arguments": {
      "food_name": "frozen mango",
      "portion_amount": 8,
      "portion_unit": "piece",
      "meal_type": "snack"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "chai tea",
      "portion_amount": 1,
      "portion_unit": "cup",
      "meal_type": "snack"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "pepperoni pizza",
      "portion_amount": 2,
      "portion_unit": "slice",
      "meal_type": "snack"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "coffee",
      "portion_amount": 1,
      "portion_unit": "cup",
      "meal_type": "snack"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>文本回复：


I'll log all four items for you. Since you didn't specify exact meal types, I'm making reasonable assumptions — let me know if any need adjusting!



工具调用：
[
  {
    "name": "log_food",
    "arguments": {
      "food_name": "frozen mango",
      "portion_amount": 8,
      "portion_unit": "piece",
      "meal_type": "snack"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "chai tea",
      "portion_amount": 1,
      "portion_unit": "cup",
      "meal_type": "snack"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "pepperoni pizza",
      "portion_amount": 2,
      "portion_unit": "slice",
      "meal_type": "lunch"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "coffee",
      "portion_amount": 1,
      "portion_unit": "cup",
      "meal_type": "breakfast"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Could not find a matching function among index [2, 3] of model output for index 2 of possible answers.",
  {
    "Model Result Index 2": {
      "sub_error": [
        "Invalid value for parameter 'meal_type': 'lunch'. Expected one of ['', 'snack']. Case insensitive."
      ],
      "sub_error_type": "value_error:string",
      "model_output_item": {
        "log_food": {
          "food_name": "pepperoni pizza",
          "portion_amount": 2,
          "portion_unit": "slice",
          "meal_type": "lunch"
        }
      },
      "possible_answer_item": {
        "log_food": {
          "food_name": [
            "pepperoni pizza"
          ],
          "portion_amount": [
            2.0
          ],
          "portion_unit": [
            "slice"
          ],
          "meal_type": [
            "",
            "snack"
          ]
        }
      }
    }
  },
  {
    "Model Result Index 3": {
      "sub_error": [
        "Invalid value for parameter 'food_name': 'coffee'. Expected one of ['pepperoni pizza']. Case insensitive."
      ],
      "sub_error_type": "value_error:string",
      "model_output_item": {
        "log_food": {
          "food_name": "coffee",
          "portion_amount": 1,
          "portion_unit": "cup",
          "meal_type": "breakfast"
        }
      },
      "possible_answer_item": {
        "log_food": {
          "food_name": [
            "pepperoni pizza"
          ],
          "portion_amount": [
            2.0
          ],
          "portion_unit": [
            "slice"
          ],
          "meal_type": [
            "",
            "snack"
          ]
        }
      }
    }
  }
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "log_food",
    "arguments": {
      "food_name": "frozen mango",
      "portion_amount": 8,
      "portion_unit": "piece"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "chai tea",
      "portion_amount": 1,
      "portion_unit": "cup"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "pepperoni pizza",
      "portion_amount": 2,
      "portion_unit": "slice"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "coffee",
      "portion_amount": 1,
      "portion_unit": "cup"
    }
  }
]</pre>

</details>

## live_parallel_12-8-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 5.819511 | 682 |
| Qwen3.8-27B | 正确 | 19.431944 | 784 |
| gemma-4-26B-A4B-it | 正确 | 1.866476 | 234 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: For breakfast I had a 12 ounce iced coffee and a banana.

For lunch I had a quesadilla

Breakfast four ounces of asparagus, two eggs, one piece of gluten free bread.</pre>

### Official accepted answer

<pre>[
  {
    "log_food": {
      "food_name": [
        "iced coffee"
      ],
      "portion_amount": [
        12.0
      ],
      "portion_unit": [
        "ounces"
      ],
      "meal_name": [
        "breakfast"
      ]
    }
  },
  {
    "log_food": {
      "food_name": [
        "banana"
      ],
      "portion_amount": [
        1.0
      ],
      "portion_unit": [
        "pieces"
      ],
      "meal_name": [
        "breakfast"
      ]
    }
  },
  {
    "log_food": {
      "food_name": [
        "quesadilla"
      ],
      "portion_amount": [
        1.0
      ],
      "portion_unit": [
        "pieces"
      ],
      "meal_name": [
        "lunch"
      ]
    }
  },
  {
    "log_food": {
      "food_name": [
        "asparagus"
      ],
      "portion_amount": [
        4.0
      ],
      "portion_unit": [
        "ounces"
      ],
      "meal_name": [
        "breakfast"
      ]
    }
  },
  {
    "log_food": {
      "food_name": [
        "eggs"
      ],
      "portion_amount": [
        2.0
      ],
      "portion_unit": [
        "pieces"
      ],
      "meal_name": [
        "breakfast"
      ]
    }
  },
  {
    "log_food": {
      "food_name": [
        "gluten free bread"
      ],
      "portion_amount": [
        1.0
      ],
      "portion_unit": [
        "pieces"
      ],
      "meal_name": [
        "breakfast"
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
    "name": "log_food",
    "arguments": {
      "food_name": "iced coffee",
      "portion_amount": 12,
      "portion_unit": "ounces",
      "meal_name": "breakfast"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "banana",
      "portion_amount": 1,
      "portion_unit": "pieces",
      "meal_name": "breakfast"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "asparagus",
      "portion_amount": 4,
      "portion_unit": "ounces",
      "meal_name": "breakfast"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "eggs",
      "portion_amount": 2,
      "portion_unit": "pieces",
      "meal_name": "breakfast"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "gluten free bread",
      "portion_amount": 1,
      "portion_unit": "pieces",
      "meal_name": "breakfast"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "quesadilla",
      "portion_amount": 1,
      "portion_unit": "pieces",
      "meal_name": "lunch"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>文本回复：


I'll log all of those meals for you now.



工具调用：
[
  {
    "name": "log_food",
    "arguments": {
      "food_name": "iced coffee",
      "portion_amount": 12,
      "portion_unit": "ounces",
      "meal_name": "breakfast"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "banana",
      "portion_amount": 1,
      "portion_unit": "pieces",
      "meal_name": "breakfast"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "quesadilla",
      "portion_amount": 1,
      "portion_unit": "pieces",
      "meal_name": "lunch"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "asparagus",
      "portion_amount": 4,
      "portion_unit": "ounces",
      "meal_name": "breakfast"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "eggs",
      "portion_amount": 2,
      "portion_unit": "pieces",
      "meal_name": "breakfast"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "gluten free bread",
      "portion_amount": 1,
      "portion_unit": "pieces",
      "meal_name": "breakfast"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "log_food",
    "arguments": {
      "food_name": "iced coffee",
      "meal_name": "breakfast",
      "portion_amount": 12,
      "portion_unit": "ounces"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "banana",
      "meal_name": "breakfast",
      "portion_amount": 1,
      "portion_unit": "pieces"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "quesadilla",
      "meal_name": "lunch",
      "portion_amount": 1,
      "portion_unit": "pieces"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "asparagus",
      "meal_name": "breakfast",
      "portion_amount": 4,
      "portion_unit": "ounces"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "eggs",
      "meal_name": "breakfast",
      "portion_amount": 2,
      "portion_unit": "pieces"
    }
  },
  {
    "name": "log_food",
    "arguments": {
      "food_name": "gluten free bread",
      "meal_name": "breakfast",
      "portion_amount": 1,
      "portion_unit": "pieces"
    }
  }
]</pre>

</details>

## live_parallel_13-9-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.767645 | 203 |
| Qwen3.8-27B | 正确 | 4.799631 | 187 |
| gemma-4-26B-A4B-it | 正确 | 0.34542 | 38 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Could you tell me the current weather in Boston, MA and also in San Francisco?</pre>

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
  },
  {
    "get_current_weather": {
      "location": [
        "San Francisco, CA"
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
      "location": "Boston, MA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA"
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
      "location": "Boston, MA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA"
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
      "location": "Boston, MA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA"
    }
  }
]</pre>

</details>

## live_parallel_14-10-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.556899 | 177 |
| Qwen3.8-27B | 正确 | 2.739643 | 104 |
| gemma-4-26B-A4B-it | 正确 | 0.343915 | 38 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What's the weather like in the two cities of Boston and San Francisco?</pre>

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
  },
  {
    "get_current_weather": {
      "location": [
        "San Francisco, CA"
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
      "location": "Boston, MA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA"
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
      "location": "Boston, MA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA"
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
      "location": "Boston, MA"
    }
  },
  {
    "name": "get_current_weather",
    "arguments": {
      "location": "San Francisco, CA"
    }
  }
]</pre>

</details>

## live_parallel_15-11-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.612016 | 184 |
| Qwen3.8-27B | 错误 | 6.862231 | 272 |
| gemma-4-26B-A4B-it | 错误 | 0.197801 | 19 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: list file in c drive and make file called testing.txt</pre>

### Official accepted answer

<pre>[
  {
    "cmd_controller.execute": {
      "command": [
        "dir c:\\",
        "dir c:\\\\"
      ]
    }
  },
  {
    "cmd_controller.execute": {
      "command": [
        "echo.&gt;C:\\testing.txt",
        "echo.&gt;C:\\\\testing.txt"
      ],
      "unit": [
        "",
        "N/A"
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>文本回复：


I'll help you list files in the C drive and create a file called testing.txt. Let me execute these commands for you.



工具调用：
[
  {
    "name": "cmd_controller_execute",
    "arguments": {
      "command": "dir C:\\"
    }
  },
  {
    "name": "cmd_controller_execute",
    "arguments": {
      "command": "echo. &gt; C:\\testing.txt"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "cmd_controller_execute",
    "arguments": {
      "command": "echo. &gt; C:\\testing.txt",
      "unit": "seconds"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Wrong number of functions."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 错误</summary>

### Model output

<pre>[
  {
    "name": "cmd_controller_execute",
    "arguments": {
      "command": "dir C:\\"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Wrong number of functions."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>


[Category index](README.md) · [All categories](../README.md)
