from llama_cpp import Llama

def main():
    model_path = "llama-3.2-3b-instruct-q4_k_m.gguf"

    llm = Llama(
        model_path=model_path,
        n_threads=4
    )

    prompt = "Quem descobriu o Brasil e em qual ano?"

    response = llm.create_completion(
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        top_p=0.9
    )

    text = response["choices"][0]["text"].strip()
    print(f"\n=== Resposta ===\n{text}\n")

if __name__ == "__main__":
    main()
