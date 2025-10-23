import lmstudio as lms

print("The capitol of the US state containing Tampa is ... Tallahassee, Florida.\nhe capital city of Florida is Tallahassee. So the answer")
print()

with lms.Client() as client:
    model = client.llm.model("qwen/qwen3-8b")
    prompt = "The capitol of the US state containing Tampa is "
    result = model.complete(prompt, config={"maxTokens": 20})
    print(f"{prompt}...{result.content}")
    print()
