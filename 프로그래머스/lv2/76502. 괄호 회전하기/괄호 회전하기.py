def solution(s):
    answer = 0
    temp = list(s)
    for i in range(len(s)):
        st = []
        for j in range(len(temp)):
            if len(st) > 0:
                if st[-1] == '[' and temp[j] == ']':
                    st.pop()
                elif st[-1] == '(' and temp[j] == ')':
                    st.pop()
                elif st[-1] == '{' and temp[j] == '}':
                    st.pop()
                else:
                    st.append(temp[j])
            else:
                st.append(temp[j])
        if len(st) == 0:
            answer += 1
        temp.append(temp.pop(0))
    return answer