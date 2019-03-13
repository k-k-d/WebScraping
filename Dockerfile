FROM python:3.6.7
WORKDIR /WebScrapePyDock
ADD . /WebScrapePyDock
RUN pip install -r ./require.txt
EXPOSE 80
CMD ["python" , "webscrape.py"]
