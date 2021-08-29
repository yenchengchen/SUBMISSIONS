#!/bin/bash

touch answers.txt
mkdir s1
mkdir ./s1/s3
mkdir ./s1/s2
touch ./s1/s3/conf.txt
touch ./s1/s2/text_chunk1.txt
mkdir ./s1/s2/Advanced
touch ./s1/s2/Advanced/text_chunk2.txt
echo "Virtual (conda) environments are my favorite new technology" >> ./s1/s3/conf.txt
echo "Virtual environments are good for my mental health." >> ./s1/s2/text_chunk1.txt 
cat ./s1/s2/text_chunk1.txt > ./s1/s2/Advanced/text_chunk2.txt 
echo "I like them because it helps my brain do exercise everyday" >> ./s1/s2/Advanced/text_chunk2.txt 
cat ./make_tree.sh > ./answers.txt