"""
An implementation of Delta/Huffman Compressor (DHC) for embedded systems.

Copyright (c) 2022 
Marcelo Barros de Almeida <marcelobarrosalmeida@gmail.com>
Marden Fagundes <maf_cadastro-github@yahoo.com>
"""

from ctypes import *
from random import randint
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

import dhc

DHC_MAX_BITS   = 16
DHC_TABLE_SIZE = (DHC_MAX_BITS+1)

dhc_lib_file = './dhc_lib.so'
dhc_functions = CDLL(dhc_lib_file)

def eval_std():
    input_size = 1000
    avg = 0
    nrep = 10
    stds = list(range(1,10,1)) + list(range(10,100,5)) + list(range(100,900,100))
    map = [0]*DHC_TABLE_SIZE
    avg_var = []
    std_var = []
    avg_var_map = []
    std_var_map = []

    for std in stds:
        var = []
        var_map = []
        for n in range(nrep):
            input = np.random.normal(loc=avg, scale=std, size=input_size)
            input = [ int(x) for x in input ]
            (ratio,compressed_size_bits) = dhc.compress_evaluate(input,input_size)
            var.append(ratio)
            map = [0]*DHC_TABLE_SIZE
            (ratio,compressed_size_bits) = dhc.compress_evaluate(input,input_size,map)
            var_map.append(ratio)
        avg_var.append(np.mean(var))
        std_var.append(np.std(var))
        avg_var_map.append(np.mean(var_map))
        std_var_map.append(np.std(var_map))

        print(f'{std} {np.mean(var):2.2f}/{np.std(var):2.2f}  {np.mean(var_map):2.2f}/{np.std(var_map):2.2f}')
    
    input = np.random.normal(loc=avg, scale=20, size=5000)
    counts, bins = np.histogram(input,bins=20)
    plt.stairs(counts, bins)
    plt.grid()
    plt.show()

    plt.plot(stds, avg_var, linewidth=2, markersize=4, marker='o')
    plt.xlabel('Desvio Padrão')
    plt.ylabel('Taxa de Comptactação [%]')
    plt.title('Eficiência da Compactação (Média=0)')
    plt.grid()
    #plt.errorbar(stds, avg_var, std_var, linestyle='-', marker='^')
    plt.show()

    input = np.random.normal(loc=avg, scale=500, size=5000)
    counts, bins = np.histogram(input,bins=20)
    plt.stairs(counts, bins)
    plt.grid()
    plt.show()

    plt.plot(stds, avg_var, linewidth=2, markersize=4, marker='o')
    plt.plot(stds, avg_var_map, linewidth=2, markersize=4, marker='x')
    plt.xlabel('Desvio Padrão')
    plt.ylabel('Taxa de Comptactação [%]')
    plt.title('Eficiência da Compactação com Mapeamento (Média=0)')
    plt.grid()
    #plt.errorbar(stds, avg_var, std_var, linestyle='-', marker='^')
    plt.show()

def eval_avg():
    input_size = 1000
    std = 10
    nrep = 50
    avgs = list(range(1,10,1)) + list(range(10,100,5)) + list(range(100,900,100))
    map = [0]*DHC_TABLE_SIZE
    avg_var = []
    std_var = []
    avg_var_map = []
    std_var_map = []

    for avg in avgs:
        var = []
        var_map = []
        for n in range(nrep):
            input = np.random.normal(loc=avg, scale=std, size=input_size)
            input = [ int(x) for x in input ]
            (ratio,compressed_size_bits) = dhc.compress_evaluate(input,input_size)
            var.append(ratio)
            map = [0]*DHC_TABLE_SIZE
            (ratio,compressed_size_bits) = dhc.compress_evaluate(input,input_size,map)
            var_map.append(ratio)
        avg_var.append(np.mean(var))
        std_var.append(np.std(var))
        avg_var_map.append(np.mean(var_map))
        std_var_map.append(np.std(var_map))

        print(f'{std} {np.mean(var):2.2f}/{np.std(var):2.2f}  {np.mean(var_map):2.2f}/{np.std(var_map):2.2f}')
    
    input = np.random.normal(loc=avg, scale=20, size=5000)
    counts, bins = np.histogram(input,bins=20)
    plt.stairs(counts, bins)
    plt.grid()
    plt.show()

    plt.plot(avgs, avg_var, linewidth=2, markersize=4, marker='o')
    plt.xlabel('Média')
    plt.ylabel('Taxa de Comptactação [%]')
    plt.title('Eficiência da Compactação (Média=0)')
    plt.grid()
    #plt.errorbar(stds, avg_var, std_var, linestyle='-', marker='^')
    plt.show()

    input = np.random.normal(loc=avg, scale=500, size=5000)
    counts, bins = np.histogram(input,bins=20)
    plt.stairs(counts, bins)
    plt.grid()
    plt.show()

    plt.plot(avgs, avg_var, linewidth=2, markersize=4, marker='o')
    plt.plot(avgs, avg_var_map, linewidth=2, markersize=4, marker='x')
    plt.xlabel('Média')
    plt.ylabel('Taxa de Comptactação [%]')
    plt.title('Eficiência da Compactação com Mapeamento (Média=0)')
    plt.grid()
    #plt.errorbar(stds, avg_var, std_var, linestyle='-', marker='^')
    plt.show()


