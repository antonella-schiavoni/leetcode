# 1. Two Sum · Easy

**Link:** [LeetCode #1](https://leetcode.com/problems/two-sum/)

---

## Solución

```python
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        return []
```

**Complejidad:** O(n) tiempo · O(n) espacio

---

## Explicación

Por cada número calculo su **complemento** (`target - num`) y verifico si ya lo vi antes en un hash map. Si está, encontré el par. Si no, guardo el número actual y sigo.

Esto evita el doble loop O(n²) — cada lookup en el dict es O(1).
