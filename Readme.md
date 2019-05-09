## Building
sudo docker image build -t rhisling/keras .

## Running
sudo docker container run --name powerapi -p 5001:5000 -d rhisling/keras