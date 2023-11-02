'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.



Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.

'''
from typing import List
from pprint import pprint


class Trie():
    def __init__(self):
        self.root = {"*": "*"}

    def add_word(self, word: str):
        current_node = self.root
        for letter in word:
            print("letter", letter)
            if letter not in current_node:
                current_node[letter] = {}
            current_node = current_node[letter]
        current_node["*"] = "*"

    def does_word_exists(self, word: str):
        current_node = self.root
        for letter in word:
            if letter not in current_node:
                return False
            current_node = current_node[letter]
        return "*" in current_node

    def get_common_prefix(self):
        current_node = self.root
        common_prefix = "-"
        if len(current_node) > 2:
            return common_prefix.replace("-", "")
        root_call = True
        while current_node:
            pprint(current_node)
            ch = list(current_node.keys())
            child_nodes = ch if ch is not None else []
            if root_call:
                child_nodes.remove("*")
                root_call = False
            print("child _Nodes", child_nodes)

            if len(child_nodes) == 1:
                if child_nodes[0] != "*":
                    common_prefix += child_nodes[0]
                    current_node = current_node[child_nodes[0]]
                    print("common_prefix", common_prefix)
                else:
                    break
            else:
                break
        print(common_prefix)
        return common_prefix.replace("-", "")


class SolutionOne:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            print("word", word)
            if word == "":
                word = "-"
            trie.add_word(word)
        return trie.get_common_prefix()


class SolutionTwo:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans = ""
        v = sorted(v)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return ans
            ans += first[i]
        return ans


if __name__ == '__main__':
    sol = SolutionTwo()
    strs = ["flower","flow","flight"]
    output = "fl"
    result = sol.longestCommonPrefix(v=strs)
    print(result)
    assert output == result
