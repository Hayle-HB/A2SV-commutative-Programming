class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
            words = sentence.split()
            
            dictionary.sort(key=len)
            
            for i in range(len(words)):
                for root in dictionary:
                    if words[i].startswith(root):
                        words[i] = root
                        break
            
            return ' '.join(words)