from notion.client import NotionClient

# login
token_v2 = ""
client = NotionClient(token_v2=token_v2)

# connect page
url = ""
page = client.get_block(url)

# add block
page.children.add_new("header", title="오늘 할일")
page.children.add_new("to_do", title="8시 홈플러스")
page.children.add_new("to_do", title="9시 운동")

print("blocks added!")
