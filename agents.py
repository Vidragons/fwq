"""
智能扫地机器人
假设在50*50单位的空地有若干个垃圾
设0为无垃圾，1为有垃圾
输入垃圾的个数，并随机分配
经过循环找出垃圾总数
"""
import random
import copy
class Map:
    
    def mapinit(self):
        """初始化地图，并将所有单位都赋值为0，即无垃圾状态"""
        item_2=[]
        item_1=[]
        i=0
        while i<50:
            i=i+1
            num=0
            item_1.append(num)
            item_2.append(item_1)
            """利用列表模拟地图，item_2成为地图"""
        return item_2
        
    def setting(self,item_2):
        """初始化垃圾个数，并随机分布"""
        min=0
        max=49
        n=0
        m=0
        ylist=[]
        item_3=[]
        item=[]
        """将出现的y形成列表"""
        judge=[]
        """中间的过度的列表"""
        rubbish=input("请设定垃圾的个数，并随机分配")
        rubbish=int(rubbish)
        while n < rubbish:
            item=[0,0,0,0,0,0,0,0,0,0,
                  0,0,0,0,0,0,0,0,0,0,
                  0,0,0,0,0,0,0,0,0,0,
                  0,0,0,0,0,0,0,0,0,0,
                  0,0,0,0,0,0,0,0,0,0]
            """每一次循环都初始化item"""
            x=random.randint(min,max)
            y=random.randint(min,max)
            """利用随机函数将x,y赋值"""
            print("坐标为("+str(x+1)+","+str(y+1)+")")
            """打印坐标"""
                
            n=n+1
            if y in ylist:
                """y不是第一次出现"""
                judge=item_2[y]
                if judge[x]==1:
                    rubbish=rubbish+1
                    """即随机函数的值重复了,循环+1"""
                    continue
                else:
                    judge[x]=1
                    item_2[y]=judge
                    judge=[0,0,0,0,0,0,0,0,0,0,
                           0,0,0,0,0,0,0,0,0,0,
                           0,0,0,0,0,0,0,0,0,0,
                           0,0,0,0,0,0,0,0,0,0,
                           0,0,0,0,0,0,0,0,0,0]
                           
            else:
                item[x]=1
                item_2[y]=item
                
            ylist.append(y)
            """出现的y添加到列表中"""

        while m<50:
            print(item_2[m])
            m=m+1
            """打印整齐的item_2以便观察"""

        item_3=item_2
        return item_3
        
    

    def cycle(self,item_3):
        """循环函数，将整个列表循环一遍查看有无垃圾"""
        item=[]
        i=0
        rubbish=0
        """初始化为0"""
        while i<50:
            """分两部分循环，当i为偶数的时候顺序查询，反之逆序查询"""
            item=item_3[i]
            n=49
            j=0
            while j<50:
    
                if i%2==0:
                    """偶数顺序查询"""
                    if item[j]==1:
                        rubbish=rubbish+1  
                        """找到垃圾后，rubbish+1"""
                        
                else:
                    while n>=0:
                        """奇数逆序查询"""
                        if item[n]==1:
                            rubbish=rubbish+1
                            """找到垃圾后，rubbish+1"""
                        n=n-1
                        
                j=j+1
            i=i+1
        print("找到的垃圾数目为"+str(rubbish))
            
    




