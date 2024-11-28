def naive_search(pat, txt):
    M, N = len(pat), len(txt)
    for i in range(N - M + 1):
        if txt[i:i + M] == pat:
            print(f"Pattern found at index {i}")

txt = "AABAACAADAABAAABAA"
pat = "AABA"
naive_search(pat, txt)
