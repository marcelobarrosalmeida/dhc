#!/bin/bash

echo "" > output.txt

for val in {1..50..1}
  do 
     #j=$((2*val))
     echo "$val/50..."
    ./app -m -$val -M $val -f 1024 -r 1000 >> output.txt
done

for val in {50..5000..100}
  do 
     #j=$((2*val))
     echo "$val/5000..."
    ./app -m -$val -M $val -f 1024 -r 1000 >> output.txt
done

for val in {5000..30000..1000}
  do 
     #j=$((2*val))
     echo "$val/30000..."
    ./app -m -$val -M $val -f 1024 -r 1000 >> output.txt
done