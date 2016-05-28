#!/usr/bin/env bash
sort ${2:-output_ex045.txt} | grep "^""${1:-する}""\t" | uniq -c | sort -r
