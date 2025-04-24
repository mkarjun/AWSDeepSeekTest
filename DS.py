import boto3
import json
session = boto3.Session(profile_name="arjun-sso")
bedrock = session.client("bedrock-runtime", region_name="us-east-1")

payload = {
    "prompt": "Explain the architecture of the Transformer model and MAMBA SSM in simple terms with examples.",
    "max_tokens": 512,
    "temperature": 0.5,
    "top_p": 0.9
}
response = bedrock.invoke_model(
    modelId="us.deepseek.r1-v1:0",
    contentType="application/json",
    accept="application/json",
    body=json.dumps(payload)
)
response_body = json.loads(response['body'].read())
print(json.dumps(response_body, indent=2))