def eval_minmax():
    input_size = 1000
    std = 10
    nrep = 10
    minmaxs = list(range(2,10,1)) + list(range(10,100,5)) + list(range(100,1900,100))
    map = [0]*DHC_TABLE_SIZE
    avg_var = []
    std_var = []
    avg_var_map = []
    std_var_map = []

    for minmax in minmaxs:
        var = []
        var_map = []
        for n in range(nrep):
            input = np.random.randint(low=-minmax/2, high=minmax/2, size=input_size)
            input = [ int(x) for x in input ]
            (ratio,compressed_size_bits) = dhc.compress_evaluate(input,input_size)
            var.append(ratio)
            map = [0]*DHC_TABLE_SIZE
            (ratio,compressed_size_bits) = dhc.compress_evaluate(input,input_size,map)
            var_map.append(ratio)
        avg_var.append(np.mean(var))
        std_var.append(np.std(var))
        avg_var_map.append(np.mean(var_map))
        std_var_map.append(np.std(var_map))

        print(f'{std} {np.mean(var):2.2f}/{np.std(var):2.2f}  {np.mean(var_map):2.2f}/{np.std(var_map):2.2f}')
    

    plt.plot(minmaxs, avg_var,linewidth=2, markersize=4, marker='o')
    plt.xlabel('Maximum Delta')
    plt.ylabel('Compressor Rate [%]')
    #plt.title('Estimated Compression Rate for DHC')
    #plt.xticks(list(range(0,1900,100)))
    plt.grid()
    #plt.errorbar(stds, avg_var, std_var, linestyle='-', marker='^')
    plt.show()


    plt.plot(minmaxs, avg_var, label='Ordem original',linewidth=2, markersize=4, marker='o')
    plt.plot(minmaxs, avg_var_map, label='Ordem via histograma', linewidth=2, markersize=4, marker='x')
    plt.xlabel('Diferença Máxima')
    plt.ylabel('Taxa de Comptactação [%]')
    plt.title('Eficiência da Compactação com Mapeamento')
    #plt.xticks(list(range(0,1900,100)))
    plt.grid()
    plt.legend()
    #plt.errorbar(stds, avg_var, std_var, linestyle='-', marker='^')
    plt.show()

def input_data_sample_lin(data_range=100,num_points=30):
    t = list(range(0,num_points+1))
    input = np.random.randint(low=-data_range, high=data_range, size=num_points+1)
    #input = np.add(input,t)
    input_func = interpolate.interp1d(t,input,kind='cubic')
    input_interp = input_func(np.linspace(0, num_points, num=100,endpoint=False))
    diff = np.diff(input_interp,prepend=[0])
    plt.plot(input_interp,label=f'Amostras (m={np.mean(input_interp):2.2f}, s={np.std(input_interp):2.2f})')
    plt.plot(diff,label=f'Diferenças (m={np.mean(diff):2.2f}, s={np.std(diff):2.2f})')
    plt.title(f'Variação Aleatória entre [{-data_range},{data_range}]')
    plt.legend()
    plt.grid()
    plt.show()

def input_data_sample_nor(avg=0,std=10,num_points=30):
    t = list(range(0,num_points+1))
    input = np.random.normal(loc=avg, scale=std, size=num_points+1)
    input_func = interpolate.interp1d(t,input,kind='cubic')
    input_interp = input_func(np.linspace(0, num_points, num=100,endpoint=False))
    diff = np.diff(input_interp,prepend=[0])
    plt.plot(input_interp,label=f'Amostras (m={np.mean(input_interp):2.2f}, s={np.std(input_interp):2.2f})')
    plt.plot(diff,label=f'Diferenças (m={np.mean(diff):2.2f}, s={np.std(diff):2.2f})')
    plt.title(f'Variação Aleatória [m={avg}, s={std}]')
    plt.legend()
    plt.grid()
    plt.show()

