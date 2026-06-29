# 217. Contains Duplicate · Easy

**Link:** [LeetCode #217](https://leetcode.com/problems/contains-duplicate/)

---

## Solución 1 — Loop con early exit

```python
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen: set[int] = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

**Complejidad:** O(n) tiempo · O(n) espacio

Recorro el array manteniendo un set de números ya vistos. Si el número actual ya está en el set, retorno `True` inmediatamente sin procesar el resto del array.

---

## Solución 2 — One-liner pythónico

```python
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```

**Complejidad:** O(n) tiempo · O(n) espacio

Convierte el array a set (que elimina duplicados) y compara los tamaños. Si son distintos, había duplicados.

---

## Conclusión

La **Solución 1** es mejor en la práctica. Aunque ambas tienen la misma complejidad teórica O(n), el loop con early exit corta en cuanto encuentra el primer duplicado — en el peor caso recorre todo, pero en el caso promedio es más rápido.

La **Solución 2** siempre construye el set completo antes de comparar, sin importar si el duplicado estaba en la posición 1 o en la última. Es más legible y suficiente para entrevistas donde la claridad importa, pero no es óptima en runtime.

> En una entrevista: mencioná el one-liner como solución obvia, luego proponé el loop como optimización para casos con duplicados tempranos. Eso muestra que pensás en casos promedio, no solo en worst case.
