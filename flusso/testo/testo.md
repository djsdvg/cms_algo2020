###cc Primo stage (Volterra) - Allenamento primo stage
# Algoritmo di massimo flusso

## Descrizione del problema

Si calcoli il massimo flusso tra i nodi `S`
e `E` in un grafo pesato orientato avente `N`
nodi e `M` archi.


## Input

Il file `input.txt` contiene sulla prima
riga `N` e `M`, separati da uno spazio, e
sulla seconda riga `S` e `E`, separati da uno
spazio. Le successive `M` righe contengono tre numeri
interi positivi, `u`, `v` e `w`, che
rappresentano un arco di peso `w` che collega i
nodi `u` e `v`.


## Output
Il file `output.txt` contiene un'unica riga. In
questa riga deve essere presente il flusso massimo ottenibile.


## assunzioni
- $1 \le; N \le; 10000$
- $2 \le; M \le; 1000000$
- $1 \le; W_i < ; 2^{31}$
- Il flusso massimo è sicuramente $< 2^{31}$
</assunzioni>

## Esempio

|input from stdin | output to stdout |
|------|--------|
|6 8
5 2
1 2 734
2 6 497
3 5 926
4 3 882
5 4 9
5 6 74
5 1 257
6 4 491| 257 |


## Nota
Tutti gli interi sono 1-based.


