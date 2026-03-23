import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove HTML section 
content = re.sub(r'\s*<!-- ============ CHART SECTION ============ -->.*?(?=<!-- ============ COMO FUNCIONA ============ -->)', '\n\n    ', content, flags=re.DOTALL)

# Remove JS section
content = re.sub(r'\s*// ---- Charts ----.*?(?=// ---- Smooth scroll ----)', '\n\n        ', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
