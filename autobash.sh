#!/bin/bash
loops=$(python3 -c "for i in range(1,22,1):print(i/10)")
echo $loops
for i in $loops;do
	#echo "python3 index.py $i"
	python3 index.py $i
done

