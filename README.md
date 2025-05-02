## llama.cpp
`llama.cpp` é uma biblioteca em C/C++ open-source para inferência de grandes modelos de linguagem (LLMs) localmente, sem dependências pesadas e com foco em desempenho mesmo em hardware modesto.

### Dependências
- Python 3.8+
- Compilador C
    - Linux: gcc or clang
    - Windows: Visual Studio or MinGW
    - MacOS: Xcode

### Por quê usar o `llama.cpp`?
O objetivo desse projeto é criar um RAG leve e de fácil utilização, para isso o llama.cpp oferece fácil distribuição dos modelos utilizando o formato [**GGUF**](https://github.com/ggml-org/ggml/blob/master/docs/gguf.md). Além disso, com o llama.cpp é fácil fazer a [quantização](https://huggingface.co/docs/optimum/en/concept_guides/quantization) dos modelos através do script [`convert_hf_to_gguf.py`](https://github.com/ggml-org/llama.cpp/blob/master/convert_hf_to_gguf.py).

### Como usar
Como eu fiz para rodar um LLM no meu computador(CPU-only):

1. Instalei o binding python do llama.cpp:
<pre><code>pip install llama-cpp-python</code></pre>

2. Usei o `huggingface-hub` para baixar o modelo já quantizado no format GGUF:

Primeiro, instalar o `huggingface-hub`:
<pre><code>pip install huggingface-hub</code></pre>

Depois, criei um script Python para baixar o modelo do `repo_id` que possui o seguinte `filename`:
<pre>
<code>
python from llama_cpp import Llama

llm = Llama.from_pretrained( 
    repo_id="nathan-assis/Llama-3.2-3B-Instruct-Q4_K_M-GGUF",
    filename="llama-3.2-3b-instruct-q4_k_m.gguf"
)
</code>
</pre>

3. Com o modelo baixado, criei um script para testá-lo:
<pre>
<code>
from llama_cpp import Llama

llm = Llama(
    model_path="llama-3.2-3B-Instruct-Q4_K_M.gguf",
    n_threads=4
)
print(llm("Quem descobriu o Brasil?"))
</code>
</pre>
