# simple_python — page 8/14

[Category index](README.md) · [All categories](../README.md) · [Previous](page-007.md) · [Next](page-009.md)

30 cases. Expand the question/answer and model sections below. Tool calls were scored, not executed.

## simple_python_210

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.326623 | 151 |
| Qwen3.8-27B | 正确 | 2.483089 | 91 |
| gemma-4-26B-A4B-it | 正确 | 0.240497 | 25 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Get 5 latest news on Bitcoin in US</pre>

### Official accepted answer

<pre>[
  {
    "get_news": {
      "topic": [
        "Bitcoin"
      ],
      "quantity": [
        5
      ],
      "region": [
        "US",
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
    "name": "get_news",
    "arguments": {
      "topic": "Bitcoin",
      "quantity": 5,
      "region": "US"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_news",
    "arguments": {
      "topic": "Bitcoin",
      "quantity": 5,
      "region": "US"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_news",
    "arguments": {
      "quantity": 5,
      "region": "US",
      "topic": "Bitcoin"
    }
  }
]</pre>

</details>

## simple_python_211

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.741145 | 199 |
| Qwen3.8-27B | 正确 | 4.30475 | 163 |
| gemma-4-26B-A4B-it | 正确 | 0.368938 | 42 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Send an email to John Doe at john.doe@example.com with the subject 'Meeting' and body 'Let's meet at 10 AM tomorrow'.</pre>

### Official accepted answer

<pre>[
  {
    "send_email": {
      "to": [
        "john.doe@example.com"
      ],
      "subject": [
        "Meeting"
      ],
      "body": [
        "Let's meet at 10 AM tomorrow",
        "Let's meet at 10 AM tomorrow."
      ],
      "cc": [
        ""
      ],
      "bcc": [
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
    "name": "send_email",
    "arguments": {
      "to": "john.doe@example.com",
      "subject": "Meeting",
      "body": "Let's meet at 10 AM tomorrow"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "send_email",
    "arguments": {
      "to": "john.doe@example.com",
      "subject": "Meeting",
      "body": "Let's meet at 10 AM tomorrow"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "send_email",
    "arguments": {
      "body": "Let's meet at 10 AM tomorrow",
      "subject": "Meeting",
      "to": "john.doe@example.com"
    }
  }
]</pre>

</details>

## simple_python_212

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.570486 | 180 |
| Qwen3.8-27B | 正确 | 2.74362 | 101 |
| gemma-4-26B-A4B-it | 正确 | 0.273699 | 29 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Give me detail information about stocks of Apple Inc.</pre>

### Official accepted answer

<pre>[
  {
    "get_stock_info": {
      "company_name": [
        "Apple Inc."
      ],
      "detail_level": [
        "detailed"
      ],
      "market": [
        "",
        "NASDAQ"
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
    "name": "get_stock_info",
    "arguments": {
      "company_name": "Apple Inc.",
      "detail_level": "detailed",
      "market": "NASDAQ"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_stock_info",
    "arguments": {
      "company_name": "Apple Inc.",
      "detail_level": "detailed",
      "market": "NASDAQ"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_stock_info",
    "arguments": {
      "company_name": "Apple Inc.",
      "detail_level": "detailed"
    }
  }
]</pre>

</details>

## simple_python_213

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.841317 | 211 |
| Qwen3.8-27B | 正确 | 4.524158 | 172 |
| gemma-4-26B-A4B-it | 正确 | 0.456177 | 54 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Book a direct flight from San Francisco to London for 2022-04-27 afternoon</pre>

### Official accepted answer

<pre>[
  {
    "flight.book": {
      "departure_location": [
        "San Francisco",
        "SF"
      ],
      "destination_location": [
        "London"
      ],
      "date": [
        "2022-04-27",
        "04/27/2022",
        "Apr 27, 2022"
      ],
      "time": [
        "afternoon",
        ""
      ],
      "direct_flight": [
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
    "name": "flight_book",
    "arguments": {
      "departure_location": "San Francisco",
      "destination_location": "London",
      "date": "2022-04-27",
      "time": "afternoon",
      "direct_flight": true
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "flight_book",
    "arguments": {
      "departure_location": "San Francisco",
      "destination_location": "London",
      "date": "2022-04-27",
      "time": "afternoon",
      "direct_flight": true
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "flight_book",
    "arguments": {
      "date": "2022-04-27",
      "departure_location": "San Francisco",
      "destination_location": "London",
      "direct_flight": true,
      "time": "afternoon"
    }
  }
]</pre>

</details>

## simple_python_214

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.884551 | 218 |
| Qwen3.8-27B | 正确 | 3.535022 | 133 |
| gemma-4-26B-A4B-it | 正确 | 0.313921 | 35 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Search for upcoming month rock concerts in New York.</pre>

### Official accepted answer

<pre>[
  {
    "event_finder.find_upcoming": {
      "location": [
        "New York",
        "New York, NY",
        "NYC"
      ],
      "genre": [
        "Rock",
        "rock"
      ],
      "days_ahead": [
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
    "name": "event_finder_find_upcoming",
    "arguments": {
      "location": "New York, NY",
      "genre": "rock",
      "days_ahead": 30
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "event_finder_find_upcoming",
    "arguments": {
      "location": "New York, NY",
      "genre": "rock",
      "days_ahead": 30
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "event_finder_find_upcoming",
    "arguments": {
      "days_ahead": 30,
      "genre": "rock",
      "location": "New York, NY"
    }
  }
]</pre>

</details>

## simple_python_215

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.374149 | 157 |
| Qwen3.8-27B | 正确 | 2.550118 | 95 |
| gemma-4-26B-A4B-it | 正确 | 0.187479 | 18 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Give me a brief on movie 'Interstellar'</pre>

### Official accepted answer

<pre>[
  {
    "movie_details.brief": {
      "title": [
        "Interstellar"
      ],
      "extra_info": [
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
    "name": "movie_details_brief",
    "arguments": {
      "title": "Interstellar",
      "extra_info": false
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "movie_details_brief",
    "arguments": {
      "title": "Interstellar"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "movie_details_brief",
    "arguments": {
      "title": "Interstellar"
    }
  }
]</pre>

</details>

## simple_python_216

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.086957 | 122 |
| Qwen3.8-27B | 正确 | 2.428603 | 89 |
| gemma-4-26B-A4B-it | 正确 | 0.305886 | 34 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Analyze the sentiment of a customer review 'I love the food here! It's always fresh and delicious.'.</pre>

### Official accepted answer

<pre>[
  {
    "sentiment_analysis": {
      "text": [
        "I love the food here! It's always fresh and delicious."
      ],
      "language": [
        "english",
        "English",
        "en"
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
    "name": "sentiment_analysis",
    "arguments": {
      "text": "I love the food here! It's always fresh and delicious.",
      "language": "English"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "sentiment_analysis",
    "arguments": {
      "text": "I love the food here! It's always fresh and delicious.",
      "language": "English"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "sentiment_analysis",
    "arguments": {
      "language": "English",
      "text": "I love the food here! It's always fresh and delicious."
    }
  }
]</pre>

</details>

## simple_python_217

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.972045 | 227 |
| Qwen3.8-27B | 正确 | 5.051678 | 195 |
| gemma-4-26B-A4B-it | 正确 | 0.397634 | 46 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Analyze my fMRI data in ~/data/myfMRI.nii from a multi-band sequence, that is smoothed at 6mm with an isotropic voxel size of 2mm.</pre>

### Official accepted answer

<pre>[
  {
    "fMRI.analyze": {
      "data_source": [
        "~/data/myfMRI.nii"
      ],
      "sequence_type": [
        "multi-band"
      ],
      "smooth": [
        6
      ],
      "voxel_size": [
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
    "name": "fMRI_analyze",
    "arguments": {
      "data_source": "~/data/myfMRI.nii",
      "sequence_type": "multi-band",
      "smooth": 6,
      "voxel_size": 2
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "fMRI_analyze",
    "arguments": {
      "data_source": "~/data/myfMRI.nii",
      "sequence_type": "multi-band",
      "smooth": 6,
      "voxel_size": 2
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "fMRI_analyze",
    "arguments": {
      "data_source": "~/data/myfMRI.nii",
      "sequence_type": "multi-band",
      "smooth": 6,
      "voxel_size": 2
    }
  }
]</pre>

</details>

## simple_python_218

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.530449 | 174 |
| Qwen3.8-27B | 正确 | 2.752901 | 98 |
| gemma-4-26B-A4B-it | 正确 | 0.375488 | 43 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Given patient with id 546382, retrieve their brain MRI report with the status 'concluded'.</pre>

### Official accepted answer

<pre>[
  {
    "patient.get_mri_report": {
      "patient_id": [
        "546382"
      ],
      "mri_type": [
        "brain",
        ""
      ],
      "status": [
        "concluded"
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
    "name": "patient_get_mri_report",
    "arguments": {
      "patient_id": "546382",
      "mri_type": "brain",
      "status": "concluded"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "patient_get_mri_report",
    "arguments": {
      "patient_id": "546382",
      "mri_type": "brain",
      "status": "concluded"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "patient_get_mri_report",
    "arguments": {
      "mri_type": "brain",
      "patient_id": "546382",
      "status": "concluded"
    }
  }
]</pre>

</details>

## simple_python_219

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.794037 | 207 |
| Qwen3.8-27B | 正确 | 2.933962 | 109 |
| gemma-4-26B-A4B-it | 正确 | 0.262628 | 28 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What are the coordinates of the neuron in a rat's all part of the brain that produces GABA neurotransmitters?</pre>

### Official accepted answer

<pre>[
  {
    "get_neuron_coordinates": {
      "neuron_type": [
        "GABA"
      ],
      "brain_region": [
        "All",
        "all part of the brain",
        "entire brain"
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
    "name": "get_neuron_coordinates",
    "arguments": {
      "neuron_type": "GABA",
      "brain_region": "All"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_neuron_coordinates",
    "arguments": {
      "neuron_type": "GABA",
      "brain_region": "All"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_neuron_coordinates",
    "arguments": {
      "brain_region": "all",
      "neuron_type": "GABA"
    }
  }
]</pre>

</details>

## simple_python_220

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.603278 | 182 |
| Qwen3.8-27B | 正确 | 3.983413 | 150 |
| gemma-4-26B-A4B-it | 正确 | 0.334243 | 37 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Calculate the neuronal activity based on synaptic input rate of 200 and weight 0.5 and decay rate of 0.1.</pre>

### Official accepted answer

<pre>[
  {
    "calculate_neuronal_activity": {
      "input_synaptic_rate": [
        200
      ],
      "weight": [
        0.5
      ],
      "decay_rate": [
        0.1
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
    "name": "calculate_neuronal_activity",
    "arguments": {
      "input_synaptic_rate": 200,
      "weight": 0.5,
      "decay_rate": 0.1
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_neuronal_activity",
    "arguments": {
      "input_synaptic_rate": 200,
      "weight": 0.5,
      "decay_rate": 0.1
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_neuronal_activity",
    "arguments": {
      "decay_rate": 0.1,
      "input_synaptic_rate": 200,
      "weight": 0.5
    }
  }
]</pre>

</details>

## simple_python_221

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.158749 | 131 |
| Qwen3.8-27B | 正确 | 3.188955 | 119 |
| gemma-4-26B-A4B-it | 正确 | 0.20968 | 21 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What will be the population growth in London over the next five years?</pre>

### Official accepted answer

<pre>[
  {
    "population_growth_estimate": {
      "location": [
        "London"
      ],
      "years": [
        5
      ],
      "rate": [
        "",
        1.2
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
    "name": "population_growth_estimate",
    "arguments": {
      "location": "London",
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
    "name": "population_growth_estimate",
    "arguments": {
      "location": "London",
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
    "name": "population_growth_estimate",
    "arguments": {
      "location": "London",
      "years": 5
    }
  }
]</pre>

</details>

## simple_python_222

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.288432 | 145 |
| Qwen3.8-27B | 正确 | 2.671999 | 97 |
| gemma-4-26B-A4B-it | 正确 | 0.203538 | 20 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Can you calculate my Body Mass Index (BMI) given my weight is 70 kg and height is 180 cm?</pre>

### Official accepted answer

<pre>[
  {
    "calculate_bmi": {
      "weight": [
        70
      ],
      "height": [
        180
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
    "name": "calculate_bmi",
    "arguments": {
      "weight": 70,
      "height": 180
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_bmi",
    "arguments": {
      "weight": 70,
      "height": 180
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "calculate_bmi",
    "arguments": {
      "height": 180,
      "weight": 70
    }
  }
]</pre>

</details>

## simple_python_223

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.756337 | 203 |
| Qwen3.8-27B | 正确 | 3.747408 | 141 |
| gemma-4-26B-A4B-it | 正确 | 0.275807 | 29 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find social behaviors and patterns in a group size of 50 with extroverted members being 15 and introverted members being 35.</pre>

### Official accepted answer

<pre>[
  {
    "group_dynamics.pattern": {
      "total": [
        50
      ],
      "extroverts": [
        15
      ],
      "introverts": [
        35
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
    "name": "group_dynamics_pattern",
    "arguments": {
      "total": 50,
      "extroverts": 15,
      "introverts": 35
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "group_dynamics_pattern",
    "arguments": {
      "total": 50,
      "extroverts": 15,
      "introverts": 35
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "group_dynamics_pattern",
    "arguments": {
      "extroverts": 15,
      "introverts": 35,
      "total": 50
    }
  }
]</pre>

</details>

## simple_python_224

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 错误 | 1.994079 | 229 |
| Qwen3.8-27B | 正确 | 3.657811 | 139 |
| gemma-4-26B-A4B-it | 错误 | 0.367716 | 42 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find the most followed person on twitter who tweets about psychology related to behaviour and group dynamics.</pre>

### Official accepted answer

<pre>[
  {
    "social_media_analytics.most_followed": {
      "topic": [
        "psychology"
      ],
      "sub_topics": [
        [
          "behaviour",
          "group dynamics"
        ]
      ],
      "region": [
        "",
        "all"
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
    "name": "social_media_analytics_most_followed",
    "arguments": {
      "topic": "psychology",
      "sub_topics": [
        "behavior",
        "group dynamics"
      ],
      "region": "all"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'sub_topics': ['behavior', 'group dynamics']. Expected one of [['behaviour', 'group dynamics']]."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "social_media_analytics_most_followed",
    "arguments": {
      "topic": "psychology",
      "sub_topics": [
        "behaviour",
        "group dynamics"
      ]
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 错误</summary>

### Model output

<pre>[
  {
    "name": "social_media_analytics_most_followed",
    "arguments": {
      "sub_topics": [
        "behavioral psychology",
        "group dynamics",
        "social psychology"
      ],
      "topic": "psychology"
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'sub_topics': ['behavioral psychology', 'group dynamics', 'social psychology']. Expected one of [['behaviour', 'group dynamics']]."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

## simple_python_225

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.754846 | 201 |
| Qwen3.8-27B | 正确 | 3.537897 | 134 |
| gemma-4-26B-A4B-it | 正确 | 0.333437 | 37 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What is the percentage of population preferring digital reading over physical books?</pre>

### Official accepted answer

<pre>[
  {
    "psych_research.get_preference": {
      "category": [
        "reading"
      ],
      "option_one": [
        "digital reading",
        "digital"
      ],
      "option_two": [
        "physical book",
        "physical",
        "physical books"
      ],
      "demographic": [
        "",
        "all"
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
    "name": "psych_research_get_preference",
    "arguments": {
      "category": "reading",
      "option_one": "digital reading",
      "option_two": "physical books",
      "demographic": "all"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "psych_research_get_preference",
    "arguments": {
      "category": "reading",
      "option_one": "digital reading",
      "option_two": "physical books",
      "demographic": "all"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "psych_research_get_preference",
    "arguments": {
      "category": "reading",
      "option_one": "digital reading",
      "option_two": "physical books"
    }
  }
]</pre>

</details>

## simple_python_226

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.210349 | 137 |
| Qwen3.8-27B | 正确 | 2.143878 | 78 |
| gemma-4-26B-A4B-it | 正确 | 0.30705 | 34 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find the compatibility score in percentage of Aries with Gemini.</pre>

### Official accepted answer

<pre>[
  {
    "get_zodiac_compatibility": {
      "sign1": [
        "Aries"
      ],
      "sign2": [
        "Gemini"
      ],
      "scale": [
        "percentage",
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
    "name": "get_zodiac_compatibility",
    "arguments": {
      "sign1": "Aries",
      "sign2": "Gemini",
      "scale": "percentage"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_zodiac_compatibility",
    "arguments": {
      "sign1": "Aries",
      "sign2": "Gemini",
      "scale": "percentage"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_zodiac_compatibility",
    "arguments": {
      "scale": "percentage",
      "sign1": "Aries",
      "sign2": "Gemini"
    }
  }
]</pre>

</details>

## simple_python_227

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.093642 | 123 |
| Qwen3.8-27B | 正确 | 2.648525 | 95 |
| gemma-4-26B-A4B-it | 正确 | 0.276261 | 30 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Get me strength and weakness traits for ENFJ personality type.</pre>

### Official accepted answer

<pre>[
  {
    "get_personality_traits": {
      "type": [
        "ENFJ"
      ],
      "traits": [
        [
          "strengths",
          "weaknesses"
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
    "name": "get_personality_traits",
    "arguments": {
      "type": "ENFJ",
      "traits": [
        "strengths",
        "weaknesses"
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
    "name": "get_personality_traits",
    "arguments": {
      "type": "ENFJ",
      "traits": [
        "strengths",
        "weaknesses"
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
    "name": "get_personality_traits",
    "arguments": {
      "traits": [
        "strengths",
        "weaknesses"
      ],
      "type": "ENFJ"
    }
  }
]</pre>

</details>

## simple_python_228

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.433132 | 164 |
| Qwen3.8-27B | 正确 | 2.215584 | 81 |
| gemma-4-26B-A4B-it | 正确 | 0.231012 | 24 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find three personality traits of people who like jogging.</pre>

### Official accepted answer

<pre>[
  {
    "get_personality_traits": {
      "hobby": [
        "jogging"
      ],
      "trait_count": [
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
    "name": "get_personality_traits",
    "arguments": {
      "hobby": "jogging",
      "trait_count": 3
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_personality_traits",
    "arguments": {
      "hobby": "jogging",
      "trait_count": 3
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_personality_traits",
    "arguments": {
      "hobby": "jogging",
      "trait_count": 3
    }
  }
]</pre>

</details>

## simple_python_229

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.420922 | 162 |
| Qwen3.8-27B | 正确 | 2.353865 | 86 |
| gemma-4-26B-A4B-it | 正确 | 0.291917 | 32 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What's my Big Five Personality trait scores given that I am efficient, organized, easy going and compassionate?</pre>

### Official accepted answer

<pre>[
  {
    "get_bigfive_scores": {
      "characteristics": [
        [
          "efficient",
          "organized",
          "easy going",
          "compassionate"
        ]
      ],
      "scale": [
        "medium",
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
    "name": "get_bigfive_scores",
    "arguments": {
      "characteristics": [
        "efficient",
        "organized",
        "easy going",
        "compassionate"
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
    "name": "get_bigfive_scores",
    "arguments": {
      "characteristics": [
        "efficient",
        "organized",
        "easy going",
        "compassionate"
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
    "name": "get_bigfive_scores",
    "arguments": {
      "characteristics": [
        "efficient",
        "organized",
        "easy going",
        "compassionate"
      ]
    }
  }
]</pre>

</details>

## simple_python_230

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.374444 | 157 |
| Qwen3.8-27B | 正确 | 2.740323 | 102 |
| gemma-4-26B-A4B-it | 正确 | 0.278882 | 30 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Who was the King of France in 1510?</pre>

### Official accepted answer

<pre>[
  {
    "historic_leader_search": {
      "location": [
        "France"
      ],
      "date": [
        1510
      ],
      "title": [
        "King",
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
    "name": "historic_leader_search",
    "arguments": {
      "location": "France",
      "date": 1510,
      "title": "King"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "historic_leader_search",
    "arguments": {
      "location": "France",
      "date": 1510,
      "title": "King"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "historic_leader_search",
    "arguments": {
      "date": 1510,
      "location": "France",
      "title": "King"
    }
  }
]</pre>

</details>

## simple_python_231

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.639704 | 187 |
| Qwen3.8-27B | 正确 | 3.80021 | 144 |
| gemma-4-26B-A4B-it | 正确 | 0.394337 | 45 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Provide key war events in German history from 1871 to 1945.</pre>

### Official accepted answer

<pre>[
  {
    "history.get_key_events": {
      "country": [
        "Germany",
        "DE"
      ],
      "start_year": [
        1871
      ],
      "end_year": [
        1945
      ],
      "event_type": [
        [
          "War"
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
    "name": "history_get_key_events",
    "arguments": {
      "country": "Germany",
      "start_year": 1871,
      "end_year": 1945,
      "event_type": [
        "War"
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
    "name": "history_get_key_events",
    "arguments": {
      "country": "Germany",
      "start_year": 1871,
      "end_year": 1945,
      "event_type": [
        "War"
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
    "name": "history_get_key_events",
    "arguments": {
      "country": "Germany",
      "end_year": 1945,
      "event_type": [
        "War"
      ],
      "start_year": 1871
    }
  }
]</pre>

</details>

## simple_python_232

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.467937 | 168 |
| Qwen3.8-27B | 正确 | 3.529075 | 134 |
| gemma-4-26B-A4B-it | 正确 | 0.278525 | 30 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: What was the full name king of England in 1800?</pre>

### Official accepted answer

<pre>[
  {
    "monarch.getMonarchOfYear": {
      "location": [
        "England",
        "ENG"
      ],
      "year": [
        1800
      ],
      "fullName": [
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
    "name": "monarch_getMonarchOfYear",
    "arguments": {
      "location": "England",
      "year": 1800,
      "fullName": true
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "monarch_getMonarchOfYear",
    "arguments": {
      "location": "England",
      "year": 1800,
      "fullName": true
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "monarch_getMonarchOfYear",
    "arguments": {
      "fullName": true,
      "location": "England",
      "year": 1800
    }
  }
]</pre>

</details>

## simple_python_233

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.254314 | 140 |
| Qwen3.8-27B | 正确 | 3.795205 | 145 |
| gemma-4-26B-A4B-it | 正确 | 0.31067 | 34 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: When did the Treaty of Tordesillas take place? Put it in the format of YYYY.</pre>

### Official accepted answer

<pre>[
  {
    "european_history.get_event_date": {
      "event_name": [
        "Treaty of Tordesillas"
      ],
      "format": [
        "YYYY"
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
    "name": "european_history_get_event_date",
    "arguments": {
      "event_name": "Treaty of Tordesillas",
      "format": "YYYY"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "european_history_get_event_date",
    "arguments": {
      "event_name": "Treaty of Tordesillas",
      "format": "YYYY"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "european_history_get_event_date",
    "arguments": {
      "event_name": "Treaty of Tordesillas",
      "format": "YYYY"
    }
  }
]</pre>

</details>

## simple_python_234

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 3.916561 | 460 |
| Qwen3.8-27B | 错误 | 9.111832 | 359 |
| gemma-4-26B-A4B-it | 正确 | 0.279094 | 30 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find important Wars in European history during the 19th century.</pre>

### Official accepted answer

<pre>[
  {
    "history_eu.fetch_events": {
      "century": [
        19
      ],
      "region": [
        "Northern",
        "Southern",
        "Eastern",
        "Western"
      ],
      "category": [
        "Wars"
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
    "name": "history_eu_fetch_events",
    "arguments": {
      "century": 19,
      "region": "Western",
      "category": "Wars"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "history_eu_fetch_events",
    "arguments": {
      "century": 19,
      "region": "Northern",
      "category": "Wars"
    }
  },
  {
    "name": "history_eu_fetch_events",
    "arguments": {
      "century": 19,
      "region": "Southern",
      "category": "Wars"
    }
  },
  {
    "name": "history_eu_fetch_events",
    "arguments": {
      "century": 19,
      "region": "Eastern",
      "category": "Wars"
    }
  },
  {
    "name": "history_eu_fetch_events",
    "arguments": {
      "century": 19,
      "region": "Western",
      "category": "Wars"
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
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "history_eu_fetch_events",
    "arguments": {
      "category": "Wars",
      "century": 19,
      "region": "Western"
    }
  }
]</pre>

</details>

## simple_python_235

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 0.914212 | 101 |
| Qwen3.8-27B | 正确 | 2.424281 | 90 |
| gemma-4-26B-A4B-it | 正确 | 0.216694 | 22 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: When was the signing of the Treaty of Lisbon?</pre>

### Official accepted answer

<pre>[
  {
    "get_event_date": {
      "event": [
        "Treaty of Lisbon",
        "Signing of the Treaty of Lisbon",
        "The signing of the Treaty of Lisbon"
      ],
      "location": [
        "",
        "Lisbon",
        "Lisbon, Portugal"
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
    "name": "get_event_date",
    "arguments": {
      "event": "Treaty of Lisbon"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_event_date",
    "arguments": {
      "event": "signing of the Treaty of Lisbon",
      "location": "Lisbon, Portugal"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_event_date",
    "arguments": {
      "event": "signing of the Treaty of Lisbon"
    }
  }
]</pre>

</details>

## simple_python_236

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.232934 | 139 |
| Qwen3.8-27B | 正确 | 2.710801 | 97 |
| gemma-4-26B-A4B-it | 正确 | 0.308751 | 34 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Get start date on the American Civil War.</pre>

### Official accepted answer

<pre>[
  {
    "us_history.get_event_info": {
      "event_name": [
        "American Civil War",
        "Civil War"
      ],
      "specific_info": [
        "Start Date"
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
    "name": "us_history_get_event_info",
    "arguments": {
      "event_name": "American Civil War",
      "specific_info": "Start Date"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "us_history_get_event_info",
    "arguments": {
      "event_name": "American Civil War",
      "specific_info": "Start Date"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "us_history_get_event_info",
    "arguments": {
      "event_name": "American Civil War",
      "specific_info": "Start Date"
    }
  }
]</pre>

</details>

## simple_python_237

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.445482 | 164 |
| Qwen3.8-27B | 正确 | 3.752191 | 141 |
| gemma-4-26B-A4B-it | 正确 | 0.322324 | 36 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Get historical GDP data for United States from 1960 to 2000.</pre>

### Official accepted answer

<pre>[
  {
    "get_historical_GDP": {
      "country": [
        "United States",
        "US"
      ],
      "start_year": [
        1960
      ],
      "end_year": [
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
    "name": "get_historical_GDP",
    "arguments": {
      "country": "United States",
      "start_year": 1960,
      "end_year": 2000
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_historical_GDP",
    "arguments": {
      "country": "United States",
      "start_year": 1960,
      "end_year": 2000
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "get_historical_GDP",
    "arguments": {
      "country": "United States",
      "end_year": 2000,
      "start_year": 1960
    }
  }
]</pre>

</details>

## simple_python_238

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.573324 | 180 |
| Qwen3.8-27B | 错误 | 8.807684 | 346 |
| gemma-4-26B-A4B-it | 正确 | 0.262861 | 28 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Who was the president of the United States during the American Civil War?</pre>

### Official accepted answer

<pre>[
  {
    "us_history.get_president": {
      "event": [
        "American Civil War"
      ],
      "year": [
        1861,
        1862,
        1863,
        1864,
        1865
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
    "name": "us_history_get_president",
    "arguments": {
      "event": "American Civil War",
      "year": 1861
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "us_history_get_president",
    "arguments": {
      "event": "American Civil War",
      "year": 1861
    }
  },
  {
    "name": "us_history_get_president",
    "arguments": {
      "event": "American Civil War",
      "year": 1865
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
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "us_history_get_president",
    "arguments": {
      "event": "American Civil War",
      "year": 1861
    }
  }
]</pre>

</details>

## simple_python_239

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.243333 | 142 |
| Qwen3.8-27B | 正确 | 2.476847 | 92 |
| gemma-4-26B-A4B-it | 正确 | 0.249379 | 26 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Who was the full name of the president of the United States in 1861?</pre>

### Official accepted answer

<pre>[
  {
    "US_president.in_year": {
      "year": [
        1861
      ],
      "full_name": [
        true,
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
    "name": "US_president_in_year",
    "arguments": {
      "year": 1861,
      "full_name": true
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "US_president_in_year",
    "arguments": {
      "year": 1861,
      "full_name": true
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "US_president_in_year",
    "arguments": {
      "full_name": true,
      "year": 1861
    }
  }
]</pre>

</details>


[Category index](README.md) · [All categories](../README.md) · [Previous](page-007.md) · [Next](page-009.md)
