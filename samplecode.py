def justify_paragraph(paragraph, page_width):
    words = paragraph.split()
    lines = []
    current_line = ''
    
    for word in words:
        if len(current_line) + len(word) <= page_width:
            if current_line:
                current_line += ' '
            current_line += word
        else:
            lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)
    
    return lines

# Sample input string
paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
page_width = 20
justified_paragraph = justify_paragraph(paragraph, page_width)
for i, line in enumerate(justified_paragraph, 1):
    print(f"Array[{i}] = \"{line}\"")
