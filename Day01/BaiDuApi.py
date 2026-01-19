from openai import OpenAI
from pyexpat.errors import messages

client = OpenAI(
    base_url='https://qianfan.baidubce.com/v2',
    api_key='bce-v3/ALTAK-5a18Osp4VawqBfoYarFPR/840ed49abec94804d5113011721b9d93eea8f772'
)

response = client.chat.completions.create(
    model="ernie-4.5-turbo-128k",
    messages=[
        {
            "role": "user",
            "content": "什麽是IP定位？"},
        {
            "role": "assistant",
            "content": "我可以完成多种任务，包括但不限于知识问答（涵盖学科专业知识、百科知识、生活常识等）、文本创作（如小说、文案、诗歌、作文的创作）、知识推理（例如逻辑推理、脑筋急转弯等）。除此之外，我也可以陪你聊天、分享笑话、讲故事等。如果你有任何需求，都可以问我哦。“\n"
        }
    ],
    max_tokens=100,
    temperature=0.5,
    top_p=1,
    extra_body={
        "penalty_score": 1,
        "stop": [],
        "web_search": {
            "enable": False,
            "enable_trace": False
        }
    }
)
print(response)

