# 변수 선언
name = "홍길동"
age = 1000
score = 95.5

# 1. 기본 출력
print("Hello, Python!")

# 2. 여러 값 출력 (콤마로 구분 → 자동 띄어쓰기)
print("Name:", name, "Age:", age, "Score:", score)

# 3. f-string (가장 많이 쓰임, Python 3.6+)
print(f"My name is {name}, I am {age} years old, score: {score}")

# 4. format() 함수
print("My name is {}, I am {} years old, score: {}".format(name, age, score))
print("My name is {0}, age {1}, score {2}".format(name, age, score))
print("Score with 2 decimals: {:.2f}".format(score))

# 5. % 포맷팅 (C 스타일, 옛날 방식)
print("Name: %s, Age: %d, Score: %.1f" % (name, age, score))

# 6. 여러 줄 출력 (줄바꿈 포함)
print("This is line 1\nThis is line 2")

# 7. end 옵션 (기본값은 줄바꿈 '\n')
print("Hello", end=" ")
print("World!")

# 8. sep 옵션 (기본값은 공백 ' ')
print("2025", "09", "23", sep="-")

# 9. 딕셔너리/리스트 같이 출력
data = {"name": name, "age": age, "score": score}
print("Data:", data)

# 10. f-string 내 계산식/함수 사용
print(f"Next year age: {age + 1}")
print(f"Score (rounded): {round(score)}")

# 11. 멀티라인 f-string (''' 혹은 """)
print(f"""
Student Info:
 - Name : {name}
 - Age  : {age}
 - Score: {score:.2f}
""")
