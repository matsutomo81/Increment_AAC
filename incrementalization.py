# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 22:17:07 2020

@author: matsuda
"""

"""
このコードはdevide_index_moduleとセットで使う
"""
import devide_index_module as di
import time
import random

index_list=[]

#インデックスの集合を多プルの入ったリストの形で与えると、長方形が返ってくる[(),()]


"""
問題の準備
計算に使う寄与配列bを定義
"""

try:
    b[0]
except:
    b=[[random.randint(-1000, 1000) for i in range(3000)] for j in range(3000)] 
    
    
    
"""   
計算するステップ数をnliに入力
"""
nli=[100]
problem=0


"""
problemで選んだ計算が実行される
if problem==から始まる一連のコードブロックがシステムへの入力に相当する

論文中実験パートの入力は
プログラムB:problem==0
プログラムC:problem==4
プログラムD:problem==6
"""


for n in nli:
    if problem==0:
        """
        クラスdi.for_loopを使ってループを記述する
        di.for_loop("ループ変数名","範囲")のようにする
                    
        漸増化対象for文をloop_suoと書く
        """
        loop_suo = di.for_loop("i",range(n))
        loop_l1 = di.for_loop("l1","range((2*i+1))")
        loop_l2 = di.for_loop("l2","range((2*i+1))")
        """
        代入文はdi.assignment("[代入文テキスト中で参照する寄与配列のインデックス]","代入文テキスト","代入文の演算子")
        のように入力する
        演算は"+","*","min","max"が使える
        配列参照は["l1","l2"]のように2次元しか入力できない
        """
        assignment_1=di.assignment(["l1","l2"],"ans[i]+=b[l1][l2]","+")
        """
        inc_coefficientは"ans[i]+=1*b[l1][l2]"における"1*"にあたる係数を指定する
        dec_coefficientは"ans[i]+=1*b[l1][l2]"の逆演算として"-1*"を指定する
        代入文個数とinc_coefficient,dec_coefficientの要素数が一致するようにする
        """
        inc_coefficient=[1]
        dec_coefficient=[-1]        
        """
        expression_listのリスト要素として上記のループ文と代入文を実行する順に入力する
        """
        expression_list=[loop_l1,loop_l2,assignment_1]
        """
        以上の入力に対する通常実行は変数normal_execution_sentenceにテキストとして書き出されるので
        それを見ることで確認することができる
        """
        


    if problem==1:
        loop_suo = di.for_loop("i",range(n))
        loop_l1 = di.for_loop("l1","range((2*i+1))")
        loop_l2 = di.for_loop("l2","range((2*i+1))")
        """
        次のように書けば演算子部分にmax,minは使うことができる
        ただしdecが空集合になるときのみ成功する
        """
        assignment_1=di.assignment(["l1","l2"],"ans[i]=max(ans[i], b[l1][l2])","max")
        expression_list=[loop_l1,loop_l2,assignment_1]
        inc_coefficient=[1]
        dec_coefficient=[1]

    if problem==2:
        loop_suo = di.for_loop("i",range(n))
        loop_l1 = di.for_loop("l1","range((i+1))")
        loop_l2 = di.for_loop("l2","range((100))")
        assignment_1=di.assignment(["l1","l2"],"ans[i]+=b[l1][l2]","+")
        expression_list=[loop_l1,loop_l2,assignment_1]
        inc_coefficient=[1]
        dec_coefficient=[-1]

    if problem==3:
        loop_suo = di.for_loop("i",range(n))
        loop_l1 = di.for_loop("l1","range(i,(i+30))")
        loop_l2 = di.for_loop("l2","range((100))")
        """
        *を使う時の0除算エラー対策はしていない
        """
        assignment_1=di.assignment(["l1","l2"],"ans[i]*=b[l1][l2]","*")
        expression_list=[loop_l1,loop_l2,assignment_1]
        inc_coefficient=[1]
        dec_coefficient=[1]
        
    if problem==4:
        loop_suo = di.for_loop("i",range(n))
        loop_l1 = di.for_loop("l1","range((100))")
        loop_l2 = di.for_loop("l2","range((100))")
        assignment_1=di.assignment(["l1+i","l2"],"ans[i]+=b[l1+i][l2]","+")
        expression_list=[loop_l1,loop_l2,assignment_1]
        inc_coefficient=[1]
        dec_coefficient=[-1]
        
    if problem==6:
        loop_suo = di.for_loop("i",range(n))
        loop_l1 = di.for_loop("l1","range(-i+1000,i+1001)")
        loop_l2 = di.for_loop("l2","range(-i+1000,i+1001)")
        assignment_1=di.assignment(["l1","l2"],"ans[i]+=b[l1][l2]","+")
        expression_list=[loop_l1,loop_l2,assignment_1]
        inc_coefficient=[1,1]
        dec_coefficient=[1,1]
        
    if problem==7:
        loop_suo = di.for_loop("i",range(n))
        loop_l1 = di.for_loop("l1","range(0,i+1)")
        assignment_1=di.assignment(["l1","0"],"ans[i]+=b[l1][0]","+")
        expression_list=[loop_l1,assignment_1]
        inc_coefficient=[1]
        dec_coefficient=[-1]        
        
    
    if problem==8:
        loop_suo = di.for_loop("i",range(n))
        loop_l1 = di.for_loop("l1","range((i+1))")
        loop_l2 = di.for_loop("l2","range((i+1))")
        assignment_1=di.assignment(["l1","l2"],"ans[i]+=2*b[l1][l2]","+")
        assignment_2=di.assignment(["l1+1","l2+1"],"ans[i]+=3*b[l1+1][l2+1]","+")
        expression_list=[loop_l1,loop_l2,assignment_1,assignment_2]
        """
        2個の代入文が出てきたらinc_coefficient,dec_coefficientに2個の式の係数に対応するように2個書く
        2個以上の代入文があるとき、演算子が2種類以上になる実装には対応していない(この場合は2個とも"+"なのでOK)
        """
        inc_coefficient=[2,3]
        dec_coefficient=[-2,-3]


    if problem==9:
        b=[[random.randint(-2000, 2000) for i in range(1)] for j in range(2000)] 
        loop_suo = di.for_loop("i",range(n))
        loop_l1 = di.for_loop("l1","range((1))")
        assignment_1=di.assignment(["i","0"],"ans[i]+=2*b[i][0]","+")
        assignment_2=di.assignment(["i+1","0"],"ans[i]+=3*b[i+1][0]","+")
        assignment_3=di.assignment(["i+2","0"],"ans[i]+=2*b[i+2][0]","+")
        expression_list=[loop_l1,assignment_1,assignment_2,assignment_3]
        inc_coefficient=[2,3,2]
        dec_coefficient=[-2,-3,-2]
        
    if problem==10:
        loop_suo = di.for_loop("i",range(n))
        loop_l1 = di.for_loop("l1","range(i,i+1)")
        loop_l2 = di.for_loop("l2","range(i,i+1)")
        assignment_1=di.assignment(["l1","l2"],"ans[i]+=1*b[l1][l2]","+")
        assignment_2=di.assignment(["l1+1","l2"],"ans[i]+=-1*b[l1+1][l2]","+")
        assignment_3=di.assignment(["l1","l2+1"],"ans[i]+=1*b[l1][l2+1]","+")
        assignment_4=di.assignment(["l1+1","l2+1"],"ans[i]+=-1*b[l1+1][l2+1]","+")
        expression_list=[loop_l1,loop_l2,assignment_1,assignment_2,assignment_3,assignment_4]
        
        inc_coefficient=[1,-1,1,-1]
        dec_coefficient=[-1,1,-1,1]
    
        
        """
