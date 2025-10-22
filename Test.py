import lmstudio as lms

with lms.Client() as client:
    model = client.llm.model("qwen/qwen3-8b")
    result = model.complete("The quick brown fox ", config={"maxTokens": 10})
    print(result)

