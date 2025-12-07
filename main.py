from transformers import pipeline
import torch   # corrected spelling

# Create the generator
generator = pipeline("text-generation", model="distilgpt2")

# Generate text
result = generator(
    "AI is the future because",
    max_length=50,
    num_return_sequences=1
)

# Print output
print(result[0]["generated_text"])

