class Solution:
    def __init__(self):
        pass
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        concatenated_words = []
        check_length = int
        words = set(words)
        for x in words:
            memory = set()
            check_length = len(x)

            if self.checkconcatenated(x, words,check_length,memory):
                concatenated_words.append(x)
            else:
                continue
        return concatenated_words

    def checkconcatenated(self, to_be_checked: str, words: list[str],length_of_word,memory: set(str)):
        print(f"Checking: '{to_be_checked}', memory:{memory}")
        temp = to_be_checked
        if temp in memory:
            print("It was meeee")
            return False
        for word in words:
            if len(word)<= len(to_be_checked) and len(word)<length_of_word:
                if word == to_be_checked[0:len(word)]:
                    upd_to_be_checked = to_be_checked.replace(word, "", 1)
                    if upd_to_be_checked =="":
                        print(f"Checked:{to_be_checked} It was concatenated")
                        return True
                    else:
                        trigger = self.checkconcatenated(to_be_checked=upd_to_be_checked, words=words,length_of_word=length_of_word,memory=memory)
                        if trigger == False:
                            pass

                        else:
                            return True
        print(f"Checked:{to_be_checked} It was nonconcatenated")
        memory.add(temp)
        return False


if __name__ == "__main__":
    solution = Solution()
    words = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaab"]
    result = solution.findAllConcatenatedWordsInADict(words)
    print(result)