import requests

api_key="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"

def img_gen(prompt,output_file):
    API_URL="{Your huuging face IMage_gen model API}"
    headers={"Authorization": f"Bearer {api_key}"}

    def query(payload):
        response = requests.post(API_URL,headers=headers,json=payload)
        return response.content
    image_bytes=query({
        "inputs":prompt,
    })
    with open(output_file,'wb') as f:
        f.write(image_bytes)
        
if __name__=="__main__":
    img_gen("A super sport bike","bike.jpg")