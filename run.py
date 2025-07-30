from llama_cpp import Llama

def main():
    model_path = "llama-3.2-3b-instruct-q4_k_m.gguf"

    llm = Llama(
        model_path=model_path,
        n_threads=4
    )

    prompt = "Seja objetivo e responda apenas o que for dito/perguntado.\nPergunta: Quais as desvantagens do scrum?"

    response = llm.create_completion(
        prompt=prompt,
        suffix="\n\n",
        max_tokens=None,
        temperature=0.7,
        top_p=0.9,
        stream=True,
    )

    print(f"\n=== Resposta ===\n")
    for res in response:
        print(res["choices"][0]["text"], end="", flush=True)


if __name__ == "__main__":
    main()
