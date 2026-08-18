from transformers import AutoTokenizer, AutoModelForCausalLM

# Mend AI-BOM will detect this model loading
model_id = "google/gemma-2b"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

print("Loading Gemma model for AI demo...")
