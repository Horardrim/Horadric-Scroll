from typing import List

def solution(input: List[int], target: int) -> List[int]:
    result = []
    cache = {}
    idx : int = 0
    for i in input:
        if i in cache:
            result.append(cache.get(i))
            result.append(idx)
            break

        cache[target - i] = idx
        idx += 1

    return result