問題例終わり
"""





    """
    入力から通常実行コードを書き出して実行
    """
    ###############################################
    normal_execution_sentence=di.normal_execution(loop_suo,expression_list)
    t1 = time.time() 
    exec(normal_execution_sentence)
    t2 = time.time()
    elapsed_time = t2-t1
    print(f"直接的な実行での経過時間：{elapsed_time}秒")
    print("通常実行のコード：")
    print(normal_execution_sentence)
    ###############################################
    


    """
    ここから漸増化を行って計算
    """

    t1 = time.time() #実行時間計測開始
    incrementalized_ans=[0] #incrementalizationの結果はinc_ansに格納する。これがansと一致すれば正しい計算ができている。
    expression_inc_all=[]
    expression_dec_all=[]
    
    
    
    for expression in expression_list:
        if type(expression)==di.assignment:
            
            sentences_inc_list=[]
            sentences_dec_list=[]
            sample_number=5 #この回数だけ列挙する
            
            
            """
            具体的にinc,decを求めるパート
            origにインデックスを格納して、origの差計算でinc,decを求める
            """
            orig=[[] for i in range(n+10)]
            dec=[[] for i in range(n+10)]
            inc=[[] for i in range(n+10)]
            
            """
            sの実行でinc,decを具体的に求める
            """
            s="for i in range(0,sample_number):"+"\n"
            indent_n=1
            for i in expression_list:
                if type(i)==di.for_loop:
                    s+=("    "*indent_n)+di.make_loop(i)
                    indent_n+=1
                
            s+=("    ")*indent_n+di.make_index_append(expression.index_list)+"\n"*2
            s+=("    ")*1+"if i>0:"
            s+="\n"+"    "*2+"inc[i]=di.make_Difference_set(orig[i],orig[i-1])"
            s+="\n"+"    "*2+"dec[i]=di.make_Difference_set(orig[i-1],orig[i])"
            exec(s)
            
            """
            ここから分割パート
            dec2,3とinc2,3を分割
            """
            for i in range(2,4):
                print("\ninc",i,"を分割します"+"\n")
                tmp=di.devide_index(inc[i].copy())
                if tmp!=None:
                    sentences_inc_list.append(tmp)
                
                print("\ndec",i,"を分割します"+"\n")
                tmp=di.devide_index(dec[i].copy())
                if tmp!=None:    
                    sentences_dec_list.append(tmp)
                    
            expression_inc_all.append(sentences_inc_list)
            expression_dec_all.append(sentences_dec_list)
                
        
    """
    今まで得た情報をoutput_codeに渡して漸増化コードを書き出してもらう
    operatorはassignment_1.operatorで使う一種類のものしか受け付けない実装なので、注意
    """
    program=di.output_code(expression_inc_all,expression_dec_all,2,n,ans[0],True,inc_coefficient,dec_coefficient,assignment_1.operator)
    exec(program)
    ###############################################
    t2 = time.time()
    print("生成コード：")
    print(program)
    elapsed_time = t2-t1
    print(f"漸増化した実行での経過時間：{elapsed_time}秒")
    ################################################
    print("漸増化コードと通常実行の結果一致：",ans==inc_ans)
        
