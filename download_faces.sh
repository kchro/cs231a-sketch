#!/bin/sh
echo 'mac only'
curl -o faces.mp4 https://instagram.fsea1-1.fna.fbcdn.net/vp/0bc1f14b61f19cf6f6db5df5af82daf1/5AAEC33A/t50.2886-16/18673652_437436553287430_1041814007784144896_n.mp4
python generate_faces.py
