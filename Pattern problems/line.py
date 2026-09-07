para = ("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since 1966, when designers at Letraset and James Mosley, the librarian at St Bride Printing Library in London, took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets. It has survived not only many decades, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised thanks to these sheets and more recently with desktop publishing software like Aldus PageMaker and Microsoft Word including versions of Lorem Ipsum.")
line_len =  50
strs=[]
ans=[]
count = 0
for char in para:
    strs.append(char)   
for i in range(0, len(strs), 1):
    if count == line_len:
        # if strs[i+line_len]!=" ":
        #     i -= 2
        ans.append(strs[i-1:i+line_len])
        count = 0
    else:
        count +=1

for i in range(0, len(ans)):
    print("".join(ans[i]))

    





        
        
 
    