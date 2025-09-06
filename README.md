
```
sudo snap install ollama
```

```
ollama pull llama3 o
```

or use below to pull quantized verison if lower memory on hardware

```
# example: pull a quantized 8B model (name may vary by registry)
ollama pull llama3:8b
```

```
ollama run llama3
```

if quantized version then
```
# then run it (or let Python trigger it)
ollama run llama3:8b
```

Entry point
```
streamlit run index.py
```


docker exec -it ollama ollama run gemma:2b

