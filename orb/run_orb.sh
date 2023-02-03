#build image
docker build -t virtual-orb ./orb/

# run container
docker run -v /orb_device -p 8000:8000 virtual-orb:latest