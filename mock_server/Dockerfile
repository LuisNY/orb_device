FROM python:3.8

WORKDIR /orb_device

COPY . .

# create folder to store irises sent to mock server
RUN mkdir -p /orb_device/mock_server/stored_irises

RUN pip3 install --no-cache-dir -r ./requirements.txt

# launch mock server
CMD [ "python3", "./main.py" ]