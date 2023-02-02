#build image
docker build -t virtual-orb .

# run container
docker run -v $1:/app/test-files -p 8000:8000 virtual-orb:latest