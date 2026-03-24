import os
import re

articles_dir = '/root/.openclaw/workspace/blog_domotique/site/articles/'

def process_file(file_path):
    if not file_path.endswith('.md'):
        return
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def replacer(match):
        full = match.group(0)
        start = match.start()
        end = match.end()
        
        pre = content[start-2:start] if start >= 2 else ""
        post = content[end:end+2] if end <= len(content) - 2 else ""
        
        if pre == '**' and post == '**':
            return full # Already bolded
        elif pre == '**':
            return full + '**' # Fix broken bolding (only ** at start)
        elif post == '**':
            return '**' + full # Fix broken bolding (only ** at end)
        else:
            return f'**{full}**'

    # Matches standard markdown links [text](url)
    new_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replacer, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {os.path.basename(file_path)}")

for filename in os.listdir(articles_dir):
    process_file(os.path.join(articles_dir, filename))
print("Done processing articles.")
