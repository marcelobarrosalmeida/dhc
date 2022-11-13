#!/usr/bin/python3
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
    plt.xlabel('Diferença Máxima')
    plt.ylabel('Taxa de Comptactação [%]')
    plt.title('Compactação Estimada do DHC')
    plt.xticks(list(range(0,1900,100)))
    plt.grid()
    #plt.errorbar(stds, avg_var, std_var, linestyle='-', marker='^')
    plt.show()


    plt.plot(minmaxs, avg_var, label='Ordem original',linewidth=2, markersize=4, marker='o')
    plt.plot(minmaxs, avg_var_map, label='Ordem via histograma', linewidth=2, markersize=4, marker='x')
    plt.xlabel('Diferença Máxima')
    plt.ylabel('Taxa de Comptactação [%]')
    plt.title('Eficiência da Compactação com Mapeamento')
    plt.xticks(list(range(0,1900,100)))
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

if __name__ == '__main__':
    input_data_sample_lin(data_range=100)
    eval_minmax()

