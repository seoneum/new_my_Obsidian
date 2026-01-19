# 정렬 알고리즘

## 1. 기본 O(n²) 정렬

### Bubble Sort (버블 정렬)
**원리**: 인접한 두 원소를 비교해서 큰 것을 뒤로 보냄

```cpp
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-1-i; j++) {
            if (arr[j] > arr[j+1])
                swap(arr[j], arr[j+1]);
        }
    }
}
```

| 특징 | 설명 |
|------|------|
| 시간 | O(n²) |
| Swap 횟수 | O(n²) - 가장 많음 |
| Stable | ✅ Yes |
| 비고 | 가장 느림, 논외 수준 |

### Selection Sort (선택 정렬)
**원리**: 최솟값을 찾아서 맨 앞으로 이동

```cpp
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        int minIdx = i;
        for (int j = i+1; j < n; j++) {
            if (arr[j] < arr[minIdx])
                minIdx = j;
        }
        swap(arr[i], arr[minIdx]);
    }
}
```

| 특징 | 설명 |
|------|------|
| 시간 | O(n²) |
| Swap 횟수 | O(n) - 한 라운드에 1번 |
| Stable | ❌ No |
| 비고 | Swap 비용이 클 때 유리 |

### Insertion Sort (삽입 정렬)
**원리**: 정렬된 부분에 새 원소를 적절한 위치에 삽입

```cpp
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }
}
```

| 특징 | 설명 |
|------|------|
| 시간 | O(n²), 거의 정렬됨: O(n) |
| Stable | ✅ Yes |
| 비고 | Shell Sort의 기반 |

---

## 2. 고급 O(n log n) 정렬

### Merge Sort (병합 정렬) ⭐⭐⭐

**원리**: Divide & Conquer
1. 반으로 쪼갬 (하나 남을 때까지)
2. 합치면서 정렬

```cpp
void merge(int arr[], int l, int m, int r) {
    // 임시 배열 사용
    int n1 = m - l + 1;
    int n2 = r - m;
    int* L = new int[n1];
    int* R = new int[n2];
    
    // 복사
    for (int i = 0; i < n1; i++) L[i] = arr[l + i];
    for (int j = 0; j < n2; j++) R[j] = arr[m + 1 + j];
    
    // 병합
    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j])
            arr[k++] = L[i++];
        else
            arr[k++] = R[j++];
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
    
    delete[] L;
    delete[] R;
}

void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}
```

| 특징 | 설명 |
|------|------|
| 시간 | O(n log n) - 항상 보장 |
| 공간 | O(n) - 추가 메모리 필요 |
| Stable | ✅ Yes |
| 비고 | **Not In-place** |

### Quick Sort (퀵 정렬)

**원리**: Pivot을 기준으로 분할
1. Pivot 선택
2. Pivot보다 작은 것은 왼쪽, 큰 것은 오른쪽
3. 재귀적으로 정렬

```cpp
int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
```

| 특징 | 설명 |
|------|------|
| 시간 | 평균 O(n log n), 최악 O(n²) |
| 공간 | O(log n) - In-place |
| Stable | ❌ No |
| 비고 | 실전에서 가장 빠름 |

### Heap Sort (힙 정렬)

**원리**: 힙을 이용한 정렬
1. 힙 구축
2. 하나씩 꺼내면 정렬

| 특징 | 설명 |
|------|------|
| 시간 | O(n log n) - 항상 보장 |
| 공간 | O(1) - In-place |
| Stable | ❌ No |

---

## 3. 정렬 알고리즘 비교표 ⭐⭐⭐

| 알고리즘 | 평균 | 최악 | 공간 | Stable | In-place |
|----------|------|------|------|--------|----------|
| Bubble | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| Selection | O(n²) | O(n²) | O(1) | ❌ | ✅ |
| Insertion | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| Merge | O(n log n) | O(n log n) | O(n) | ✅ | ❌ |
| Quick | O(n log n) | O(n²) | O(log n) | ❌ | ✅ |
| Heap | O(n log n) | O(n log n) | O(1) | ❌ | ✅ |

---

## 4. Stable vs Unstable

### Stable Sort
- 같은 값의 원소들의 **상대적 순서 유지**
- 예: `[2a, 1, 2b]` → `[1, 2a, 2b]`

### Unstable Sort
- 같은 값의 원소들의 순서가 바뀔 수 있음
- 예: `[2a, 1, 2b]` → `[1, 2b, 2a]` (가능)

**Selection Sort가 Unstable인 이유:**
```
[2a, 2b, 1] → 최솟값 1을 2a와 swap
[1, 2b, 2a] → 2a와 2b의 순서가 바뀜!
```

---

## 5. 시험 핵심 체크리스트

- [ ] 각 정렬의 시간/공간 복잡도 암기
- [ ] Stable/Unstable 구분
- [ ] In-place 여부
- [ ] Merge Sort: 추가 공간 O(n) 필요
- [ ] Quick Sort: 최악 O(n²), Pivot 선택 중요
- [ ] Heap Sort: In-place, Unstable
- [ ] 정렬 과정 손으로 그리기 (시험 필출)
