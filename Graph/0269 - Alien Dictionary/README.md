# Alien Dictionary

There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings `words` from the alien language's dictionary. Now it is claimed that the strings in `words` are sorted lexicographically by the rules of this new language.

Lexicographically: A string `a` is **lexicographically smaller** than `a` string `b` if in the first position where `a` and `b` differ, string `a` has a letter that appears earlier in the alien language than the corresponding letter in `b`. If the first `min(a.length, b.length)` characters do not differ, then the shorter string is the lexicographically smaller one.

If this claim is incorrect, and the given arrangement of string in `words` cannot correspond to any order of letters, return `""`.

Otherwise, return _a string of the unique letters in the new alien language sorted in ***lexicographically increasing order*** by the new language's rules_. If there are multiple solutions, return **_any of them_**.
