# Basic API example

To build Docker image:
```bash
sudo docker build -t apiexample:latest .
```
To run Docker image:
```bash
sudo docker run -d --restart=always -p 80:80 apiexample
```
Remove old images:
```bash
sudo docker system prune -f
```
Installing Docker:
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

sudo apt-get update

apt-cache policy docker-ce

sudo apt-get install -y docker-ce

sudo systemctl status docker
```
To run on localhost without docker, cd into the app directory and run:
```python
python main.py
```
And navigate in your browser to localhost:8000. The username is: user and the password is: pass
