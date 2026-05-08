<div align="center">

# 🩺 KINGorithm

### 의료비 고위험군 선별을 위한 Top-K 알고리즘 비교 웹 서비스

**Medical Cost Risk Top-K Selection Algorithm Web App**

</div>

---

## 📌 프로젝트 요약

KINGorithm은 의료비 위험 점수를 기준으로 **상위 20% 고위험군 환자**를 선별하는 알고리즘 중심 웹 애플리케이션이다.

본 프로젝트는 단순한 AI 예측 서비스가 아니라, 알고리즘 과목 프로젝트의 목적에 맞게 여러 가지 **Top-K 선택 알고리즘**을 비교하는 데 초점을 둔다.

> `n`명의 환자 데이터가 주어졌을 때,  
> 위험 점수가 가장 높은 `k`명의 환자를 효율적으로 선별한다.

본 프로젝트에서는 다음과 같이 설정한다.

```text
k = 전체 환자의 상위 20%
```

선별된 환자들은 **고위험군**으로 분류된다.

---

## 🎯 핵심 아이디어

의료비 예측에서는 정확한 금액을 예측하는 것도 중요하지만, 실제 의료 및 보험 리스크 관리에서는 **고위험군을 조기에 식별하는 것**이 더 중요할 수 있다.

따라서 본 프로젝트는 의료비 리스크 문제를 다음과 같은 알고리즘 문제로 변환한다.

> **많은 환자 데이터 중에서 위험 점수가 높은 환자를 어떻게 효율적으로 선별할 수 있는가?**

---

## 🧠 비교할 알고리즘

| 접근 방식 | 설명 | 시간 복잡도 |
|---|---|---|
| **전체 정렬** | 모든 환자를 위험 점수 기준으로 정렬한 뒤 상위 k명 선택 | `O(n log n)` |
| **Min-Heap Top-K** | 크기 k의 heap을 유지하면서 상위 k명만 관리 | `O(n log k)` |
| **Quickselect** | partition 방식을 이용해 k번째 기준값을 찾음 | 평균 `O(n)`, 최악 `O(n²)` |

---

## 🧩 주요 기능

- 랜덤 환자 데이터 생성
- 의료비 위험 점수 계산
- 상위 20% 고위험군 환자 선별
- 여러 Top-K 알고리즘 실행 및 비교
- 각 알고리즘의 실행 시간 측정
- speedup ratio 표시
- 2D Canvas를 이용한 환자 위험 분포 시각화
- 선별된 고위험군 환자 강조 표시
- 선택적으로 LLM을 이용한 자연어 설명 제공

---

## 🏥 환자 데이터 구성

생성되는 환자 데이터는 다음과 같은 정보를 포함한다.

| 항목 | 설명 |
|---|---|
| **Age** | 환자 나이 |
| **Gender** | 성별 |
| **Visit Count** | 병원 방문 횟수 |
| **Chronic Disease Count** | 만성질환 개수 |
| **Previous Medical Cost** | 전년도 의료비 |
| **Admission Count** | 입원 횟수 |
| **Risk Score** | 계산된 의료비 위험 점수 |

---

## 📊 위험 점수 계산 방식

각 환자의 위험 점수는 간단한 가중치 기반 공식으로 계산한다.

```text
risk_score =
0.30 * previous_cost_score
+ 0.25 * visit_count_score
+ 0.20 * chronic_disease_score
+ 0.15 * age_score
+ 0.10 * admission_score
```

계산된 `risk_score`는 Top-K 알고리즘에서 정렬 및 선별 기준으로 사용된다.

---

## 🏗️ 시스템 구조

```text
[Frontend]
- 사용자 입력
- Canvas 시각화
- 결과 테이블 표시

        ↓

[Backend]
- 환자 데이터 생성
- 위험 점수 계산
- 알고리즘 실행
- 실행 시간 측정

        ↓

[Top-K Algorithms]
- Full Sorting
- Min-Heap Top-K
- Quickselect

        ↓

[Optional LLM Module]
- 자연어 설명 생성
- 리스크 리포트 생성
```

---

## 🖥️ 웹 인터페이스

웹 애플리케이션은 다음 기능을 제공한다.

| UI 요소 | 설명 |
|---|---|
| **환자 수 입력** | 사용자가 생성할 환자 수 선택 |
| **Generate Button** | 랜덤 환자 데이터 생성 |
| **Run Algorithms Button** | Top-K 알고리즘 실행 |
| **Result Table** | 알고리즘별 실행 시간 및 speedup 표시 |
| **2D Canvas** | 환자 위험 분포 시각화 |
| **Highlighted Points** | 선별된 고위험군 환자 강조 표시 |

---

## 🔌 API 엔드포인트

| Method | Endpoint | 설명 |
|---|---|---|
| `GET` | `/` | 프론트엔드 페이지 제공 |
| `POST` | `/generate` | 랜덤 환자 데이터 생성 |
| `POST` | `/top-k-risk` | Top-K 알고리즘 실행 및 결과 반환 |
| `POST` | `/explain` | 선택 기능: LLM 기반 설명 생성 |

---

## 🛠️ 기술 스택

| 영역 | 기술 |
|---|---|
| **Frontend** | HTML, CSS, JavaScript, Canvas |
| **Backend** | Python, FastAPI 또는 Flask |
| **Algorithms** | Python |
| **Data Processing** | Pandas / Python standard library |
| **Optional LLM** | Upstage Solar |
| **Version Control** | GitHub |

---

## 📁 프로젝트 구조

```text
KINGorithm/
├── app.py
├── algorithms.py
├── data_generator.py
├── requirements.txt
├── README.md
└── static/
    ├── index.html
    ├── style.css
    └── app.js
```

---

## 📈 성능 평가

최종 보고서에서는 입력 데이터 크기에 따른 알고리즘 실행 시간을 비교한다.

| 환자 수 | Full Sorting | Min-Heap Top-K | Quickselect |
|---:|---:|---:|---:|
| 100 | - | - | - |
| 1,000 | - | - | - |
| 5,000 | - | - | - |

보고서에서는 전체 정렬이 아닌 Top-K 알고리즘을 사용할 때 왜 더 효율적일 수 있는지 분석한다.

---

## 📄 보고서 핵심 내용

최종 보고서에서는 다음 내용을 중심으로 작성한다.

1. 의료비 위험군 선별 문제를 Top-K 선택 문제로 정의
2. 각 알고리즘의 동작 방식 설명
3. 각 알고리즘의 시간 복잡도 비교
4. 입력 크기에 따른 실행 시간 비교
5. 고위험군 시각화 결과 캡처
6. 전체 정렬보다 Top-K 선택 알고리즘이 효율적인 이유 분석
7. LLM은 핵심 알고리즘이 아니라 결과 설명 보조 기능임을 명시

---

## 👥 팀원 역할

| 역할 | 담당자 |
|---|---|
| **Frontend Lead** | 황유림 |
| **Backend / Server Lead** | 고은서 |
| **LLM Integration / Prompt Engineering Lead** | 이유라 |
| **PM / Planning / Documentation / Presentation Coordination** | 박재형 |

<div align="center">

### KINGorithm  
**알고리즘 효율성을 기반으로 고위험군을 선별하는 웹 서비스**

</div>