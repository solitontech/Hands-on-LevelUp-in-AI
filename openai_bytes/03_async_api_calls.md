# Byte #3: Calling Models Asynchronously (Fast Calls) ⚡

**⏱️ Time to Complete: 5-10 minutes**

## What is Asynchronous Programming?

Imagine you're at a restaurant:

**🐌 Synchronous (Normal way):**
- Order food → Wait → Eat
- Order dessert → Wait → Eat
- Order coffee → Wait → Drink
- **Total time:** 45 minutes (15 min each)

**⚡ Asynchronous (Smart way):**
- Order food, dessert, AND coffee all at once
- Kitchen makes them in parallel
- You get everything together
- **Total time:** 15 minutes!

## Why Use Async with OpenAI?

When you need to:
- Ask multiple models the same question (compare responses)
- Process many questions at once
- Call different APIs simultaneously
- Save time when making multiple API calls

## The Performance Difference

```python
# Synchronous: One at a time (SLOW)
# Call Model 1 → Wait 2 seconds
# Call Model 2 → Wait 2 seconds
# Call Model 3 → Wait 2 seconds
# Total: 6 seconds

# Asynchronous: All at once (FAST)
# Call all 3 models together
# Wait 2 seconds (they run in parallel)
# Total: 2 seconds ✨
```

## Setup: Install Async OpenAI

```bash
# The OpenAI library already supports async!
pip install openai asyncio
```

## Basic Async Example: Single Call

```python
import asyncio
from openai import AsyncOpenAI

async def ask_ai(question):
    """Ask a question asynchronously"""
    client = AsyncOpenAI(api_key="your-key")
    
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}]
    )
    
    return response.choices[0].message.content

# Run the async function
async def main():
    answer = await ask_ai("What is Python?")
    print(answer)

# Execute
asyncio.run(main())
```

**Key Differences from Sync:**
1. Use `AsyncOpenAI` instead of `OpenAI`
2. Functions are defined with `async def`
3. Use `await` before async operations
4. Run with `asyncio.run()`

## Calling Multiple Models at Once

```python
import asyncio
from openai import AsyncOpenAI
import time

async def ask_model(client, model, question):
    """Ask one model a question"""
    start = time.time()
    
    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": question}]
    )
    
    duration = time.time() - start
    
    return {
        "model": model,
        "answer": response.choices[0].message.content,
        "tokens": response.usage.total_tokens,
        "time": duration
    }

async def compare_models(question):
    """Ask the same question to multiple models simultaneously"""
    client = AsyncOpenAI(api_key="your-key")
    
    # List of models to compare
    models = ["gpt-4o-mini", "gpt-4o"]
    
    # Create tasks for all models
    tasks = [ask_model(client, model, question) for model in models]
    
    # Run all tasks in parallel
    results = await asyncio.gather(*tasks)
    
    return results

# Run it
async def main():
    print("Asking multiple models the same question...\n")
    
    results = await compare_models("Explain async programming in one sentence")
    
    for result in results:
        print(f"Model: {result['model']}")
        print(f"Answer: {result['answer']}")
        print(f"Tokens: {result['tokens']}")
        print(f"Time: {result['time']:.2f}s")
        print("-" * 60)

asyncio.run(main())
```

**Sample Output:**
```
Asking multiple models the same question...

Model: gpt-4o-mini
Answer: Async programming allows multiple tasks to run concurrently without blocking execution.
Tokens: 28
Time: 1.23s
------------------------------------------------------------
Model: gpt-4o
Answer: Asynchronous programming enables tasks to execute independently, improving efficiency by not waiting for each to complete sequentially.
Tokens: 32
Time: 1.45s
------------------------------------------------------------
```

## Speed Comparison: Sync vs Async

```python
import asyncio
from openai import OpenAI, AsyncOpenAI
import time

# SYNCHRONOUS VERSION (Slow)
def sync_multiple_calls():
    """Make 5 calls one at a time"""
    client = OpenAI(api_key="your-key")
    
    start = time.time()
    
    questions = [
        "What is Python?",
        "What is JavaScript?",
        "What is Go?",
        "What is Rust?",
        "What is Java?"
    ]
    
    results = []
    for question in questions:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": question}]
        )
        results.append(response.choices[0].message.content)
    
    duration = time.time() - start
    print(f"⏱️  Synchronous: {duration:.2f} seconds")
    return results

# ASYNCHRONOUS VERSION (Fast)
async def async_multiple_calls():
    """Make 5 calls all at once"""
    client = AsyncOpenAI(api_key="your-key")
    
    start = time.time()
    
    questions = [
        "What is Python?",
        "What is JavaScript?",
        "What is Go?",
        "What is Rust?",
        "What is Java?"
    ]
    
    async def ask(question):
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": question}]
        )
        return response.choices[0].message.content
    
    # Create all tasks
    tasks = [ask(q) for q in questions]
    
    # Run all in parallel
    results = await asyncio.gather(*tasks)
    
    duration = time.time() - start
    print(f"⚡ Asynchronous: {duration:.2f} seconds")
    return results

# Compare them
print("Making 5 API calls...\n")
sync_multiple_calls()
asyncio.run(async_multiple_calls())
```

