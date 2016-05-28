#!/usr/bin/env bash
sort ${1:-output_ex045.txt} | uniq -c | sort -r
