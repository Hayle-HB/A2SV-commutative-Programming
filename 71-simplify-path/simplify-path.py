class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')

        stack = []

        for pt in path:
            if stack and pt == '..':
                stack.pop()
            elif pt not in ['.', '..', '']:
                stack.append(pt)
        

        return '/' + '/'.join(stack)


        