os16 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
prs4 = ["00", "01", "02", "03", "10", "11", "12", "13", "20", "21", "22", "23", "30", "31", "32", "33"]

D = input()
L = int(input())
N = input()

tstr = ''
st = ""

for i in range(L):
    tstr = N[L-1-i] + tstr
    if len(tstr) == 2:
        st = os16[prs4.index(tstr)] + st
        tstr = ""
        
if len(tstr) == 1:
    tstr = "0" + tstr
    st = os16[prs4.index(tstr)] + st
        
print(st.count(D))