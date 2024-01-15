

def removeDuplicateLetters(s: str) -> str:
        occurrence = {}
        visited = set()
        for i, c in enumerate(s):
            occurrence[c] = i
        stack = []
        for i, c in enumerate(s):
            if c not in visited:
                while stack and occurrence[stack[-1]] > i and stack[-1] > c:
                    visited.remove(stack.pop())
                stack.append(c)
                visited.add(c)
            print(stack, occurrence)
        return "".join(stack)


if __name__ == "__main__":
    x = removeDuplicateLetters("cbacdcbc")
    print(x)
    

    
