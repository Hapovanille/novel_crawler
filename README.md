## Dependencies
```bash
pip3 install requirements.txt
```

## Run
```python
python3 title_fetcher.py
```

## Merge
```bash
bash merge.sh <bookname>
```

## Return code of chapter_crawler
0: success
1: chapter file existed
2: failed to grab text body of the chapter, probably the path is wrong
3: file name conflicted. expect `chapter_file_name` is calculated from the toc page; actual `chapter_file_name` is calculated from the article page