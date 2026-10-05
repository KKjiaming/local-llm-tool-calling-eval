# live_multiple — page 9/36

[Category index](README.md) · [All categories](../README.md) · [Previous](page-008.md) · [Next](page-010.md)

30 cases. Expand the question/answer and model sections below. Tool calls were scored, not executed.

## live_multiple_240-107-1

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.829816 | 188 |
| Qwen3.8-27B | 错误 | 2.608314 | 82 |
| gemma-4-26B-A4B-it | 正确 | 0.322984 | 20 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: weather in India using searcvh web tool </pre>

### Official accepted answer

<pre>[
  {
    "search_web_tool": {
      "query": [
        "weather in India",
        "current weather in India",
        "What's the current weather in India",
        "What's the current weather in India?"
      ],
      "num_results": [
        "",
        3
      ],
      "source": [
        "",
        "text"
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
    "name": "search_web_tool",
    "arguments": {
      "query": "weather in India"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "search_web_tool",
    "arguments": {
      "query": "current weather in India today",
      "num_results": 5,
      "source": "news"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'query': 'current weather in India today'. Expected one of ['weather in India', 'current weather in India', \"What's the current weather in India\", \"What's the current weather in India?\"]. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "search_web_tool",
    "arguments": {
      "query": "current weather in India"
    }
  }
]</pre>

</details>

## live_multiple_241-107-2

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 错误 | 1.866462 | 194 |
| Qwen3.8-27B | 错误 | 3.372397 | 113 |
| gemma-4-26B-A4B-it | 正确 | 0.347495 | 23 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: search flight prices from NYC to NEw Delhi use tools, finally respond in json</pre>

### Official accepted answer

<pre>[
  {
    "search_web_tool": {
      "query": [
        "flight prices from NYC to New Delhi"
      ],
      "num_results": [
        "",
        3
      ],
      "source": [
        "",
        "text"
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
    "name": "search_web_tool",
    "arguments": {
      "query": "flight prices from NYC to New Delhi",
      "num_results": 5,
      "source": "text"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'num_results': 5. Expected one of ['', 3]."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "search_web_tool",
    "arguments": {
      "query": "flight prices from New York City to New Delhi 2025",
      "num_results": 5,
      "source": "text"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'query': 'flight prices from New York City to New Delhi 2025'. Expected one of ['flight prices from NYC to New Delhi']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "search_web_tool",
    "arguments": {
      "query": "flight prices from NYC to New Delhi"
    }
  }
]</pre>

</details>

## live_multiple_242-107-3

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 错误 | 3.427677 | 382 |
| Qwen3.8-27B | 错误 | 15.484498 | 615 |
| gemma-4-26B-A4B-it | 错误 | 0.464012 | 37 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: voice narration tool prompt "If you could have dinner with any historical figure, who would you choose and why?, also genart a photo of that figure"</pre>

### Official accepted answer

<pre>[
  {
    "tts_tool": {
      "content": [
        "If you could have dinner with any historical figure, who would you choose and why?, also genart a photo of that figure"
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
    "name": "tts_tool",
    "arguments": {
      "content": "If you could have dinner with any historical figure, who would you choose and why?",
      "speaker": "female",
      "file_name": "historical_figure_question"
    }
  },
  {
    "name": "generate_image_tool",
    "arguments": {
      "desc": "Leonardo da Vinci, the famous Italian Renaissance polymath, artist, and inventor, depicted in a detailed portrait showing his thoughtful expression, wearing period clothing from the 15th-16th century, with soft lighting highlighting his features, realistic style",
      "file_name": "leonardo_da_vinci"
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
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "tts_tool",
    "arguments": {
      "content": "If you could have dinner with any historical figure, I would choose Leonardo da Vinci. The man who painted the Mona Lisa was also an engineer, an anatomist, and an inventor who sketched flying machines centuries before the first airplane ever took off. Sitting across from him, I would want to ask how he managed to see connections between fields that everyone else kept separate — how the same curiosity that led him to study the flow of water also led him to study the human heart. I imagine his dinner table would be a place of constant questions, and I would want to be there to ask a few of my own.",
      "file_name": "dinner_with_da_vinci",
      "speaker": "female"
    }
  },
  {
    "name": "generate_image_tool",
    "arguments": {
      "desc": "A portrait of Leonardo da Vinci seated at a candlelit Renaissance dinner table, wearing his iconic red robe, with a long beard and thoughtful expression, quill pen and anatomical sketches on parchment in front of him, warm golden candlelight, oil painting style, rich detail",
      "file_name": "leonardo_da_vinci_dinner.png"
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
    "name": "tts_tool",
    "arguments": {
      "content": "If you could have dinner with any historical figure, who would you choose and why?",
      "speaker": "female"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'content': 'If you could have dinner with any historical figure, who would you choose and why?'. Expected one of ['If you could have dinner with any historical figure, who would you choose and why?, also genart a photo of that figure']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

## live_multiple_243-107-4

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 错误 | 1.660533 | 168 |
| Qwen3.8-27B | 错误 | 2.823446 | 90 |
| gemma-4-26B-A4B-it | 正确 | 0.379525 | 27 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: tool prompt "Find a recent news article about corona virus".</pre>

### Official accepted answer

<pre>[
  {
    "search_web_tool": {
      "query": [
        "Find a recent news article about corona virus",
        "recent news article about corona virus",
        "recent news corona virus"
      ],
      "num_results": [
        "",
        3
      ],
      "source": [
        "news"
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
    "name": "search_web_tool",
    "arguments": {
      "query": "corona virus recent news article",
      "source": "news",
      "num_results": 3
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'query': 'corona virus recent news article'. Expected one of ['Find a recent news article about corona virus', 'recent news article about corona virus', 'recent news corona virus']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "search_web_tool",
    "arguments": {
      "query": "coronavirus latest news",
      "source": "news",
      "num_results": 5
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'query': 'coronavirus latest news'. Expected one of ['Find a recent news article about corona virus', 'recent news article about corona virus', 'recent news corona virus']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "search_web_tool",
    "arguments": {
      "query": "recent news article about coronavirus",
      "source": "news"
    }
  }
]</pre>

</details>

## live_multiple_244-108-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.006564 | 100 |
| Qwen3.8-27B | 正确 | 1.930312 | 61 |
| gemma-4-26B-A4B-it | 正确 | 0.237998 | 16 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What is the version?</pre>

### Official accepted answer

<pre>[
  {
    "version_api.VersionApi.get_version": {}
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

## live_multiple_245-109-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 0.778242 | 79 |
| Qwen3.8-27B | 正确 | 1.53574 | 50 |
| gemma-4-26B-A4B-it | 正确 | 0.201205 | 16 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What is the application version?</pre>

### Official accepted answer

<pre>[
  {
    "version_api.VersionApi.get_version": {}
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

## live_multiple_246-110-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 0.80635 | 85 |
| Qwen3.8-27B | 正确 | 2.096811 | 77 |
| gemma-4-26B-A4B-it | 正确 | 0.178597 | 16 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What is the application version? Do not add parameters!</pre>

### Official accepted answer

<pre>[
  {
    "version_api.VersionApi.get_version": {}
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

## live_multiple_247-111-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.648657 | 301 |
| Qwen3.8-27B | 正确 | 6.86798 | 269 |
| gemma-4-26B-A4B-it | 正确 | 0.498761 | 54 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Can you retrieve the analysis trail for the vulnerability ef903ac-893-f00 within the component AB1010CD of my project with id SUPERFANCY?</pre>

### Official accepted answer

<pre>[
  {
    "analysis_api.AnalysisApi.retrieve_analysis": {
      "project": [
        "SUPERFANCY"
      ],
      "component": [
        "AB1010CD"
      ],
      "vulnerability": [
        "ef903ac-893-f00"
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
    "name": "analysis_api_AnalysisApi_retrieve_analysis",
    "arguments": {
      "project": "SUPERFANCY",
      "component": "AB1010CD",
      "vulnerability": "ef903ac-893-f00"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "analysis_api_AnalysisApi_retrieve_analysis",
    "arguments": {
      "project": "SUPERFANCY",
      "component": "AB1010CD",
      "vulnerability": "ef903ac-893-f00"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "analysis_api_AnalysisApi_retrieve_analysis",
    "arguments": {
      "component": "AB1010CD",
      "project": "SUPERFANCY",
      "vulnerability": "ef903ac-893-f00"
    }
  }
]</pre>

</details>

## live_multiple_248-112-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 0.864646 | 79 |
| Qwen3.8-27B | 正确 | 1.726529 | 50 |
| gemma-4-26B-A4B-it | 正确 | 0.269611 | 16 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: version?</pre>

### Official accepted answer

<pre>[
  {
    "version_api.VersionApi.get_version": {}
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

## live_multiple_249-113-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 0.862379 | 90 |
| Qwen3.8-27B | 正确 | 1.411154 | 44 |
| gemma-4-26B-A4B-it | 正确 | 0.19134 | 16 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: what version?</pre>

### Official accepted answer

<pre>[
  {
    "version_api.VersionApi.get_version": {}
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

## live_multiple_250-114-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 0.697942 | 68 |
| Qwen3.8-27B | 正确 | 1.631729 | 53 |
| gemma-4-26B-A4B-it | 正确 | 0.209568 | 16 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Version?</pre>

### Official accepted answer

<pre>[
  {
    "version_api.VersionApi.get_version": {}
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

## live_multiple_251-115-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 0.962428 | 102 |
| Qwen3.8-27B | 正确 | 1.7926 | 61 |
| gemma-4-26B-A4B-it | 正确 | 0.189914 | 16 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What is the version?</pre>

### Official accepted answer

<pre>[
  {
    "version_api.VersionApi.get_version": {}
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

## live_multiple_252-116-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 0.976322 | 101 |
| Qwen3.8-27B | 正确 | 2.493747 | 89 |
| gemma-4-26B-A4B-it | 正确 | 0.207543 | 16 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: what is the version? Provide the full API call</pre>

### Official accepted answer

<pre>[
  {
    "version_api.VersionApi.get_version": {}
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

## live_multiple_253-117-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.456075 | 281 |
| Qwen3.8-27B | 正确 | 4.887783 | 191 |
| gemma-4-26B-A4B-it | 正确 | 0.338608 | 35 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Provide metrics for the bandana project. Use version number 5.</pre>

### Official accepted answer

<pre>[
  {
    "badge_api.BadgeApi.get_project_vulnerabilities_badge": {
      "name": [
        "bandana",
        "bandana project"
      ],
      "version": [
        "5"
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
    "name": "badge_api_BadgeApi_get_project_vulnerabilities_badge",
    "arguments": {
      "name": "bandana",
      "version": "5"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "badge_api_BadgeApi_get_project_vulnerabilities_badge",
    "arguments": {
      "name": "bandana",
      "version": "5"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "badge_api_BadgeApi_get_project_vulnerabilities_badge",
    "arguments": {
      "name": "bandana",
      "version": "5"
    }
  }
]</pre>

</details>

## live_multiple_254-118-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.022953 | 227 |
| Qwen3.8-27B | 正确 | 2.957297 | 110 |
| gemma-4-26B-A4B-it | 正确 | 0.349653 | 36 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I want the violation badge for project bandana. The version is 5.</pre>

### Official accepted answer

<pre>[
  {
    "BadgeApi.get_project_policy_violations_badge1": {
      "project_name": [
        "bandana"
      ],
      "project_version": [
        "5"
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
    "name": "BadgeApi_get_project_policy_violations_badge1",
    "arguments": {
      "project_name": "bandana",
      "project_version": "5"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "BadgeApi_get_project_policy_violations_badge1",
    "arguments": {
      "project_name": "bandana",
      "project_version": "5"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "BadgeApi_get_project_policy_violations_badge1",
    "arguments": {
      "project_name": "bandana",
      "project_version": "5"
    }
  }
]</pre>

</details>

## live_multiple_255-119-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.108526 | 237 |
| Qwen3.8-27B | 正确 | 6.718992 | 265 |
| gemma-4-26B-A4B-it | 正确 | 0.316212 | 30 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I want the violation badge for project ID badae.</pre>

### Official accepted answer

<pre>[
  {
    "badge_api.BadgeApi.get_project_policy_violations_badge": {
      "uuid": [
        "badae"
      ],
      "format": [
        "",
        "svg"
      ],
      "style": [
        "",
        "flat"
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
    "name": "badge_api_BadgeApi_get_project_policy_violations_badge",
    "arguments": {
      "uuid": "badae"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>文本回复：


I'll generate the policy violations badge for project ID `badae`.



工具调用：
[
  {
    "name": "badge_api_BadgeApi_get_project_policy_violations_badge",
    "arguments": {
      "uuid": "badae"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "badge_api_BadgeApi_get_project_policy_violations_badge",
    "arguments": {
      "uuid": "badae"
    }
  }
]</pre>

</details>

## live_multiple_256-120-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.964959 | 333 |
| Qwen3.8-27B | 正确 | 4.753633 | 178 |
| gemma-4-26B-A4B-it | 正确 | 0.623837 | 66 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Returns a VEX for a project in CycloneDX format ofr project '123e4567-e89b-12d3-a456-426614174000'</pre>

### Official accepted answer

<pre>[
  {
    "vex_api.VexApi.export_project_as_cyclone_dx1": {
      "uuid": [
        "123e4567-e89b-12d3-a456-426614174000"
      ],
      "download": [
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
    "name": "vex_api_VexApi_export_project_as_cyclone_dx1",
    "arguments": {
      "uuid": "123e4567-e89b-12d3-a456-426614174000"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "vex_api_VexApi_export_project_as_cyclone_dx1",
    "arguments": {
      "uuid": "123e4567-e89b-12d3-a456-426614174000"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "vex_api_VexApi_export_project_as_cyclone_dx1",
    "arguments": {
      "uuid": "123e4567-e89b-12d3-a456-426614174000"
    }
  }
]</pre>

</details>

## live_multiple_257-121-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.343858 | 259 |
| Qwen3.8-27B | 正确 | 3.548112 | 128 |
| gemma-4-26B-A4B-it | 正确 | 0.405037 | 37 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: For project ID '1a1a-c6' give its VEX export it in the CycloneDX format</pre>

### Official accepted answer

<pre>[
  {
    "vex_api.VexApi.export_project_as_cyclone_dx1": {
      "uuid": [
        "1a1a-c6"
      ],
      "download": [
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
    "name": "vex_api_VexApi_export_project_as_cyclone_dx1",
    "arguments": {
      "uuid": "1a1a-c6"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "vex_api_VexApi_export_project_as_cyclone_dx1",
    "arguments": {
      "uuid": "1a1a-c6"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "vex_api_VexApi_export_project_as_cyclone_dx1",
    "arguments": {
      "uuid": "1a1a-c6"
    }
  }
]</pre>

</details>

## live_multiple_258-122-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.48077 | 163 |
| Qwen3.8-27B | 正确 | 2.814587 | 103 |
| gemma-4-26B-A4B-it | 正确 | 0.394518 | 41 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: see details for the 'Orion' version 2.1.3.</pre>

### Official accepted answer

<pre>[
  {
    "project_api.ProjectApi.get_project_by_name_and_version": {
      "name": [
        "Orion"
      ],
      "version": [
        "2.1.3"
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
    "name": "project_api_ProjectApi_get_project_by_name_and_version",
    "arguments": {
      "name": "Orion",
      "version": "2.1.3"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "project_api_ProjectApi_get_project_by_name_and_version",
    "arguments": {
      "name": "Orion",
      "version": "2.1.3"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "project_api_ProjectApi_get_project_by_name_and_version",
    "arguments": {
      "name": "Orion",
      "version": "2.1.3"
    }
  }
]</pre>

</details>

## live_multiple_259-123-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.743876 | 193 |
| Qwen3.8-27B | 正确 | 2.576251 | 92 |
| gemma-4-26B-A4B-it | 正确 | 0.422328 | 44 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I need project my_version_proj, with v 1.2.3</pre>

### Official accepted answer

<pre>[
  {
    "project_api.ProjectApi.get_project_by_name_and_version": {
      "name": [
        "my_version_proj"
      ],
      "version": [
        "1.2.3"
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
    "name": "project_api_ProjectApi_get_project_by_name_and_version",
    "arguments": {
      "name": "my_version_proj",
      "version": "1.2.3"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "project_api_ProjectApi_get_project_by_name_and_version",
    "arguments": {
      "name": "my_version_proj",
      "version": "1.2.3"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "project_api_ProjectApi_get_project_by_name_and_version",
    "arguments": {
      "name": "my_version_proj",
      "version": "1.2.3"
    }
  }
]</pre>

</details>

## live_multiple_260-124-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 0.930747 | 98 |
| Qwen3.8-27B | 正确 | 2.214111 | 79 |
| gemma-4-26B-A4B-it | 正确 | 0.1913 | 16 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: tell me the current version information of app, with name and version number?</pre>

### Official accepted answer

<pre>[
  {
    "version_api.VersionApi.get_version": {}
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "version_api_VersionApi_get_version",
    "arguments": {}
  }
]</pre>

</details>

## live_multiple_261-125-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.415992 | 143 |
| Qwen3.8-27B | 正确 | 3.870794 | 136 |
| gemma-4-26B-A4B-it | 正确 | 0.267037 | 14 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: rotate the image by 30 degrees</pre>

### Official accepted answer

<pre>[
  {
    "rotateImageAction": {
      "degrees": [
        30
      ],
      "image_format": [
        "",
        "JPEG"
      ],
      "keep_original": [
        "",
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
    "name": "rotateImageAction",
    "arguments": {
      "degrees": 30
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "rotateImageAction",
    "arguments": {
      "degrees": 30
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "rotateImageAction",
    "arguments": {
      "degrees": 30
    }
  }
]</pre>

</details>

## live_multiple_262-125-1

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 错误 | 5.037097 | 576 |
| Qwen3.8-27B | 正确 | 14.156317 | 560 |
| gemma-4-26B-A4B-it | 错误 | 0.503682 | 44 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: turn it by 20 degree and freeze it to 40 degree celsius</pre>

### Official accepted answer

<pre>[
  {
    "rotateImageAction": {
      "degrees": [
        20
      ],
      "image_format": [
        "",
        "JPEG"
      ],
      "keep_original": [
        "",
        true
      ]
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.5-9B — 错误</summary>

### Model output

<pre>未调用工具


I can help you rotate an image by 20 degrees, but I need to clarify a few things:

1. **Image Rotation**: I can rotate an image clockwise by 20 degrees using my image processing tools. However, I need you to provide the image file path or image data that you want to rotate.

2. **Temperature Setting**: I cannot "freeze to 40 degree celsius" as this is not an image processing operation. Temperature settings are not applicable to image manipulation. This might be a misunderstanding or you may be referring to something else.

Could you please:
- Provide the image file path or image data you want to rotate
- Clarify what you mean by "freeze it to 40 degree celsius" - is this related to image processing or something else?

Once you provide the image, I can rotate it by 20 degrees for you.</pre>

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

<pre>文本回复：


I can rotate the image for you, but I should flag that "freezing to 40 degrees Celsius" isn't something that applies to an image — there's no temperature or freezing operation in image editing (and 40°C isn't even a freezing temperature, which is 0°C). Let me handle the rotation part.



工具调用：
[
  {
    "name": "rotateImageAction",
    "arguments": {
      "degrees": 20
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 错误</summary>

### Model output

<pre>未调用工具
I can help you with the image rotation, but I don't have the ability to change the temperature of an object in a photo.

Would you like me to rotate the image by 20 degrees?</pre>

### Official diagnostic

<pre>[
  "Wrong number of functions."
]</pre>

### Provisional error group

<pre>工具集合不匹配</pre>

</details>

## live_multiple_263-126-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 错误 | 1.177205 | 127 |
| Qwen3.8-27B | 错误 | 1.841484 | 64 |
| gemma-4-26B-A4B-it | 正确 | 0.202703 | 17 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: When is my gym session?</pre>

### Official accepted answer

<pre>[
  {
    "EventQuery": {
      "search_string": [
        "gym session"
      ],
      "start_date": [
        "",
        "null"
      ],
      "end_date": [
        "",
        "null"
      ],
      "include_recurring": [
        "",
        false
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
    "name": "EventQuery",
    "arguments": {
      "search_string": "gym"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'search_string': 'gym'. Expected one of ['gym session']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "EventQuery",
    "arguments": {
      "search_string": "gym"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'search_string': 'gym'. Expected one of ['gym session']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "EventQuery",
    "arguments": {
      "search_string": "gym session"
    }
  }
]</pre>

</details>

## live_multiple_264-126-1

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 错误 | 2.139993 | 242 |
| Qwen3.8-27B | 错误 | 3.292856 | 123 |
| gemma-4-26B-A4B-it | 错误 | 0.457009 | 50 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I forgot the date for my trip. search between the April 1-April 30 2023?</pre>

### Official accepted answer

<pre>[
  {
    "EventQuery": {
      "search_string": [
        "trip"
      ],
      "start_date": [
        "2023-04-01"
      ],
      "end_date": [
        "2023-04-30"
      ],
      "include_recurring": [
        true
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
    "name": "EventQuery",
    "arguments": {
      "search_string": "trip",
      "start_date": "2023-04-01",
      "end_date": "2023-04-30"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Optional parameter 'include_recurring' not provided and not marked as optional."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "EventQuery",
    "arguments": {
      "search_string": "trip",
      "start_date": "2023-04-01",
      "end_date": "2023-04-30"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Optional parameter 'include_recurring' not provided and not marked as optional."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 错误</summary>

### Model output

<pre>[
  {
    "name": "EventQuery",
    "arguments": {
      "end_date": "2023-04-30",
      "search_string": "trip",
      "start_date": "2023-04-01"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Optional parameter 'include_recurring' not provided and not marked as optional."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

## live_multiple_265-127-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.296498 | 118 |
| Qwen3.8-27B | 正确 | 2.367524 | 64 |
| gemma-4-26B-A4B-it | 正确 | 0.38083 | 19 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: what is the weather like in Hanoi</pre>

### Official accepted answer

<pre>[
  {
    "Weather_1_GetWeather": {
      "city": [
        "Hanoi"
      ],
      "date": [
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
    "name": "Weather_1_GetWeather",
    "arguments": {
      "city": "Hanoi"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Weather_1_GetWeather",
    "arguments": {
      "city": "Hanoi"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Weather_1_GetWeather",
    "arguments": {
      "city": "Hanoi"
    }
  }
]</pre>

</details>

## live_multiple_266-127-1

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.64698 | 160 |
| Qwen3.8-27B | 正确 | 2.297226 | 61 |
| gemma-4-26B-A4B-it | 正确 | 0.380699 | 19 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What will the weather in San Diego be like.</pre>

### Official accepted answer

<pre>[
  {
    "Weather_1_GetWeather": {
      "city": [
        "San Diego"
      ],
      "date": [
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
    "name": "Weather_1_GetWeather",
    "arguments": {
      "city": "San Diego"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Weather_1_GetWeather",
    "arguments": {
      "city": "San Diego"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Weather_1_GetWeather",
    "arguments": {
      "city": "San Diego"
    }
  }
]</pre>

</details>

## live_multiple_267-127-2

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.553465 | 148 |
| Qwen3.8-27B | 正确 | 3.666775 | 118 |
| gemma-4-26B-A4B-it | 正确 | 0.494386 | 33 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Can you tell me what the weather will be like in Vancouver on the April 4th 2023</pre>

### Official accepted answer

<pre>[
  {
    "Weather_1_GetWeather": {
      "city": [
        "Vancouver"
      ],
      "date": [
        "2023-04-04"
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
    "name": "Weather_1_GetWeather",
    "arguments": {
      "city": "Vancouver",
      "date": "2023-04-04"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Weather_1_GetWeather",
    "arguments": {
      "city": "Vancouver",
      "date": "2023-04-04"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Weather_1_GetWeather",
    "arguments": {
      "city": "Vancouver",
      "date": "2023-04-04"
    }
  }
]</pre>

</details>

## live_multiple_268-127-3

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.126356 | 216 |
| Qwen3.8-27B | 正确 | 4.972209 | 172 |
| gemma-4-26B-A4B-it | 正确 | 0.513228 | 35 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I need to see what the weather will be like in London, UK on the 12th of March. it's 2023 right now</pre>

### Official accepted answer

<pre>[
  {
    "Weather_1_GetWeather": {
      "city": [
        "London, UK",
        "London"
      ],
      "date": [
        "2023-03-12"
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
    "name": "Weather_1_GetWeather",
    "arguments": {
      "city": "London, UK",
      "date": "2023-03-12"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Weather_1_GetWeather",
    "arguments": {
      "city": "London, UK",
      "date": "2023-03-12"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Weather_1_GetWeather",
    "arguments": {
      "city": "London, UK",
      "date": "2023-03-12"
    }
  }
]</pre>

</details>

## live_multiple_269-127-4

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 错误 | 2.504993 | 262 |
| Qwen3.8-27B | 正确 | 23.765375 | 952 |
| gemma-4-26B-A4B-it | 错误 | 0.495405 | 33 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What is the weather going to be like Wednesday next week in Philly? today is 2023.3.1 monday</pre>

### Official accepted answer

<pre>[
  {
    "Weather_1_GetWeather": {
      "city": [
        "Philadelphia"
      ],
      "date": [
        "2023-03-10"
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
    "name": "Weather_1_GetWeather",
    "arguments": {
      "city": "Philadelphia",
      "date": "2023-03-08"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'date': '2023-03-08'. Expected one of ['2023-03-10']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Weather_1_GetWeather",
    "arguments": {
      "city": "Philadelphia",
      "date": "2023-03-10"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 错误</summary>

### Model output

<pre>[
  {
    "name": "Weather_1_GetWeather",
    "arguments": {
      "city": "Philadelphia",
      "date": "2023-03-08"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'date': '2023-03-08'. Expected one of ['2023-03-10']. Case insensitive."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>


[Category index](README.md) · [All categories](../README.md) · [Previous](page-008.md) · [Next](page-010.md)
