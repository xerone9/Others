data = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
length_limit = 72
max_limit = 500

count = 0
full_count = 0
text_with_line_break = ""
for index, value in enumerate(data):
    if count == 0 and value == " ":
        count += 1
        full_count += 1
    else:
        text_with_line_break += value
        count += 1
        full_count += 1
        try:
            if count == length_limit:
                if data[index + 1] == " ":
                    text_with_line_break += "\n"
                    count = 0
                else:
                    if value == " ":
                        text_with_line_break += "\n"
                        count = 0
                    elif data[index + 2] == " ":
                        count -= 1
                    else:
                        text_with_line_break += "-\n"
                        count = 0
            if full_count == max_limit:
                break
        except IndexError:
            break

print(text_with_line_break)