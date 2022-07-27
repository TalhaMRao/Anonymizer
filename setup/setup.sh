#!/bin/bash
conda activate py368
source ~/.virtualenvs/anonymizer/Scripts/activate
pip install -r requirements.txt
set PYTHONPATH=$PYTHONPATH:. python anonymizer/bin/anonymize.py --input C:/Users/Remote/anonymizer/images --image-output C:/Users/Remote/anonymizer/out --weights C:/Users/Remote/anonymizer/weights --no-write-detections --face-threshold=0.5 --plate-threshold=0.4 --obfuscation-kernel="45, 5, 13" --image-extensions=png,jpg
python anonymizer/bin/anonymize.py --input C:/Users/Remote/anonymizer/images --image-output C:/Users/Remote/anonymizer/out --weights C:/Users/Remote/anonymizer/weights --no-write-detections --face-threshold=0.5 --plate-threshold=0.4 --obfuscation-kernel="45, 5, 13" --image-extensions=png,jpg
wait
