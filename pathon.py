
const = 100
w = 0
h = 0
a = np.array([cx, cy])
while w < x:
    wcx = cx + w * const
    
    if x < w :
        break
    
    while h < y:
        hcy = cy + h * const
        
        if y < h :
            break
        
        #ユークリッド距離算出
        b = np.array([wcx, hcy])
        l = np.linalg.norm(b-a)
        eDlist.append(l)
        rawlist.append(img[hcy][wcx])
        y+=1
    else:
        print("end y")
        
    
else:
    print("end x")

#削除
#中心点を求める
#y,x = img.shape
#cx = x//2
#cy = y//2

#中心からの対角線長
diagonalSize = np.sqrt(cy**2 + cx**2)

# ユークリッド距離,rawデータ　Euclidean distance
eDlist = []

const = 100
        
#forが使いにくい。。。
for w in range(cx):
    wcx = cx + w * const
    if wcx >= x :
        break
    for h in range(cy):
        hcy = cy + h * const
        if hcy >= y :
            break
        #ユークリッド距離算出
        a = np.array([cx, cy])
        b = np.array([wcx, hcy])
        l = np.linalg.norm(b-a)
        #eDlist.append([float(l)/float(diagonalSize),float(img[hcy][wcx])])
        eDlist.append([float(l)/float(diagonalSize),float(img[hcy][wcx])/img[cy][cx]])

# 行列Xの作成
#X = np.column_stack(np.repeat(1, len(rawlist), numpy.array(rawlist), numpy.array(rawlist)**2)

#ソート
eDlist.sort(key=lambda x:x[0])
i = 0
xList = []
yList = []
for i in range(len(eDlist)-1) :
    xList.append(eDlist[i][0])
    yList.append(eDlist[i][1])

# 行列Xの作成
#X = np.column_stack(np.repeat(1, len(xList)))

plt.figure() 
plt.plot(np.array(yList),np.array(xList),".")
from scipy import optimize as opt

def fit_func(x, a, b, c, d): 
    return a * x**3 + b * x**2 + c * x + d 
res = opt.curve_fit(fit_func, np.array(xList), np.array(yList))

a = res[0][0] 
b = res[0][1] 
c = res[0][2] 
d = res[0][3] 
Px2 = [] 
for x in np.array(xList): 
    Px2.append(a * x**3 + b * x**2 + c * x + d) 
plt.plot(np.array(Px2),np.array(xList))

#回帰曲線
#model = sm.OLS(np.array(yList),np.array(xList))
#results = model.fit()
# 結果の概要を表示
#print(results.summary())
#a,b= results.params
#plt.plot(np.array(rawlist), a*np.array(rawlist))