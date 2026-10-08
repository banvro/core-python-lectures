import streamlit as st   

st.title("Quiz App")

st.write("Topic Python intermediate quiz")

questions = [
  {
    "question": "What is the output of print(2 + 3 * 4)?",
    "Options": ["20", "14", "24", "10"],
    "Asnwer": "14"
  },
  {
    "question": "Which keyword is used to define a function in Python?",
    "Options": ["func", "define", "def", "function"],
    "Asnwer": "def"
  },
  {
    "question": "What is the data type of the value returned by type(10)?",
    "Options": ["str", "float", "int", "number"],
    "Asnwer": "int"
  },
  {
    "question": "Which of the following is used to create a list in Python?",
    "Options": ["{}", "[]", "()", "<>"],
    "Asnwer": "[]"
  },
  {
    "question": "What is the output of print(len('Python'))?",
    "Options": ["5", "6", "7", "8"],
    "Asnwer": "6"
  },
  {
    "question": "Which operator is used for exponentiation in Python?",
    "Options": ["^", "**", "//", "%%"],
    "Asnwer": "**"
  },
  {
    "question": "What is the output of print(10 // 3)?",
    "Options": ["3", "3.33", "4", "1"],
    "Asnwer": "3"
  }
]

# st.json(questions)

asnwers = []

for i, question in enumerate(questions):
    
    st.subheader(f"Question : {i+1}")
    
    ans = st.radio(
        question["question"],
        question["Options"],
        key = f"question_{i}",
        index = None 
    )
    
    asnwers.append(ans)
    # print(asnwers, "eeeeeeee")


btn = st.button("Submit Quiz", type = "primary")


if btn:
    score = 0
    
    for i, q in enumerate(questions):
        if asnwers[i] == q["Asnwer"]:
            score = score + 1
            
    st.header(score)