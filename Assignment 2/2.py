st = ""

def wordcount(st):
    counts = dict()
    w = st.split()
    for y in w:
        if y in counts:
            counts[y]+=1
        else:
            counts[y]=1
    return counts

with open(r'input.txt','r') as file:
    data = file.read()
    st +=data

a=str(wordcount(st))
st+="\nWord_Count: \n"
st+=a
st = st.replace("{","")
st = st.replace("}","")
st = st.replace("'","")
st = st.replace("P","\nP")
st = st.replace(", ","\n")
print(st)

outputfile = open(r'output.txt','w')
outputfile.write(st)
outputfile.close()
file.close()
