import json

def extract_text_from_json(input_path, output_path='output.txt'):
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    messages = data.get('messages', [])
    
    with open(output_path, 'w', encoding='utf-8') as out:
        for msg in messages:
            if msg.get('type') == 'message':
                text = msg.get('text', '')
                if isinstance(text, str):
                    plain_text = text
                elif isinstance(text, list):
                    plain_text = ''
                    for item in text:
                        if isinstance(item, dict):
                            plain_text += item.get('text', '')
                        elif isinstance(item, str):
                            plain_text += item
                else:
                    plain_text = ''
                
                if plain_text.strip():
                    out.write(f"{msg['id']}: {plain_text}\n")

extract_text_from_json('result.json')