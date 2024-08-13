import random
import networkx as nx
import matplotlib.pyplot as plt
fh=list()
f=list()
fname = input("Enter file name: ")
num_generations = int(input("Enter number of generqtions:"))
p_crossover = float(input("Enter p_crossover:"))
p_mutation = float(input("Enter p_mutation:"))
fh = open(fname).read()
f=open(fname).readlines()
last_line=open(fname).readlines()[-1]
lst = list()
#lst=fh.read().split()
lst=fh.split()
final_list=list()
for line in lst:
    if line not in final_list:
        final_list.append(line)

final_list.sort()
print(final_list)
G_asymmetric = nx.DiGraph()
for i, w in enumerate(final_list):
        G_asymmetric.add_node(final_list[i])
f1=len(final_list)
print(f1)
for count, line in enumerate(f):
    pass
count=count+1
print("total",count )

def before(value, a):
    pos_a = value.find(a)
    if pos_a == -1: return ""
    return value[0:pos_a]

def after(value, a):
    pos_a = value.rfind(a)
    if pos_a == -1: return ""
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= len(value): return ""
    return value[adjusted_pos_a:]

def common_member(a,b):
    a_set=set(a)
    b_set=set(b)
    if len(a_set.intersection(b_set))>0:
        return (a_set.intersection(b_set))

def selection():
    fit_list = []
    global selected
    selected = []
    r = 0
    fitness_sum = sum(lyekdasti[fit] for fit in range(0, 10))
    for i in range(10):
        x = (lyekdasti[i] * 100) / fitness_sum + 1
        fit_list.append(x)

    fit_list_sum = round(sum(fit_list[i] for i in range(0, 10)))
    j = 0
    while j != 10:
        ps = random.randint(1, fit_list_sum - 2)
        for x in range(0, 10):
            r = round(fit_list[x]) + r
            if ps <= r:
                selected.append(population[x])
                r = 0
                break
        j = j + 1

    print(selected)
    return selected

def convert():
    global l_list
    l_list = []
    for bb in selected:
        bbb={}
        for key, value in bb.items():
            bbb[key] =value
        #print(bbb)
        list=[(k,v) for k,v in bbb.items()]
        l_list.append(list)
        mn=len(l_list)
        if mn==10:
            print(l_list)
            return l_list

def crossover():
    p = p_crossover
    p1 = l_list[0:2]
    p2 = l_list[2:4]
    p3 = l_list[4:6]
    p4 = l_list[6:8]
    p5 = l_list[8:10]
    del l_list[0:]

    r1 = random.random()
    if r1 < p:
        cut_a = random.randint(0, len(w1))
        a = p1[0][cut_a:]
        b = p1[1][cut_a:]
        p1[0][cut_a:] = b
        p1[1][cut_a:] = a

    r2 = random.random()
    if r2 < p:
        cut_b = random.randint(0, len(w1))
        c = p2[0][cut_b:]
        d = p2[1][cut_b:]
        p2[0][cut_b:] = d
        p2[1][cut_b:] = c

    r3 = random.random()
    if r3 < p:
        cut_a = random.randint(0, len(w1))
        a1 = p3[0][cut_a:]
        b1 = p3[1][cut_a:]
        p3[0][cut_a:] = b1
        p3[1][cut_a:] = a1

    r4 = random.random()
    if r4 < p:
        cut_b = random.randint(0, len(w1))
        c1 = p4[0][cut_b:]
        d1 = p4[1][cut_b:]
        p4[0][cut_b:] = d1
        p4[1][cut_b:] = c1

    r5 = random.random()
    if r5 < p:
        cut_a = random.randint(0, len(w1))
        a2 = p5[0][cut_a:]
        b2 = p5[1][cut_a:]
        p5[0][cut_a:] = b2
        p5[1][cut_a:] = a2

    l_list.extend(p1)
    l_list.extend(p2)
    l_list.extend(p3)
    l_list.extend(p4)
    l_list.extend(p5)
    print(l_list)
    return l_list

def convert1():
    global ll_list
    global lll_list
    ll_list = []
    lll_list = []
    for bbb in l_list:
        s1=[item[0] for item in bbb]
        s2=[item[1] for item in bbb]
        ll_list.append(s1)
        lll_list.append(s2)
        mn1 = len(ll_list)
        if mn1 == 10:
            print(ll_list)
            print(lll_list)
            return lll_list

def mutation():
    p = p_mutation
    global new_generation
    global change_color
    for i in range(0, 10):
        r = random.random()
        if r < p:
            mutate_point = random.randint(0, round((f1 / 2) - 1))
            change_color = random.randint(1, round(f1 / 2))
            while change_color == lll_list[i][mutate_point]:
                change_color = random.randint(1, round(f1/2))
            lll_list[i][mutate_point]= change_color
            change_color = 0
            continue
        else:
            pass
    new_generation = lll_list[:]
    print(new_generation)
    return new_generation

def convert2():
    global l1_list
    l1_list = []
    for o1 in ll_list:
        for o2 in new_generation:
            merged_list = [(o1[i], o2[i]) for i in range(0, len(o1))]
            l1_list.append(merged_list)
        print(l1_list)
        return l1_list


