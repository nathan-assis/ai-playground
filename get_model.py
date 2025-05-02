from llama_cpp import Llama

llm = Llama.from_pretrained(
	repo_id="nathan-assis/Llama-3.2-3B-Instruct-Q4_K_M-GGUF",
	filename="llama-3.2-3b-instruct-q4_k_m.gguf",
    local_dir=""
)
