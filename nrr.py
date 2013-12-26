import numpy as np 

def rr(ss):
    i = 1
    for s in ss:
        if s == True:
            return 1.0 / float(i)

        else:
            i = i + 1

        
def mrr(scores):
    i = 1
    result = 0
    for score in scores:
        result  = result + rr(score)
        i = i + 1
    return result / i
        
if __name__ == '__main__':

    s = np.array([1,0,0])
    print rr(s)
    s = np.array([0,0,1])
    print rr(s)
    m = np.array([[1, 0, 0, 0, 0 ,0 ],
                  [0, 0, 1, 0, 0 ,0 ]])
    print mrr(m)
    # error input
    m = np.array([[1, 0, 0, 0, 0 ,1 ],
                  [0, 0, 1, 0, 0 ,0 ]])
    print mrr(m)
                