**Expected Output:**
```
Making 5 API calls...

⏱️  Synchronous: 8.45 seconds
⚡ Asynchronous: 2.13 seconds
```

**🎉 4x faster with async!**

## Practical Example: Batch Question Processor

```python
import asyncio
from openai import AsyncOpenAI

async def process_questions_batch(questions, model="gpt-4o-mini"):
    """Process multiple questions efficiently"""
    client = AsyncOpenAI(api_key="your-key")
    
    async def get_answer(question):
        response = await client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": question}]
        )
        return {
            "question": question,
            "answer": response.choices[0].message.content,
            "tokens": response.usage.total_tokens
        }
    
    # Process all questions in parallel
    tasks = [get_answer(q) for q in questions]
    results = await asyncio.gather(*tasks)
    
    return results

# Example usage
async def main():
    questions = [
        "What is machine learning?",
        "What is deep learning?",
        "What is neural network?",
        "What is GPT?",
        "What is transformer architecture?"
    ]
    
    print(f"Processing {len(questions)} questions...\n")
    
    results = await process_questions_batch(questions)
    
    total_tokens = 0
    for i, result in enumerate(results, 1):
        print(f"{i}. Q: {result['question']}")
        print(f"   A: {result['answer'][:80]}...")
        print(f"   Tokens: {result['tokens']}")
        total_tokens += result['tokens']
        print()
    
    print(f"📊 Total tokens used: {total_tokens}")

asyncio.run(main())
```

## Advanced: Error Handling in Async

```python
import asyncio
from openai import AsyncOpenAI

async def safe_api_call(client, question, model="gpt-4o-mini"):
    """API call with error handling"""
    try:
        response = await client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": question}]
        )
        return {
            "success": True,
            "answer": response.choices[0].message.content
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

async def main():
    client = AsyncOpenAI(api_key="your-key")
    
    questions = [
        "What is Python?",
        "What is AI?",
        "What is blockchain?"
    ]
    
    tasks = [safe_api_call(client, q) for q in questions]
    results = await asyncio.gather(*tasks)
    
    for i, result in enumerate(results):
        if result["success"]:
            print(f"✅ Question {i+1}: {result['answer'][:50]}...")
        else:
            print(f"❌ Question {i+1}: Error - {result['error']}")

asyncio.run(main())
```

## When to Use Async vs Sync

| Scenario | Use This | Why |
|----------|----------|-----|
| Single API call | Sync | Simpler code |
| Multiple API calls | Async | Much faster |
| Real-time chatbot | Sync | Sequential conversation |
| Batch processing | Async | Process many at once |
| Comparing models | Async | Get all responses together |
| Simple script | Sync | Easier to understand |

## 🎯 Your Practice Tasks

1. **Task 1:** Create an async function that asks 3 different models the same question and compares their response times.

2. **Task 2:** Process this list of questions asynchronously:
   ```python
   questions = [
       "Define recursion",
       "What is a REST API?",
       "Explain Python decorators",
       "What is async/await?"
   ]
   ```

3. **Task 3:** Time the difference - run 10 API calls synchronously, then asynchronously. Calculate the speedup.

## ✅ Key Takeaways

✓ Async = running multiple tasks in parallel  
✓ Use `AsyncOpenAI` for async calls  
✓ Use `await` for async operations  
✓ Use `asyncio.gather()` to run multiple tasks together  
✓ Async is 3-5x faster for multiple calls  
✓ Perfect for batch processing and model comparison  

---

**🎉 Congratulations!** You now know how to efficiently work with OpenAI models!

## Quick Reference Cheat Sheet

```python
# Sync (simple, one at a time)
from openai import OpenAI
client = OpenAI(api_key="key")
response = client.chat.completions.create(...)

# Async (fast, many at once)
from openai import AsyncOpenAI
import asyncio

async def main():
    client = AsyncOpenAI(api_key="key")
    response = await client.chat.completions.create(...)
    
asyncio.run(main())
```
