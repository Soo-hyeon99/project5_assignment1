# 학생들의 이름과 점수를 딕셔너리에 저장
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90
}

# 특정 학생의 이름을 입력 받아 점수를 출력
name = "Bob"
score = students.get(name)

print(f"{name}의 점수는 {score}점입니다.")