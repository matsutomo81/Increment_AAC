# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 13:42:05 2019

@author: matsuda
"""
from itertools import product

class for_loop():
    def __init__(self,v,v_range): #v:loop変数 v_range:vが動く範囲
         self.loop_variable=v
         self.v_range=v_range
         

class index_append():
    def __init__(self,index): 
         self.index=index

class assignment():
    def __init__(self,index_list,sentence,operator):
        self.index_list=index_list
        self.sentence=sentence
        self.operator=operator
        





class rectangle():
    """
超直方体に対応するクラス
[(a,b),(c,d)]または[[a,b],[c,d]]のような入力形式に対応
"""
    def __init__(self,vertex): #v:accumurative variable e:expression #v+=e ("v",a,"i+k","l","i
        if type(vertex[0])==tuple or list:
             self.dim=len(vertex[0])
             self.vertex1=[i for i in vertex[0]]
             self.vertex2=[i for i in vertex[1]]
             self.vertexes=self.vertex1+self.vertex2
        else:
             self.dim=len(vertex)//2
             self.vertex1=[i for i in vertex[:self.dim]]
             self.vertex2=[i for i in vertex[self.dim:]]
             self.vertexes=self.vertex1+self.vertex2        
        self.length=[abs(self.vertex1[i]-self.vertex2[i]) for i in range(self.dim)]






def normal_execution(loop_suo,expression_list):
    """
入力から通常実行するコードを書き出す
漸増化アルゴリズムとは関係ない
"""
    s=""
    indent=1
    s+="ans=[]"+"\n"
    s+=make_loop(loop_suo)+"    "*indent
    s+="ans.append(0)"+"\n"+"    "*indent
    for i in expression_list:
        if type(i)==for_loop:
            indent+=1
            s+=make_loop(i)+("    "*indent)
        if type(i)==assignment:
            s+=i.sentence+"\n"+("    ")*indent
    return(s)






def check_between_vertex(index1,index2,index_list,flag):    
    """
２個の頂点inde1,2の間に空欄のインデックスが無いかを調べる
"""
    start=min(index1[flag[1]],index2[flag[1]])
    goal=max(index1[flag[1]],index2[flag[1]])
    check=True

    if index1[flag[1]]<index2[flag[1]]:
        tmp=list(index1)
    else:
        tmp=list(index2)
        
    for i in range(start,goal):
        tmp[flag[1]]=i
        if tuple(tmp) not in index_list:
            return False
    return check



def vertex_check(sample,index):
    """
インデックスの集合sampleでindexが頂点か否かをチェックする
"""
    for i in range(len(index)):
        upindex=list(index)
        upindex[i]+=1
        downindex=list(index)
        downindex[i]+=-1
        if tuple(upindex) in sample and tuple(downindex) in sample:
            return False
    return True



def make_vertex_list(sample):
    """
インデックスの集合sampleの頂点を列挙
"""
    vertex_li=[]
    for j in range(len(sample)): 
        vertex=vertex_check(sample,sample[j])
        #頂点ならばリストに追加
        if vertex==True:
            vertex_li.append(sample[j])
    return vertex_li







def make_Difference_set(tuple1,tuple2):
    """
inc,decを求めるための集合差計算で使うもの
差集合の演算をするために入力はタプル型とする
"""
    if tuple1==[]:
        return []
    elif tuple2==[]:
        return tuple1
    else:
        li=sorted(list(set(tuple1).difference(set(tuple2))))
    return li



def make_loop (loop_class):
    """
for_loopのクラス形式を通常のループ文に変換して書き出す
"""
    if type(loop_class.v_range)==str:
        if "range" in loop_class.v_range:
            s="for "+loop_class.loop_variable+" in "+loop_class.v_range+":"+"\n"
        else:
            s="for "+loop_class.loop_variable+" in range("+loop_class.v_range+"):"+"\n"
    else:
        s="for "+loop_class.loop_variable+" in "+str(loop_class.v_range)+":"+"\n"
    return s


def make_index_append(index_list):
    """
インデックスの書き出しを行うためのコードを生成する
"""
    s1=""
    for i in index_list:
        s1+=i+","
    s="orig[i].append(("+s1[:-1]+"))"
    return s




def make_rectangle(index1,index2,li):
    """
頂点index1,2が線分になっているか調べ、線分ならば次元拡張
入力は任意の次元で可能
"""

    """
