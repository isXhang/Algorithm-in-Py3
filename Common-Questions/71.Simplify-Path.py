class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.rstrip('/')
        if not path: return "/"

        stack = []
        path = path.split('/')
        # ['', 'home', '..', '', 'foo']
        for char in path:
            if char == '' or char == '.': continue
            elif char == "..":
                if stack:
                    stack.pop()
                else: continue
            else: stack.append(char)
        return '/' + '/'.join(stack)
