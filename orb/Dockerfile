FROM python:3.8

WORKDIR /orb_device

COPY . .

RUN pip3 install --no-cache-dir -r ./requirements.txt
RUN pytest ./tests.py

# launch application
CMD [ "python3", "./main.py" ]