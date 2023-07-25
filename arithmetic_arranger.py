def arithmetic_arranger(problems, B = None):
    my_str = problems
    line1=""
    line2=""
    line3=""
    line4=""
    i=0
    if len(my_str) <= 5:
        for st in my_str:
            x=st.split()
            if len(x[0]) < 5 and len(x[2]) < 5:
                if x[1] in "+-":
                    if x[0].isnumeric() and x[2].isnumeric():
                        v = max(len(x[0]),len(x[2]))
                        lines="-"
                        line1+= x[0].rjust(v+2,' ')
                        line2+= x[1] + x[2].rjust(v+1,' ')
                        line3+= lines*(v+2)
                        if x[1]=="+":
                            summa=int(x[0])+int(x[2])
                        else:
                            summa=int(x[0])-int(x[2])
                        line4+= str(summa).rjust(v+2,' ')
                        i=i+1
                        if i<len(my_str):
                            line1+='    '
                            line2+='    '
                            line3+='    '
                            line4+='    '
                    else: 
                            return "Error: Numbers must only contain digits."
                else:
                    return "Error: Operator must be '+' or '-'."
            else:
                return "Error: Numbers cannot be more than four digits."
    else:
        return "Error: Too many problems."
    if B == True:
        answer=line1+"\n"+line2+"\n"+line3+"\n"+line4
        return answer
    else:
        answer=line1+"\n"+line2+"\n"+line3
        return answer
