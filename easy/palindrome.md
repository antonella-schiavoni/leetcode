# 9. Palindrome Number · Easy

**Link:** [LeetCode #9](https://leetcode.com/problems/palindrome-number/)

---

## Solución

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes.
        # Numbers ending in 0 (except 0 itself) can't be palindromes either.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        # Reverse only half of the number.
        # When x <= reversed_half, we've processed half the digits.
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Even number of digits: x == reversed_half
        # Odd number of digits: drop the middle digit with reversed_half // 10
        return x == reversed_half or x == reversed_half // 10
```

**Complejidad:** O(log₁₀ n) tiempo · O(1) espacio

---

## Explicación

La forma obvia de resolver esto es convertir el número a string y comparar con su reverso, pero eso usa espacio extra O(n). La idea acá es no convertir a string ni revertir el número completo — solo revertir la **mitad** y comparar.

En cada iteración del loop, extraigo el último dígito de `x` (`x % 10`) y lo voy agregando a `reversed_half`, mientras le quito ese dígito a `x` (`x //= 10`). El loop corta cuando `x <= reversed_half`, momento en el que ya procesé la mitad de los dígitos.

Al final hay dos casos según la cantidad de dígitos: si es par, `x` y `reversed_half` deben ser exactamente iguales (ej. `1221` → `x=12`, `reversed_half=12`). Si es impar, `reversed_half` tiene un dígito de más (el del medio), por eso se compara contra `reversed_half // 10` (ej. `12321` → `x=12`, `reversed_half=123`, se descarta el 3 del medio).

Los edge cases del principio evitan trabajo innecesario: los negativos nunca son palíndromos (el signo `-` rompe la simetría), y cualquier número que termine en 0 (salvo el 0 mismo) tampoco puede serlo, porque un palíndromo no puede empezar con 0.