まずはindex1,2が線分になっているか調べる
"""
    dim=len(index1)
    #flagは[２インデックスの等しくない要素数,等しくない要素インデックスの記録]
    flag=[dim,None]
    if index1==index2:
        print("2個のインデックスが等しいため、これは点です")
        return False,[]
    
    for i in range(dim):
        if index1[i]==index2[i]:
            flag[0]+=-1
        else:
            if flag[1]==None:
                flag[1]=i
            else:#等しくないインデックスが2個以上あり、すなわちindex1,2が一直線上にない場合
                return False,[]
            
    #線分の間に空間が無いか調べる
    if flag[0]==0:
        return False,[]
    
    check=check_between_vertex(index1,index2,li,flag)
    if check==False:
        return False,[]
    
    #線分と認められた場合、線分を拡張して長方形になるかを調べる
    #ここでindex1,2を、小さい順に並べておく
    if index2[flag[1]]<index1[flag[1]]:
        start_index=list(index2[:])
        goal_index=list(index1[:])
    else:
        start_index=list(index1[:])
        goal_index=list(index2[:])
      
        
    """
    ここから次元拡張
    """
    for j in range(dim):
        if j!=flag[1]:
            #index1の近傍調査
        
            while True:
                goal_index[j]+=1
                #print(enumeration_index_from_vertex(start_index,goal_index),"が拡大候補")
                if set(enumeration_index_from_vertex(start_index,goal_index)) <= set(li):
                    pass
                else:
                    goal_index[j]+=-1
                    break
                
            while True:
                start_index[j]+=-1
                if set(enumeration_index_from_vertex(start_index,goal_index)) <= set(li):
                    pass
                else:
                    start_index[j]+=1
                    break
    return True,[start_index,goal_index]
              


def enumeration_index_from_vertex(index0,index1):
    """
index0とindex1を対頂点とするような超直方体を考え、その内部のインデックスを列挙して返す
"""
    li=[]
    for i in range(len(index0)):
        li.append([j for j in range(index0[i],index1[i]+1)])
    return(list(product(*li)))



def devide_index(li):
    """
インデックスのリストを入力にとり、そのインデックスを超直方体の集合に切り分ける
"""
    if li ==[]:
        return None   
    codes=[]
    
    for n in range(1000):
        tmp_vertex=make_vertex_list(li)
        print("今回の頂点は",tmp_vertex,"である\n")
        #2点の様子を調べる
        
        for i in range(len(tmp_vertex)):
            for j in range(len(tmp_vertex)):
                if i>j:
                    check,del_vertex=make_rectangle(tmp_vertex[i],tmp_vertex[j],li)
                    
                    if check==True:
                        print("頂点インデックスが", del_vertex, "である長方形を発見")
                        codes.append(rectangle(del_vertex))
                        del_li=enumeration_index_from_vertex(del_vertex[0],del_vertex[1])
                        #print(del_li,"が消去されます")

                        for qq in del_li:
                            li.remove(qq)
                            
                        print(str(n+1)+"回目の除去により","残りのインデックスは"+str(li),"\n")        
                        if li==[]:
                            return codes
                        break                  
            else:
                continue
            break
        
    for i in li:
        codes.append(rectangle([i,i]))
    return codes


def make_coordinate_difference(rectangles):
    """
inc, decの集合列が得られた後、それらの超直方体インデックスを参照し、各超直方体インデックスの差分ベクトルを求める
"""
    difference=[]
    if rectangles==[]:
        #print("長方形がありません!")
        return None        
    elif len(rectangles[0])==[]:
        #print("長方形がありません!")
        return None
    elif len(rectangles[0])!=len(rectangles[1]):
        print("長方形の数が変化しているので本システムでは漸増化できません")
        return None
    else:#エラーではない場合
        for i in range(len(rectangles[0])):            
            li1=rectangles[0][i].vertexes.copy()
            li2=rectangles[1][i].vertexes.copy()
            li=[li2[i]-li1[i] for i in range(len(li1))]
            difference.append(li)

        return difference
    

def rectangle_to_loop(rectangle,difference,indent_number=1,variable_name="b",start_number=1,inc_or_dec="inc",coefficient=1,operator="+"):
    """
