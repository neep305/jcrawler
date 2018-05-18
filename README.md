# Django 

Django 개발 서버 실행
```bash
$ python3 manage.py runserver
```

기능 테스트 실행
```bash
$ python3 manage.py test
```

# NumPy
데이터 사이언스 스쿨의 자료를 참고하였습니다.
```python
import numpy as np

ar = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
ar
```

# Pandas
To read csv data
```python
import csv
 
with open('file.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        print(row)
```

# Data Visualisation
Going to use 'bokeh' for data visualisation
