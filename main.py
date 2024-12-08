import json
from docx import Document

def extract_questions_and_answers(file_path):
    doc = Document(file_path)
    data = []
    
    # Har bir jadvalni tahlil qilish
    for table in doc.tables:
        # Jadvalning birinchi satrini o'tkazib yuboramiz (sarlavha qatori)
         for index, row in enumerate(table.rows[1:], start=1):
            question = row.cells[1].text.strip("- ")  # "SAVOLLAR" ustuni
            answer = row.cells[2].text.strip("- ")    # "A" ustuni
            
            option1 = row.cells[2].text.strip("- ")    # "A" ustuni
            option2 = row.cells[3].text.strip("- ")    # "A" ustuni
            option3 = row.cells[4].text.strip("- ")    # "A" ustuni
            option4 = row.cells[5].text.strip("- ")    # "A" ustuni
            
            # Faqat savol va javob mavjud bo‘lsa, JSON formatga qo‘shish
            if question and answer:
                data.append({
                    "id": index,
                    "question": question,
                    "options": [
                        option1,
                        option2,
                        option3,
                        option4
                    ],
                    "answer": answer
                })
    
    return data

file_path = r"C:\Users\acer\Desktop\1.docx"  # Word fayl yo‘li
# file_path = r"C:\Users\acer\Desktop\1.docx"  # Word fayl yo‘li
json_data = extract_questions_and_answers(file_path)

# JSON faylni saqlash
output_path = "1.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

print(f"JSON fayl yaratildi: {output_path}")