def accel():
    data ="""|1 |02g|20221114-195118|SIZE 1787 bytes|COMPRESSED RATIO 40.425            |
|2 |02g|20221114-200051|SIZE 1834 bytes|COMPRESSED RATIO 38.8375           |
|3 |02g|20221114-201051|SIZE 1824 bytes|COMPRESSED RATIO 39.170833333333334|
|4 |02g|20221114-202045|SIZE 1810 bytes|COMPRESSED RATIO 39.6375           |
|5 |02g|20221114-203014|SIZE 1861 bytes|COMPRESSED RATIO 37.9625           |
|6 |02g|20221114-203927|SIZE 1833 bytes|COMPRESSED RATIO 38.87916666666667 |
|7 |02g|20221114-204908|SIZE 1897 bytes|COMPRESSED RATIO 36.75416666666667 |
|8 |02g|20221114-205904|SIZE 1888 bytes|COMPRESSED RATIO 37.041666666666664|
|9 |02g|20221114-210834|SIZE 1814 bytes|COMPRESSED RATIO 39.53333333333333 |
|10|02g|20221114-211756|SIZE 1817 bytes|COMPRESSED RATIO 39.416666666666664|
|11|04g|20221114-213801|SIZE 1711 bytes|COMPRESSED RATIO 42.954166666666666|
|12|04g|20221114-214718|SIZE 1762 bytes|COMPRESSED RATIO 41.2625           |
|13|04g|20221114-215604|SIZE 1688 bytes|COMPRESSED RATIO 43.733333333333334|
|14|04g|20221114-220508|SIZE 1770 bytes|COMPRESSED RATIO 40.979166666666664|
|15|04g|20221114-221430|SIZE 1702 bytes|COMPRESSED RATIO 43.25416666666667 |
|16|04g|20221114-222333|SIZE 1709 bytes|COMPRESSED RATIO 43.0125           |
|17|04g|20221114-223233|SIZE 1738 bytes|COMPRESSED RATIO 42.0625           |
|18|04g|20221114-224146|SIZE 1723 bytes|COMPRESSED RATIO 42.5375           |
|19|04g|20221114-225107|SIZE 1777 bytes|COMPRESSED RATIO 40.7375           |
|20|04g|20221114-230042|SIZE 1819 bytes|COMPRESSED RATIO 39.35             |
|21|08g|20221114-231150|SIZE 1581 bytes|COMPRESSED RATIO 47.270833333333336|
|22|08g|20221114-232020|SIZE 1609 bytes|COMPRESSED RATIO 46.358333333333334|
|23|08g|20221114-232857|SIZE 1625 bytes|COMPRESSED RATIO 45.80833333333333 |
|24|08g|20221114-233726|SIZE 1630 bytes|COMPRESSED RATIO 45.65             |
|25|08g|20221114-234614|SIZE 1625 bytes|COMPRESSED RATIO 45.825            |
|26|08g|20221114-235506|SIZE 1618 bytes|COMPRESSED RATIO 46.06666666666667 |
|27|08g|20221115-000358|SIZE 1636 bytes|COMPRESSED RATIO 45.45             |
|28|08g|20221115-001238|SIZE 1598 bytes|COMPRESSED RATIO 46.733333333333334|
|29|08g|20221115-002116|SIZE 1616 bytes|COMPRESSED RATIO 46.11666666666667 |
|30|08g|20221115-003004|SIZE 1663 bytes|COMPRESSED RATIO 44.5375           |
|31|16g|20221115-003834|SIZE 1423 bytes|COMPRESSED RATIO 52.541666666666664|
|32|16g|20221115-004637|SIZE 1523 bytes|COMPRESSED RATIO 49.21666666666667 |
|33|16g|20221115-005554|SIZE 1667 bytes|COMPRESSED RATIO 44.425            |
|34|16g|20221115-010425|SIZE 1464 bytes|COMPRESSED RATIO 51.1875           |
|35|16g|20221115-011226|SIZE 1458 bytes|COMPRESSED RATIO 51.38333333333333 |
|36|16g|20221115-012046|SIZE 1506 bytes|COMPRESSED RATIO 49.775            |
|37|16g|20221115-012909|SIZE 1517 bytes|COMPRESSED RATIO 49.425            |
|38|16g|20221115-013738|SIZE 1518 bytes|COMPRESSED RATIO 49.37083333333333 |
|39|16g|20221115-014613|SIZE 1523 bytes|COMPRESSED RATIO 49.21666666666667 |
|40|16g|20221115-015436|SIZE 1496 bytes|COMPRESSED RATIO 50.12916666666667 |"""
    data = data.split('\n')
    samples = {'02g':[],'04g':[],'08g':[],'16g':[],}
    for line in data:
        fields = line.split('|')
        label = fields[2]
        size = int(fields[4].split(' ')[1])
        cr = float(fields[5].split(' ')[2])
        samples[label].append([size,cr])
    #print(samples)
    labels = ['02g','04g','08g','16g']
    y = []
    e = []
    ys = []
    es = []    
    for label in labels:
        size = [ v[0] for v in samples[label] ]
        cr = [ v[1] for v in samples[label] ]
        y.append(np.mean(cr))
        e.append(np.std(cr))
        ys.append(np.mean(size))
        es.append(np.std(size))

    labels = [ v.upper().replace('0','') for v in labels ]

    plt.grid()
    plt.errorbar(labels, y, e, linestyle='-', marker='o')
    plt.xlabel('Accelerometer  Scale')
    plt.ylabel('Compression Rate [%]')
    plt.show()

    plt.grid()
    plt.errorbar(labels, ys, es, linestyle='-', marker='o')
    plt.xlabel('Accelerometer  Scale')
    plt.ylabel('Size [Bytes]')
    plt.show()

if __name__ == '__main__':
    #input_data_sample_lin(data_range=100)
    #eval_minmax()
    accel()

