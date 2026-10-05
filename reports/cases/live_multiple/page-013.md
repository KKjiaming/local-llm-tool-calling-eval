# live_multiple — page 13/36

[Category index](README.md) · [All categories](../README.md) · [Previous](page-012.md) · [Next](page-014.md)

30 cases. Expand the question/answer and model sections below. Tool calls were scored, not executed.

## live_multiple_360-134-5

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.448332 | 152 |
| Qwen3.8-27B | 正确 | 3.141681 | 108 |
| gemma-4-26B-A4B-it | 正确 | 0.351897 | 29 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Can you find me a movie in the Play genre, directed by Paul Downs Colaizzo</pre>

### Official accepted answer

<pre>[
  {
    "Movies_3_FindMovies": {
      "directed_by": [
        "Paul Downs Colaizzo"
      ],
      "genre": [
        "Play"
      ],
      "cast": [
        "",
        "dontcare"
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
    "name": "Movies_3_FindMovies",
    "arguments": {
      "genre": "Play",
      "directed_by": "Paul Downs Colaizzo",
      "cast": "dontcare"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Paul Downs Colaizzo",
      "genre": "Play",
      "cast": "dontcare"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Paul Downs Colaizzo",
      "genre": "Play"
    }
  }
]</pre>

</details>

## live_multiple_361-134-6

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.707999 | 183 |
| Qwen3.8-27B | 正确 | 3.298518 | 115 |
| gemma-4-26B-A4B-it | 正确 | 0.415443 | 37 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I need your advice in finding a movie to watch. I want it to be an action movie with ryan reynolds and directed by david leitch</pre>

### Official accepted answer

<pre>[
  {
    "Movies_3_FindMovies": {
      "directed_by": [
        "david leitch"
      ],
      "genre": [
        "Action"
      ],
      "cast": [
        "ryan reynolds"
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
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "David Leitch",
      "genre": "Action",
      "cast": "Ryan Reynolds"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "David Leitch",
      "genre": "Action",
      "cast": "Ryan Reynolds"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "cast": "ryan reynolds",
      "directed_by": "david leitch",
      "genre": "Action"
    }
  }
]</pre>

</details>

## live_multiple_362-134-7

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.582608 | 168 |
| Qwen3.8-27B | 正确 | 3.199463 | 111 |
| gemma-4-26B-A4B-it | 正确 | 0.42409 | 37 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Can you please find some Action movies for me, which are directed by Sujeeth Reddy and that are featuring Supreet Reddy?</pre>

### Official accepted answer

<pre>[
  {
    "Movies_3_FindMovies": {
      "directed_by": [
        "Sujeeth Reddy"
      ],
      "genre": [
        "Action"
      ],
      "cast": [
        "Supreet Reddy"
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
    "name": "Movies_3_FindMovies",
    "arguments": {
      "genre": "Action",
      "directed_by": "Sujeeth Reddy",
      "cast": "Supreet Reddy"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "genre": "Action",
      "directed_by": "Sujeeth Reddy",
      "cast": "Supreet Reddy"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "cast": "Supreet Reddy",
      "directed_by": "Sujeeth Reddy",
      "genre": "Action"
    }
  }
]</pre>

</details>

## live_multiple_363-134-8

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 3.366606 | 382 |
| Qwen3.8-27B | 正确 | 7.217304 | 277 |
| gemma-4-26B-A4B-it | 错误 | 0.690635 | 72 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I am interested in finding a movie that I can watch, and more specifically I am interested in movies where Zach Woods acts in? Also I want to find a movie which is directed by Thurop Van Orman.</pre>

### Official accepted answer

<pre>[
  {
    "Movies_3_FindMovies": {
      "directed_by": [
        "Thurop Van Orman"
      ],
      "genre": [
        "",
        "dontcare"
      ],
      "cast": [
        "Zach Woods"
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
    "name": "Movies_3_FindMovies",
    "arguments": {
      "cast": "Zach Woods",
      "directed_by": "Thurop Van Orman",
      "genre": "dontcare"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "cast": "Zach Woods",
      "directed_by": "Thurop Van Orman",
      "genre": "dontcare"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 错误</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "cast": "Zach Woods",
      "directed_by": "dontcare",
      "genre": "dontcare"
    }
  },
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "cast": "dontcare",
      "directed_by": "Thurop Van Orman",
      "genre": "dontcare"
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

## live_multiple_364-134-9

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.640929 | 175 |
| Qwen3.8-27B | 正确 | 3.664488 | 130 |
| gemma-4-26B-A4B-it | 正确 | 0.341344 | 27 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I feel like watching something light-hearted/funny. Find me a comedy movie that's directed by Wes Anderson?</pre>

### Official accepted answer

<pre>[
  {
    "Movies_3_FindMovies": {
      "directed_by": [
        "Wes Anderson"
      ],
      "genre": [
        "Comedy"
      ],
      "cast": [
        "",
        "dontcare"
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
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Wes Anderson",
      "genre": "Comedy",
      "cast": "dontcare"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Wes Anderson",
      "genre": "Comedy",
      "cast": "dontcare"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Wes Anderson",
      "genre": "Comedy"
    }
  }
]</pre>

</details>

## live_multiple_365-134-10

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.72199 | 185 |
| Qwen3.8-27B | 正确 | 3.415357 | 120 |
| gemma-4-26B-A4B-it | 正确 | 0.446515 | 41 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Hi, Find me a Comedy-drama movie that stars Josh Barclay Caras and is directed by Gene Stupnitsky?</pre>

### Official accepted answer

<pre>[
  {
    "Movies_3_FindMovies": {
      "directed_by": [
        "Gene Stupnitsky"
      ],
      "genre": [
        "Comedy-drama"
      ],
      "cast": [
        "Josh Barclay Caras"
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
    "name": "Movies_3_FindMovies",
    "arguments": {
      "genre": "Comedy-drama",
      "cast": "Josh Barclay Caras",
      "directed_by": "Gene Stupnitsky"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "cast": "Josh Barclay Caras",
      "directed_by": "Gene Stupnitsky",
      "genre": "Comedy-drama"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "cast": "Josh Barclay Caras",
      "directed_by": "Gene Stupnitsky",
      "genre": "Comedy-drama"
    }
  }
]</pre>

</details>

## live_multiple_366-134-11

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.239443 | 247 |
| Qwen3.8-27B | 正确 | 2.97046 | 101 |
| gemma-4-26B-A4B-it | 正确 | 0.346258 | 28 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find me a list of movies directed by Herbert Ross?</pre>

### Official accepted answer

<pre>[
  {
    "Movies_3_FindMovies": {
      "directed_by": [
        "Herbert Ross"
      ],
      "genre": [
        "",
        "dontcare"
      ],
      "cast": [
        "",
        "dontcare"
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
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Herbert Ross",
      "genre": "dontcare",
      "cast": "dontcare"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Herbert Ross",
      "genre": "dontcare",
      "cast": "dontcare"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Herbert Ross",
      "genre": "dontcare"
    }
  }
]</pre>

</details>

## live_multiple_367-134-12

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.050371 | 224 |
| Qwen3.8-27B | 正确 | 2.650079 | 89 |
| gemma-4-26B-A4B-it | 正确 | 0.269089 | 18 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I'm planning a movie night this weekend and want to watch something thrilling. Could you suggest an Action movie for us to enjoy?</pre>

### Official accepted answer

<pre>[
  {
    "Movies_3_FindMovies": {
      "directed_by": [
        "",
        "dontcare"
      ],
      "genre": [
        "Action"
      ],
      "cast": [
        "",
        "dontcare"
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
    "name": "Movies_3_FindMovies",
    "arguments": {
      "genre": "Action",
      "directed_by": "dontcare",
      "cast": "dontcare"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "genre": "Action",
      "directed_by": "dontcare",
      "cast": "dontcare"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "genre": "Action"
    }
  }
]</pre>

</details>

## live_multiple_368-134-13

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.574901 | 167 |
| Qwen3.8-27B | 正确 | 3.308763 | 114 |
| gemma-4-26B-A4B-it | 正确 | 0.419155 | 37 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I'm interested in a horror movie featuring Gwendoline Christie and directed by Peter Strickland. Can you find one for me?</pre>

### Official accepted answer

<pre>[
  {
    "Movies_3_FindMovies": {
      "directed_by": [
        "Peter Strickland"
      ],
      "genre": [
        "Horror"
      ],
      "cast": [
        "Gwendoline Christie"
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
    "name": "Movies_3_FindMovies",
    "arguments": {
      "genre": "Horror",
      "cast": "Gwendoline Christie",
      "directed_by": "Peter Strickland"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Peter Strickland",
      "genre": "Horror",
      "cast": "Gwendoline Christie"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "cast": "Gwendoline Christie",
      "directed_by": "Peter Strickland",
      "genre": "Horror"
    }
  }
]</pre>

</details>

## live_multiple_369-134-14

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.718107 | 184 |
| Qwen3.8-27B | 正确 | 3.04403 | 105 |
| gemma-4-26B-A4B-it | 正确 | 0.340088 | 27 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Could you search for Fantasy movies that were directed by Peter Jackson?</pre>

### Official accepted answer

<pre>[
  {
    "Movies_3_FindMovies": {
      "directed_by": [
        "Peter Jackson"
      ],
      "genre": [
        "Fantasy"
      ],
      "cast": [
        "",
        "dontcare"
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
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Peter Jackson",
      "genre": "Fantasy",
      "cast": "dontcare"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Peter Jackson",
      "genre": "Fantasy",
      "cast": "dontcare"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Peter Jackson",
      "genre": "Fantasy"
    }
  }
]</pre>

</details>

## live_multiple_370-134-15

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.518844 | 162 |
| Qwen3.8-27B | 正确 | 3.398796 | 119 |
| gemma-4-26B-A4B-it | 正确 | 0.416364 | 37 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I'm interested in fantasy movies with Danny John-Jules in the cast and directed by Jim Henson. Could you search for some options?</pre>

### Official accepted answer

<pre>[
  {
    "Movies_3_FindMovies": {
      "directed_by": [
        "Jim Henson"
      ],
      "genre": [
        "Fantasy"
      ],
      "cast": [
        "Danny John-Jules"
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
    "name": "Movies_3_FindMovies",
    "arguments": {
      "genre": "Fantasy",
      "cast": "Danny John-Jules",
      "directed_by": "Jim Henson"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Jim Henson",
      "genre": "Fantasy",
      "cast": "Danny John-Jules"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "cast": "Danny John-Jules",
      "directed_by": "Jim Henson",
      "genre": "Fantasy"
    }
  }
]</pre>

</details>

## live_multiple_371-134-16

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.619095 | 171 |
| Qwen3.8-27B | 正确 | 3.215779 | 112 |
| gemma-4-26B-A4B-it | 正确 | 0.415101 | 37 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Can you find me Drama movies that were directed by Gregory La Cava and include Franklin Pangborn in the cast?</pre>

### Official accepted answer

<pre>[
  {
    "Movies_3_FindMovies": {
      "directed_by": [
        "Gregory La Cava"
      ],
      "genre": [
        "Drama"
      ],
      "cast": [
        "Franklin Pangborn"
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
    "name": "Movies_3_FindMovies",
    "arguments": {
      "genre": "Drama",
      "directed_by": "Gregory La Cava",
      "cast": "Franklin Pangborn"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Gregory La Cava",
      "genre": "Drama",
      "cast": "Franklin Pangborn"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "cast": "Franklin Pangborn",
      "directed_by": "Gregory La Cava",
      "genre": "Drama"
    }
  }
]</pre>

</details>

## live_multiple_372-134-17

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.586562 | 169 |
| Qwen3.8-27B | 正确 | 3.315768 | 116 |
| gemma-4-26B-A4B-it | 正确 | 0.407444 | 36 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Search for a comedy movie with Fiona Reid in the lead role and directed by Joel Zwick?</pre>

### Official accepted answer

<pre>[
  {
    "Movies_3_FindMovies": {
      "directed_by": [
        "Joel Zwick"
      ],
      "genre": [
        "Comedy"
      ],
      "cast": [
        "Fiona Reid"
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
    "name": "Movies_3_FindMovies",
    "arguments": {
      "genre": "Comedy",
      "cast": "Fiona Reid",
      "directed_by": "Joel Zwick"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Joel Zwick",
      "genre": "Comedy",
      "cast": "Fiona Reid"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "cast": "Fiona Reid",
      "directed_by": "Joel Zwick",
      "genre": "Comedy"
    }
  }
]</pre>

</details>

## live_multiple_373-134-18

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.583086 | 168 |
| Qwen3.8-27B | 正确 | 2.93257 | 100 |
| gemma-4-26B-A4B-it | 正确 | 0.407345 | 36 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I'm looking to watch an Action movie with Sanjay Kapoor in the lead, directed by Jagan Shakti.</pre>

### Official accepted answer

<pre>[
  {
    "Movies_3_FindMovies": {
      "directed_by": [
        "Jagan Shakti"
      ],
      "genre": [
        "Action"
      ],
      "cast": [
        "Sanjay Kapoor"
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
    "name": "Movies_3_FindMovies",
    "arguments": {
      "genre": "Action",
      "cast": "Sanjay Kapoor",
      "directed_by": "Jagan Shakti"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Jagan Shakti",
      "genre": "Action",
      "cast": "Sanjay Kapoor"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "cast": "Sanjay Kapoor",
      "directed_by": "Jagan Shakti",
      "genre": "Action"
    }
  }
]</pre>

</details>

## live_multiple_374-134-19

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.530308 | 162 |
| Qwen3.8-27B | 正确 | 3.521461 | 124 |
| gemma-4-26B-A4B-it | 正确 | 0.433985 | 39 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Can you find me a movie that has Riley Stearns as the director and includes C.J. Rush in the cast?</pre>

### Official accepted answer

<pre>[
  {
    "Movies_3_FindMovies": {
      "directed_by": [
        "Riley Stearns"
      ],
      "genre": [
        "",
        "dontcare"
      ],
      "cast": [
        "C.J. Rush"
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
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Riley Stearns",
      "cast": "C.J. Rush",
      "genre": "dontcare"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Riley Stearns",
      "cast": "C.J. Rush",
      "genre": "dontcare"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "cast": "C.J. Rush",
      "directed_by": "Riley Stearns",
      "genre": "dontcare"
    }
  }
]</pre>

</details>

## live_multiple_375-134-20

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.835424 | 199 |
| Qwen3.8-27B | 正确 | 3.015585 | 104 |
| gemma-4-26B-A4B-it | 正确 | 0.360444 | 30 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find me movies that were directed by Sameh Zoabi?</pre>

### Official accepted answer

<pre>[
  {
    "Movies_3_FindMovies": {
      "directed_by": [
        "Sameh Zoabi"
      ],
      "genre": [
        "",
        "dontcare"
      ],
      "cast": [
        "",
        "dontcare"
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
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Sameh Zoabi",
      "genre": "dontcare",
      "cast": "dontcare"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Sameh Zoabi",
      "genre": "dontcare",
      "cast": "dontcare"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Movies_3_FindMovies",
    "arguments": {
      "directed_by": "Sameh Zoabi",
      "genre": "dontcare"
    }
  }
]</pre>

</details>

## live_multiple_376-135-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.383613 | 153 |
| Qwen3.8-27B | 正确 | 2.478474 | 90 |
| gemma-4-26B-A4B-it | 正确 | 0.284985 | 28 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Could you please help me find a psychologist in Santa Rosa please?</pre>

### Official accepted answer

<pre>[
  {
    "Services_4_FindProvider": {
      "city": [
        "Santa Rosa, CA"
      ],
      "type": [
        "Psychologist"
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
    "name": "Services_4_FindProvider",
    "arguments": {
      "city": "Santa Rosa, CA",
      "type": "Psychologist"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_4_FindProvider",
    "arguments": {
      "city": "Santa Rosa, CA",
      "type": "Psychologist"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_4_FindProvider",
    "arguments": {
      "city": "Santa Rosa, CA",
      "type": "Psychologist"
    }
  }
]</pre>

</details>

## live_multiple_377-135-1

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.457624 | 162 |
| Qwen3.8-27B | 正确 | 2.477384 | 90 |
| gemma-4-26B-A4B-it | 正确 | 0.277867 | 27 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I'm in Berkeley California and looking for a family counselor.</pre>

### Official accepted answer

<pre>[
  {
    "Services_4_FindProvider": {
      "city": [
        "Berkeley, CA"
      ],
      "type": [
        "Family Counselor"
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
    "name": "Services_4_FindProvider",
    "arguments": {
      "city": "Berkeley, CA",
      "type": "Family Counselor"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_4_FindProvider",
    "arguments": {
      "city": "Berkeley, CA",
      "type": "Family Counselor"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_4_FindProvider",
    "arguments": {
      "city": "Berkeley, CA",
      "type": "Family Counselor"
    }
  }
]</pre>

</details>

## live_multiple_378-135-2

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.526857 | 170 |
| Qwen3.8-27B | 正确 | 4.573822 | 177 |
| gemma-4-26B-A4B-it | 正确 | 0.285091 | 28 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I need help looking for a Family Therapist in Mountain View.</pre>

### Official accepted answer

<pre>[
  {
    "Services_4_FindProvider": {
      "city": [
        "Mountain View, CA"
      ],
      "type": [
        "Family Counselor"
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
    "name": "Services_4_FindProvider",
    "arguments": {
      "city": "Mountain View, CA",
      "type": "Family Counselor"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_4_FindProvider",
    "arguments": {
      "city": "Mountain View, CA",
      "type": "Family Counselor"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_4_FindProvider",
    "arguments": {
      "city": "Mountain View, CA",
      "type": "Family Counselor"
    }
  }
]</pre>

</details>

## live_multiple_379-136-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.57131 | 150 |
| Qwen3.8-27B | 正确 | 3.788485 | 120 |
| gemma-4-26B-A4B-it | 正确 | 0.438371 | 25 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: May I see the alarms that I have set? with user id 12345</pre>

### Official accepted answer

<pre>[
  {
    "Alarm_1_GetAlarms": {
      "user_id": [
        "12345"
      ],
      "include_disabled": [
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
    "name": "Alarm_1_GetAlarms",
    "arguments": {
      "user_id": "12345"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Alarm_1_GetAlarms",
    "arguments": {
      "user_id": "12345"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Alarm_1_GetAlarms",
    "arguments": {
      "user_id": "12345"
    }
  }
]</pre>

</details>

## live_multiple_380-136-1

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.841509 | 182 |
| Qwen3.8-27B | 正确 | 3.271165 | 100 |
| gemma-4-26B-A4B-it | 正确 | 0.439635 | 25 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I believe I have some notifications set. Can you please check for me? My user ID is 12345.</pre>

### Official accepted answer

<pre>[
  {
    "Alarm_1_GetAlarms": {
      "user_id": [
        "12345"
      ],
      "include_disabled": [
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
    "name": "Alarm_1_GetAlarms",
    "arguments": {
      "user_id": "12345"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Alarm_1_GetAlarms",
    "arguments": {
      "user_id": "12345"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Alarm_1_GetAlarms",
    "arguments": {
      "user_id": "12345"
    }
  }
]</pre>

</details>

## live_multiple_381-136-2

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.576253 | 150 |
| Qwen3.8-27B | 错误 | 8.733817 | 326 |
| gemma-4-26B-A4B-it | 正确 | 0.455846 | 27 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Can you check my schedule and tell me what alarms I have set for today? My user ID is U123456.</pre>

### Official accepted answer

<pre>[
  {
    "Alarm_1_GetAlarms": {
      "user_id": [
        "U123456"
      ],
      "include_disabled": [
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
    "name": "Alarm_1_GetAlarms",
    "arguments": {
      "user_id": "U123456"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 错误</summary>

### Model output

<pre>[
  {
    "name": "Alarm_1_GetAlarms",
    "arguments": {
      "user_id": "U123456",
      "include_disabled": true
    }
  }
]</pre>

### Official diagnostic

<pre>[
  "Invalid value for parameter 'include_disabled': True. Expected one of ['', False]."
]</pre>

### Provisional error group

<pre>参数／调用数量不匹配</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Alarm_1_GetAlarms",
    "arguments": {
      "user_id": "U123456"
    }
  }
]</pre>

</details>

## live_multiple_382-137-0

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.508462 | 278 |
| Qwen3.8-27B | 正确 | 2.924421 | 99 |
| gemma-4-26B-A4B-it | 正确 | 0.3616 | 29 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find me a hair stylist in Fremont, CA, and it shouldn't be unisex?</pre>

### Official accepted answer

<pre>[
  {
    "Services_1_FindProvider": {
      "city": [
        "Fremont, CA"
      ],
      "is_unisex": [
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
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "Fremont, CA",
      "is_unisex": false
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "Fremont, CA",
      "is_unisex": false
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "Fremont, CA",
      "is_unisex": false
    }
  }
]</pre>

</details>

## live_multiple_383-137-1

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.661143 | 179 |
| Qwen3.8-27B | 正确 | 2.734603 | 93 |
| gemma-4-26B-A4B-it | 正确 | 0.351801 | 28 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: see a hair stylist. I want to get my hair done in New York, locate a unisex salon?</pre>

### Official accepted answer

<pre>[
  {
    "Services_1_FindProvider": {
      "city": [
        "New York, NY"
      ],
      "is_unisex": [
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
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "New York, NY",
      "is_unisex": true
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "New York, NY",
      "is_unisex": true
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "New York, NY",
      "is_unisex": true
    }
  }
]</pre>

</details>

## live_multiple_384-137-2

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.128562 | 230 |
| Qwen3.8-27B | 正确 | 3.087022 | 106 |
| gemma-4-26B-A4B-it | 正确 | 0.35019 | 28 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I would like to find a Unisex Salon in San Jose</pre>

### Official accepted answer

<pre>[
  {
    "Services_1_FindProvider": {
      "city": [
        "San Jose, CA"
      ],
      "is_unisex": [
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
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "San Jose, CA",
      "is_unisex": true
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "San Jose, CA",
      "is_unisex": true
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "San Jose, CA",
      "is_unisex": true
    }
  }
]</pre>

</details>

## live_multiple_385-137-3

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.707232 | 183 |
| Qwen3.8-27B | 正确 | 3.653091 | 130 |
| gemma-4-26B-A4B-it | 正确 | 0.34313 | 27 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Find a salon in Campbell and preferably one that services both men and women?</pre>

### Official accepted answer

<pre>[
  {
    "Services_1_FindProvider": {
      "city": [
        "Campbell, CA"
      ],
      "is_unisex": [
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
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "Campbell, CA",
      "is_unisex": true
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "Campbell, CA",
      "is_unisex": true
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "Campbell, CA",
      "is_unisex": true
    }
  }
]</pre>

</details>

## live_multiple_386-137-4

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.255617 | 250 |
| Qwen3.8-27B | 正确 | 2.638448 | 89 |
| gemma-4-26B-A4B-it | 正确 | 0.298462 | 21 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I need to get my hair done. Please find a salon in San Francisco.</pre>

### Official accepted answer

<pre>[
  {
    "Services_1_FindProvider": {
      "city": [
        "San Francisco, CA"
      ],
      "is_unisex": [
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
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "San Francisco, CA"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "San Francisco, CA"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "San Francisco, CA"
    }
  }
]</pre>

</details>

## live_multiple_387-137-5

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 1.67087 | 176 |
| Qwen3.8-27B | 正确 | 3.02084 | 104 |
| gemma-4-26B-A4B-it | 正确 | 0.359191 | 28 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: I'm in New York, and I need to find a hair stylist for a quick trim. Can you look up a place that does both men's and women's haircuts?</pre>

### Official accepted answer

<pre>[
  {
    "Services_1_FindProvider": {
      "city": [
        "New York, NY"
      ],
      "is_unisex": [
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
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "New York, NY",
      "is_unisex": true
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "New York, NY",
      "is_unisex": true
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "New York, NY",
      "is_unisex": true
    }
  }
]</pre>

</details>

## live_multiple_388-137-6

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.204525 | 242 |
| Qwen3.8-27B | 正确 | 3.221786 | 112 |
| gemma-4-26B-A4B-it | 正确 | 0.296813 | 21 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: Can you find me a nice salon in Alameda?</pre>

### Official accepted answer

<pre>[
  {
    "Services_1_FindProvider": {
      "city": [
        "Alameda, CA"
      ],
      "is_unisex": [
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
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "Alameda, CA"
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "Alameda, CA"
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "Alameda, CA"
    }
  }
]</pre>

</details>

## live_multiple_389-137-7

| Model | Official verdict | Latency (s) | Output tokens |
|---|---|---:|---:|
| Qwen3.5-9B | 正确 | 2.491591 | 277 |
| Qwen3.8-27B | 正确 | 2.734892 | 92 |
| gemma-4-26B-A4B-it | 正确 | 0.364371 | 29 |

<details>
<summary>Question and accepted answer</summary>

### Question

<pre>user: My friend told me about an unisex salon and now I am interested in going to one. Will you find a unisex salon in Corte Madera.</pre>

### Official accepted answer

<pre>[
  {
    "Services_1_FindProvider": {
      "city": [
        "Corte Madera, CA"
      ],
      "is_unisex": [
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
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "Corte Madera, CA",
      "is_unisex": true
    }
  }
]</pre>

</details>

<details>
<summary>Qwen/Qwen3.8-27B — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "Corte Madera, CA",
      "is_unisex": true
    }
  }
]</pre>

</details>

<details>
<summary>google/gemma-4-26B-A4B-it — 正确</summary>

### Model output

<pre>[
  {
    "name": "Services_1_FindProvider",
    "arguments": {
      "city": "Corte Madera, CA",
      "is_unisex": true
    }
  }
]</pre>

</details>


[Category index](README.md) · [All categories](../README.md) · [Previous](page-012.md) · [Next](page-014.md)
