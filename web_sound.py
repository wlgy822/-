import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 제목
# -----------------------------

st.title("2차원 소리 간섭 시뮬레이션")

st.write(
    "스피커와 사람의 위치를 조절하여 "
    "파동의 간섭 현상을 관찰할 수 있습니다."
)

# -----------------------------
# 스피커 위치 조절
# -----------------------------

st.sidebar.header("🔊 스피커 위치 조절")

s1x = st.sidebar.slider(
    "스피커1 X좌표",
    0.0, 10.0, 3.0
)

s1y = st.sidebar.slider(
    "스피커1 Y좌표",
    0.0, 10.0, 7.0
)

s2x = st.sidebar.slider(
    "스피커2 X좌표",
    0.0, 10.0, 7.0
)

s2y = st.sidebar.slider(
    "스피커2 Y좌표",
    0.0, 10.0, 7.0
)

# -----------------------------
# 사람 위치 조절
# -----------------------------

st.sidebar.header("🧍 사람 위치 조절")

px = st.sidebar.slider(
    "사람 X좌표",
    0.0, 10.0, 5.0
)

py = st.sidebar.slider(
    "사람 Y좌표",
    0.0, 10.0, 2.0
)

# -----------------------------
# 기본 설정
# -----------------------------

wavelength = 2

k = 2 * np.pi / wavelength

speaker1 = [s1x, s1y]
speaker2 = [s2x, s2y]

person = [px, py]

# -----------------------------
# 공간 생성
# -----------------------------

x = np.linspace(0, 10, 300)
y = np.linspace(0, 10, 300)

X, Y = np.meshgrid(x, y)

# -----------------------------
# 거리 계산
# -----------------------------

d1 = np.sqrt(
    (X - speaker1[0])**2 +
    (Y - speaker1[1])**2
)

d2 = np.sqrt(
    (X - speaker2[0])**2 +
    (Y - speaker2[1])**2
)

# -----------------------------
# 간섭 계산
# -----------------------------

Z = np.sin(k*d1) + np.sin(k*d2)

# -----------------------------
# 사람 위치 진폭 계산
# -----------------------------

pd1 = np.sqrt(
    (person[0] - speaker1[0])**2 +
    (person[1] - speaker1[1])**2
)

pd2 = np.sqrt(
    (person[0] - speaker2[0])**2 +
    (person[1] - speaker2[1])**2
)

amplitude = np.sin(k*pd1) + np.sin(k*pd2)

# -----------------------------
# 그래프 생성
# -----------------------------

fig, ax = plt.subplots(figsize=(7,7))

img = ax.imshow(
    Z,
    extent=(0,10,0,10),
    origin='lower',
    cmap='coolwarm'
)

# 스피커 표시
ax.scatter(
    speaker1[0],
    speaker1[1],
    color='red',
    s=150,
    label='스피커 1'
)

ax.scatter(
    speaker2[0],
    speaker2[1],
    color='blue',
    s=150,
    label='스피커 2'
)

# 사람 표시
ax.scatter(
    person[0],
    person[1],
    color='white',
    s=150,
    label='사람'
)

ax.legend()

ax.set_title("파동 간섭 패턴")

# -----------------------------
# 그래프 출력
# -----------------------------

st.pyplot(fig)

# -----------------------------
# 결과 출력
# -----------------------------

st.subheader("📊 결과 분석")

st.write(
    f"현재 위치에서의 파동 진폭 : {amplitude:.2f}"
)

# -----------------------------
# 간섭 상태 판별
# -----------------------------

if abs(amplitude) > 1.5:

    st.success(
        "보강 간섭이 강하게 발생하는 위치입니다."
    )

elif abs(amplitude) < 0.3:

    st.warning(
        "상쇄 간섭이 발생하여 소리가 약해지는 위치입니다."
    )

else:

    st.info(
        "부분적인 간섭이 발생하는 위치입니다."
    )