import math
import random

C = 540  # 最大适应度
LEN = 140  # 基因长度
maxGene = []
maxi = 0  # 最大值最初出现的进化代数
findAim = False
POPMAX = 32  # 种群数量
P_XOVER = 0.8  # 交叉概率
P_MUTATION = 0.15  # 变异概率
MAXGENERATIONS = 1000  # 总的进化代数./1
goal = [2, 8, 3, 7, 1, 4, 0, 6, 5]  # 目标状态
initiate = [2, 8, 3, 1, 0, 4, 7, 6, 5]  # 初始状态
# initiate = [1,0,2,3,4,5,6,7,8]
# goal=[0,1,2,3,4,5,6,7,8]
pop = []  # 种群所有对象


class Gene:
    def __init__(self, gene):
        self.gene = gene  # 基因，数组
        self.fitness = 0
        self.rf = 0  # 选择的概率
        self.cf = 0  # 累积的概率


# 随机初始化基因组
def initGenes():
    count = 0
    maxFit = 100  # 随机生成的基因适应度的最大值
    while (count < POPMAX):
        tmp = []
        for j in range(LEN):
            pow = round(random.random() * 3)  # 随机生成0上，1下, 2左, 3右
            tmp.append(pow)

        pop.append(Gene(tmp))
        count += 1


# 上下左右操作
def move(current, dire):
    space = 0  # 空格位置
    block = 0  # 移动的格子的位置
    for i in range(len(current)):
        if (current[i] == 0):
            space = i
            block = space
            break

    if (dire == 0):
        if (space - 3 >= 0):
            block = space - 3

    elif (dire == 1 and (space + 3 < 9)):
        block = space + 3
    elif (dire == 2):
        if (space % 3 > 0):
            block = space - 1

    elif (dire == 3):
        if (space % 3 < 2):
            block = space + 1

    current[space], current[block] = current[block], current[space]
    if (space == block):
        return False
    else:
        return True


# 计算适应度
def fitness(current):
    f = 0
    for i in range(len(current)):
        if (current[i] == goal[i]):
            f += 100 - current[i] * 10
    return f


def envaluateFitness(maxi):  # max参数只是用来记录进化代数
    totalFitness = 0
    for i in range(POPMAX):
        s0 = initiate[:]  # 每一步移动后的状态
        pop[i].fitness = 0
        for j in range(LEN):
            # 每移动一次后计算一次适应度函数，若为540说明已找到解
            move(s0, pop[i].gene[j])
            pop[i].fitness = fitness(s0)
            if (pop[i].fitness == C):
                global findAim
                findAim = True
                global maxGene
                maxGene = pop[i].gene[0:j + 1]
                return totalFitness

        if (pop[i].fitness == 0):
            pop[i].fitness = 1

        totalFitness += pop[i].fitness

    return totalFitness


# 适应度更高的基因有更高的概率往下遗传
def selectBetter(totalFitness):  # 轮盘赌选择
    lastCf = 0
    newPop = [None for i in range(POPMAX)]
    global pop
    for i in range(POPMAX):  # 计算个体选择概率和累积概率
        pop[i].rf = pop[i].fitness / totalFitness
        pop[i].cf = lastCf + pop[i].rf
        lastCf = pop[i].cf

    for i in range(POPMAX):  # 轮盘赌式选择
        p = random.random()
        if (p < pop[0].cf):
            newPop[i] = Gene(pop[0].gene)
            # newPop.append(Gene(pop[0].gene))
        else:
            for j in range(POPMAX - 1):
                if (p >= pop[j].cf and p < pop[j + 1].cf):
                    newPop[i] = Gene(pop[j + 1].gene)
                    # newPop.append(Gene(pop[j+1].gene))
                    break

    if (len(newPop) == 0):
        # console.log(pop)
        print(pop)
    import copy
    pop = copy.deepcopy(newPop)


def exChgOver(first, second):  # 基因交换函数
    ecc = round(random.random() * LEN)
    for i in range(int(ecc)):
        index = math.floor(random.random() * LEN)
        pop[first].gene[index], pop[second].gene[index] = pop[second].gene[index], pop[first].gene[index]


# 交叉
def crossover():
    first = -1
    for i in range(POPMAX):
        p = random.random()
        if (p < P_XOVER):
            if (first < 0):
                first = i
            else:  # 选择了两个随机个体，进行基因交换
                exChgOver(first, i)
                first = -1


def reverseGene(index):  # 变异操作函数
    mcc = round(random.random() * LEN)
    for i in range(int(mcc)):
        gi = math.floor(random.random() * LEN)
        pop[index].gene[gi] = 3 - pop[index].gene[gi]


# 变异
def mutation():
    for i in range(POPMAX):
        p = random.random()
        if (p < P_MUTATION):  # 只有当随机数小于变异概率才进行变异操作
            reverseGene(i)


initGenes()
f = envaluateFitness(0)
for i in range(MAXGENERATIONS):
    selectBetter(f)
    crossover()
    mutation()
    f = envaluateFitness(i)
    if (findAim):
        break


# console.log(maxGene);

def transform(gene):
    s0 = initiate[:]
    options = []
    for i in range(len(gene)):
        if (move(s0, gene[i])):
            if (gene[i] == 0):
                options.append('上')
            elif (gene[i] == 1):
                options.append('下')
            elif (gene[i] == 2):
                options.append('左')
            elif (gene[i] == 3):
                options.append('右')

    print(options)
    print(s0)


transform(maxGene)

# let m = maxGene
# let s0 = initiate.slice(0)
# for (let i = 0; i< m.length; i++) {
#     move(s0, m[i])
# }
# console.log(s0)