得られた超直方体をテキストの形の出力でループ文そのものに変換する
"""
    s=""
    start=[]
    goal=[]
    for i in range(rectangle.dim):
        if rectangle.vertex1[i]<rectangle.vertex2[i]:
            start,goal=rectangle.vertex1[i],rectangle.vertex2[i]
            flag=[0,1]
        else:
            goal,start=rectangle.vertex1[i],rectangle.vertex2[i]
            flag=[1,0]

        tmp="    "*(i+indent_number)+"for "+"p"+str(i)+" in range("+str(start)+"+(i-"+str(start_number)+")*"+\
        str(difference[flag[0]*rectangle.dim+i])+","+str(goal+1)+"+(i-"+str(start_number)+")*"+str(difference[flag[1]*rectangle.dim+i])+"):\n"

        s+=tmp
        #goal+1はpythonのレンジの仕様のため

    if inc_or_dec=="inc":
        if operator==("max" or "min"):
            s+="    "*(i+1+indent_number)+"inc_ans[i]="+operator+"(inc_ans[i],b[p0][p1])"+"\n"
        elif operator=="*":
            s+="    "*(i+1+indent_number)+"inc_ans[i]"+operator+"="+str(coefficient)+"*b[p0][p1]"+"\n"
        else:
            s+="    "*(i+1+indent_number)+"inc_ans[i]"+operator+"="+str(coefficient)+"*b[p0][p1]"+"\n"
    elif inc_or_dec=="dec":
        if operator==("max" or "min"):
            print("decが空集合列でないため、"+operator+"演算子は扱えません")
            return False
        elif operator=="*":
            s+="    "*(i+1+indent_number)+"inc_ans[i]"+"/"+"="+str(coefficient)+"*b[p0][p1]"+"\n"
        else:
            s+="    "*(i+1+indent_number)+"inc_ans[i]"+operator+"="+str(coefficient)+"*b[p0][p1]"+"\n"
    return s

    
    
def output_code(expression_inc_all,expression_dec_all,sample=2,n=100,init=0,estimate_complexity_option=False,inc_coefficient=[1],dec_coefficient=[-1],operator="+"):
    """
    これまでのプロセスで得られた情報からコードを書き出す
"""
    
    indent_number=1
    s="inc_ans=["+str(init)+"]+"+"[0 for i in range("+str(n-1)+")]\n"
    s+="#漸増化パート"+"\n"
    s+="for i in range(1,"+str(n)+"):\n"
    s+="    "+"inc_ans[i]=inc_ans[i-1]\n\n"
    
    
    loop_number=-1
    for inc_rectangles in expression_inc_all:
        operator
        loop_number+=1
        try:
            inc_difference=make_coordinate_difference(inc_rectangles)
            for i in range(len(inc_rectangles[0])):
                if estimate_complexity_option==True:
        
                    tmp,d=estimate_complexity(inc_rectangles[0][i],inc_difference[i],sample)
                    s+="#estimate complexity:"+str(tmp)+"*n**"+str(d)+"\n\n"
                
                    
                try:1
                    s+=rectangle_to_loop(inc_rectangles[0][i],inc_difference[i],indent_number,"b",sample,"inc",inc_coefficient[loop_number],operator)+"\n"
                except:

                    pass
        except:
            pass
    
    loop_number=-1
    for dec_rectangles in expression_dec_all:
        loop_number+=1
        try:
            dec_difference=make_coordinate_difference(dec_rectangles)
            for i0 in range(len(dec_rectangles[0])):
                if estimate_complexity_option==True:    
                    tmp,d=estimate_complexity(dec_rectangles[0][i],dec_difference[i],sample)
                    s+="#estimate complexity:"+str(tmp)+"*n**"+str(d)+"\n\n"
                try:
                    s+=rectangle_to_loop(dec_rectangles[0][i],dec_difference[i],indent_number,"b",sample,"dec",dec_coefficient[loop_number],operator)+"\n"
                except:
                    pass
        except:
            pass
    
    return s



def estimate_complexity(rectangle,difference,sample):
    """
超直方体から計算回数を算出する
ただし、ループ回数を変数とする多項式の最高次のみ
漸増化アルゴリズムとは独立に動作
"""
    #print("計算量を求めています",rectangle.vertexes,difference, sample)
    li=[rectangle.vertexes[i]-difference[i] for i in range(rectangle.dim*2)]
    li2=[abs(li[i]-li[i+2])+1 for i in range(rectangle.dim)]#長方形の一片長さ
    li3=[abs(difference[j+2]-difference[j]) for j in range(len(difference)//2)]#移動ベクトルの差分
    if 0 not in li3:
        return ((li3[0]+1)*(li3[1]+1)/3,3)
    if li3==[0,0]:
        return (li2[0]*li2[1],1)
    if li3[0]==0:
        return (li3[1]*li2[0]/2,2)
    if li3[1]==0:
        return (li3[0]*li2[1]/2,2)        
    