def yt(res6):
    m = 0
    ini=0
    outi=0
    pin=0
    pout=0
    yy1=0
    yy2=0
    yekdasti=0
    tozishodegi=0
    a1 = len(res6)
    for value in res6.values():
        for j in range(count):
                if (before_word[j] in value) and (after_word[j] not in value):
                    outi += 1
                    if outi != 0:
                        pout += 1
                if (before_word[j] not in value) and (after_word[j] in value):
                    ini += 1
                    if ini != 0:
                        pin += 1
                    if ini != 0 and outi != 0:
                        m += 1
        for before_word[j] in value:
            yy1=(outi * (outi + 1)) / 2
        for after_word[j] in value:
            yy2=(ini * (ini + 1)) / 2
    yekdasti = (yy1+yy2)/a1
    tozishodegi =(yy1+yy2)/((pin + pout) - m)
    print("yekdasti:", yekdasti)
    print("tozishodegi:", tozishodegi)

def convert8():
    global l3_list
    l3_list = []
    global l4_list
    l4_list = []
    fg = []
    mi = 0
    ini = 0
    outi = 0
    turbo = 0
    t1=0
    for m in ll_list:
        for n in new_generation:
            res2 = {m[i]: n[i] for i, _ in enumerate(m)}
            l3_list.append(res2)
            mn1 = len(l3_list)
            if mn1 == 10:
                print(l3_list)
                for list in l3_list:
                    res5 = {}
                    for key, value in list.items():
                        if value not in res5:
                            res5[value] = [key]
                        else:
                            res5[value].append(key)
                    l4_list.append(res5)
                    print(res5)
                    for value in res5.values():
                        for j in range(count):
                            if (before_word[j] in value) and (after_word[j] in value):
                                mi += 1
                            if (before_word[j] in value) and (after_word[j] not in value):
                                outi += 1
                            if (before_word[j] not in value) and (after_word[j] in value):
                                ini += 1
                        turbo +=((mi) /(2*((2 * mi) + (ini + outi))))
                    fg.append(turbo)
                    if len(fg) == 10:
                        best_fit_value = max(fg)
                        print("turbo:", best_fit_value)
                        best_fit_index = fg.index(best_fit_value)
                        final = l3_list[best_fit_index]
                        print(final)
                        res6 = {}
                        for key, value in final.items():
                            if value not in res6:
                                res6[value] = [key]
                            else:
                                res6[value].append(key)
                        print(res6)
                        a1 = len(res6)
                        yt(res6)
                        uuuu = []
                        for value in res6.values():
                            uuuu.append(value)
                            mn11 = len(uuuu)
                            node_list = []
                            if mn11 == a1:
                                print(uuuu)
                                print(len(uuuu))
                                if n_generations == num_generations:
                                    for list_i in uuuu:
                                        node_colors = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
                                        for node in common_member(list_i, G_asymmetric.nodes()):
                                            node_list.append(node)
                                            G_asymmetric.nodes[node]['color'] = node_colors[0]
                                    nx.draw_networkx(G_asymmetric, nodelist=node_list,node_color=[G_asymmetric.nodes[node]['color'] for node in node_list])
                                    plt.show()
p1=[]
p2=[]
yekdasti=0
tozishodegi=0
lyekdasti=[]
p=[]
ini = 0
outi = 0
pin=0
pout=0
before_word = []
after_word = []
w=list()
m=0
mi=0
turbo=0
for line in f:
        p1 = before(line, " ")
        before_word.append(p1)
        p2 = after(line, " ")
        after_word.append(p2[:-1])
        #print("%s >>>> %s " % (before_word,after_word))
        if line == last_line:
            global population
            global chromosome
            population = []
            n_generations = 0
            for k in range(10):
                    w1 = {final_list[i]: random.randint(1, round(f1 / 2)) for i in range(len(final_list))}
                    population.append(w1)
                    if len(population)==10:
                        print(population)
                    nn = len(population)
                    for list in population:
                        res = {}
                        for key, value in list.items():
                            if value not in res:
                                res[value] = [key]
                            else:
                                res[value].append(key)
                        # print(res)
                        a = len(res)
                        mmm = res.values()
                        nnn = res.keys()
                        result_list = [res[x] for x in nnn]
                        if nn == 10:
                            for value in res.values():
                                for j in range(count):
                                    G_asymmetric.add_edge(before_word[j], after_word[j])
                                    if (before_word[j] in value) and (after_word[j] in value):
                                        mi += 1
                                    if (before_word[j] in value) and (after_word[j] not in value):
                                        outi += 1
                                        if outi != 0:
                                            pout += 1
                                    if (before_word[j] not in value) and (after_word[j] in value):
                                        ini += 1
                                        if ini != 0:
                                            pin += 1
                                        if ini != 0 and outi != 0:
                                            m += 1
                                turbo += ((2 * mi) / (2 * mi + (ini + outi)))
                            yy1 = (outi * (outi + 1)) / 2
                            yy2 = (ini * (ini + 1)) / 2
                            yekdasti = (yy1 + yy2) / a
                            tozishodegi = (yy1 + yy2) / ((pin + pout) - m)
                            yektozi = yekdasti + tozishodegi + turbo
                            lyekdasti.append(yektozi)
                            if len(lyekdasti) == 10:
                                nx.spring_layout(G_asymmetric)
                                nx.draw_networkx(G_asymmetric)
                                plt.show()
                                while n_generations <= num_generations:
                                    selection()
                                    convert()
                                    crossover()
                                    convert1()
                                    mutation()
                                    convert2()
                                    convert8()
                                    n_generations = n_generations + 1
                                    print('generation', n_generations)