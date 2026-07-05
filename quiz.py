def Answer(y):
    global total
    print(questions[y]["question"])
    print(questions[y]["choices"])
    x = input("ตอบ")
    if x == questions[y]["answer"]:
        print("ถูกต้อง")
        total += 1
    else:
            print("ไม่ถูกต้อง")
try:
    total = 0
    questions = [
    {
        "question": "5+7=?",
        "choices": ["A. 12",
        "B. 4",
        "C. 45",
        "D. 21"],
        "answer": "A"
    },
    {
        "question": "ถ้าวัตถุมีขนาดเล็กจนแสงไม่กระทบจะเกิดอะไรขึ้น",
        "choices": ["A. ทะลุสิ่งของได้", "B. วาปได้", "C. เร็วกว่าแสงได้", "D. ถูกทุกข้อ"],
        "answer": "A"
    },
    {
        "question": "Ar มีการจัดเรียงอิเล็กตรอนยังไง",
        "choices": ["A. 1s2 2s2 2p6 3s2 3p6", "B. 2,8,6", "C. 2,8,1", "D. 2,6,8"],
        "answer": "A"
    },
    {
        "question": "อุณหภูมิปกติของร่างกายมนุษย์คือเท่าใด",
        "choices": ["A. 37°C", "B. 36°C", "C. 38°C", "D. 35°C"],
        "answer": "A"
    },
    {
        "question": "แสงและแรงโน้มถ่วงอันไหนเร็วกว่ากัน",
        "choices": ["A. แสงเร็วกว่า", "B. แรงโน้มถ่วงเร็วกว่า", "C. เท่ากัน", "D. ขึ้นอยู่กับสภาวะ"],
        "answer": "A"
    },
    {
        "question": "glucose + fructose จะได้อะไร",
        "choices": ["A. Sucrose", "B. Lactose", "C. Maltose", "D. Starch"],
        "answer": "A"
    },
    {
        "question": "A={1,2,3,4} B={4,5,6,7} แล้ว AUB =",
        "choices": ["A. {1,2,3,4,5,6,7}", "B. {4}", "C. {1,2,3}", "D. {5,6,7}"],
        "answer": "A"
    },
    {
        "question": "P(A) ของ A={1,2,3,4} มีกี่จำนวน",
        "choices": ["A. 16", "B. 8", "C. 4", "D. 12"],
        "answer": "A"
    },
    {
        "question": "เพราะเหตุใดมนุษย์จึงจำเป็นต้องกินอาหาร",
        "choices": ["A. เพื่อให้ได้พลังงานและสารอาหาร", "B. เพราะหิว", "C. เพื่อให้ร่างกายเย็น", "D. เพื่อผลิตออกซิเจน"],
        "answer": "A"
    },
    {
        "question": "ถ้า p=T q=F แล้ว p∨q =",
        "choices": ["A. T", "B. F", "C. T และ F", "D. ไม่แน่นอน"],
        "answer": "A"
    },
]
    for i in range(10):
        Answer(i)
except ValueError:
    print("ใส่ได้แค่ตัวอักษร")
finally:
    print(total)