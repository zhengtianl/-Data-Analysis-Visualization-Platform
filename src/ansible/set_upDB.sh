export node=172.26.133.182

export user='admin'
export pass='admin'
export VERSION='3.2.1'
export cookie='a192aeb9904e6590849337933b000c99'

sudo docker stop couchdb
sudo docker rm couchdb

sudo docker pull ibmcom/couchdb3:${VERSION}

sudo docker run -d --name couchdb -p 5984:5984 --restart always -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=admin ibmcom/couchdb3:3.2.1

