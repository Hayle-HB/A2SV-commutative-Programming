class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #0: declare oneIndex, twoIndex at 0, 0 and mergedString as empty array 
        wordOneIndex = 0
        wordTwoIndex = 0
        mergedString = []

        #00: if oneIndex or twoIndex is greater than the length of word1 and word2 respectivily, goto step #6

        while wordOneIndex < len(word1) and wordTwoIndex < len(word2):


                #1.  start from the first word 
                #2. append the given oneIdx to the answer
                mergedString.append( word1[wordOneIndex] )

                #3. increment oneIdx by one oneIndex = oneIndex + 1
                wordOneIndex += 1


                #4. appned the given character at twoIndex
                mergedString.append(word2[wordTwoIndex])


                #5 incremenet twoIndex by one: twoIndex = twoIndex + 1
                wordTwoIndex += 1
                #get to step #00

                


        #6: if there is remain charater of word1 that didn't added, append at the end of the answer
        mergedString.extend(word1[wordOneIndex:])

        #7: if there is a remmain character of word2, then appned it to the end of the answer
        mergedString.extend(word2[wordTwoIndex:])


        # return the answer you got after merged

        return ''.join(mergedString)


        





        