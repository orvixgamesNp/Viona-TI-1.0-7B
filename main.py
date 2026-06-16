from transformers import pipeline

MODEL_ID = "orvixgamesai/Viona-TI-1.0-7B"

pipe = pipeline(
    "text-generation",
    model=MODEL_ID,
    device_map="auto"
)

while True:
    prompt = input("You: ")
    if prompt.lower() in ["exit", "quit"]:
        break

    result = pipe(
        prompt,
        max_new_tokens=256,
        temperature=0.7,
        do_sample=True
    )

    print("\nViona:", result[0]["generated_text"])
    print()
