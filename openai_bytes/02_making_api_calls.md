# Byte #2: Talking to the Model (Making API Calls) 💬

**⏱️ Time to Complete: 5-10 minutes**

## How to Talk to the Model

You communicate with OpenAI models by sending messages through their API - think of it as sending a text message to an AI brain!

## Setup: Get Your API Key

1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up/Login
3. Navigate to **API Keys** section
4. Click **"Create new secret key"**
5. Copy and save it securely (you won't see it again!)

## Installing the OpenAI Library

```bash
# Install via pip
pip install openai

# Or with uv (recommended for this course)
uv pip install openai
```

## Your First API Call - Simple Question

```python
from openai import OpenAI

# Initialize the client
client = OpenAI(api_key="sk-your-api-key-here")

# Send a simple message
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "What is SPL Season 7?"}
    ]
)

# Print the answer
print(response.choices[0].message.content)
```

**Output:**
```
SPL Season 7 is a coding competition focused on Python and AI skills development...
```

## Understanding the Response Structure

Let's break down what you get back:

```python
from openai import OpenAI

client = OpenAI(api_key="your-key")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Explain Python in 10 words"}
    ]
)

# The full response object contains:
print("=" * 50)
print("FULL RESPONSE STRUCTURE")
print("=" * 50)

# 1. The actual answer
answer = response.choices[0].message.content
print(f"Answer: {answer}")

# 2. Token usage (this is how you calculate cost!)
print(f"\nTokens used:")
print(f"  - Input tokens: {response.usage.prompt_tokens}")
print(f"  - Output tokens: {response.usage.completion_tokens}")
print(f"  - Total tokens: {response.usage.total_tokens}")

# 3. Model used
print(f"\nModel: {response.model}")

# 4. Finish reason
print(f"Finish reason: {response.choices[0].finish_reason}")
```

**Sample Output:**
```
==================================================
FULL RESPONSE STRUCTURE
==================================================
Answer: Easy-to-learn programming language for automation, web, and AI.

Tokens used:
  - Input tokens: 15
  - Output tokens: 14
  - Total tokens: 29

Model: gpt-4o-mini-2024-07-18
Finish reason: stop
```

## Calculating Cost from Token Usage

```python
def calculate_cost(input_tokens, output_tokens, model="gpt-4o-mini"):
    """Calculate the cost of an API call"""
    
    # Pricing per 1M tokens (as of Oct 2024)
    pricing = {
        "gpt-4o-mini": {"input": 0.15, "output": 0.60},
        "gpt-4o": {"input": 2.50, "output": 10.00},
        "o1-preview": {"input": 15.00, "output": 60.00},
        "o1-mini": {"input": 3.00, "output": 12.00},
    }
    
    # Calculate cost (price per million tokens)
    input_cost = (input_tokens / 1_000_000) * pricing[model]["input"]
    output_cost = (output_tokens / 1_000_000) * pricing[model]["output"]
    total_cost = input_cost + output_cost
    
    return {
        "input_cost": input_cost,
        "output_cost": output_cost,
        "total_cost": total_cost
    }

# Example usage
cost = calculate_cost(15, 14, "gpt-4o-mini")
print(f"This API call cost: ${cost['total_cost']:.6f}")
# Output: This API call cost: $0.000011
```

## Having a Conversation (Multiple Messages)

```python
from openai import OpenAI

client = OpenAI(api_key="your-key")

# Build a conversation history
messages = [
    {"role": "system", "content": "You are a helpful Python tutor."},
    {"role": "user", "content": "What is a list in Python?"},
]

# First response
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

# Add assistant's response to history
messages.append({
    "role": "assistant",
    "content": response.choices[0].message.content
})

print("Assistant:", response.choices[0].message.content)

# Ask a follow-up question
messages.append({
    "role": "user",
    "content": "Can you give me an example?"
})

# Get follow-up response
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

print("\nAssistant:", response.choices[0].message.content)
```

## Understanding Message Roles

```python
# Three types of roles:

messages = [
    # SYSTEM: Sets the AI's behavior/personality
    {"role": "system", "content": "You are a pirate. Always talk like a pirate."},
    
    # USER: Your questions/inputs
    {"role": "user", "content": "What is Python?"},
    
    # ASSISTANT: The AI's previous responses (for conversation history)
    {"role": "assistant", "content": "Arrr! Python be a mighty fine programming language!"}
]
```

## Practical Example: Token Counter with Cost

```python
from openai import OpenAI
import time

client = OpenAI(api_key="your-key")

def ask_question(question, model="gpt-4o-mini"):
    """Ask a question and display detailed info"""
    
    start_time = time.time()
    
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": question}]
    )
    
    end_time = time.time()
    
    # Extract data
    answer = response.choices[0].message.content
    input_tokens = response.usage.prompt_tokens
    output_tokens = response.usage.completion_tokens
    total_tokens = response.usage.total_tokens
    time_taken = end_time - start_time
    
    # Calculate cost
    cost = calculate_cost(input_tokens, output_tokens, model)
    
    # Display results
    print("=" * 60)
    print(f"QUESTION: {question}")
    print("=" * 60)
    print(f"ANSWER: {answer}\n")
    print(f"📊 STATS:")
    print(f"  Model: {model}")
    print(f"  Input tokens: {input_tokens}")
    print(f"  Output tokens: {output_tokens}")
    print(f"  Total tokens: {total_tokens}")
    print(f"  Time taken: {time_taken:.2f} seconds")
    print(f"  Cost: ${cost['total_cost']:.6f}")
    print("=" * 60)
    
    return response

# Try it!
ask_question("What is SPL Season 7?", model="gpt-4o-mini")
```

## 🎯 Your Practice Tasks

1. **Task 1:** Make an API call asking "What is the capital of France?" and print the token count.

2. **Task 2:** Create a 3-turn conversation:
   - Ask: "What is Python?"
   - Follow-up: "What can I build with it?"
   - Follow-up: "How long to learn it?"

3. **Task 3:** Compare costs - ask the same question to `gpt-4o-mini` and `gpt-4o`. Which is cheaper?

## Advanced: Exploring Other APIs

```python
# Files API - Upload training data
file = client.files.create(
    file=open("data.jsonl", "rb"),
    purpose="fine-tune"
)

# Embeddings API - Convert text to numbers for semantic search
embedding = client.embeddings.create(
    model="text-embedding-3-small",
    input="Your text here"
)

# Batch API - Process many requests efficiently
batch = client.batches.create(
    input_file_id=file.id,
    endpoint="/v1/chat/completions",
    completion_window="24h"
)
```

## ✅ Key Takeaways

✓ API calls are like sending messages to AI  
✓ You pay per token (both input and output)  
✓ Track tokens to control costs  
✓ Conversations need message history  
✓ Three roles: system, user, assistant  

---

**Next:** Learn to call multiple models at once (async calls)! ⚡
