export node=172.26.133.182

export user='admin'
export pass='admin'
export VERSION='3.2.1'
export cookie='a192aeb9904e6590849337933b000c99'

sudo docker pull ibmcom/couchdb3:${VERSION}

sudo docker create      --name couchdb${node} -p 5984:5984     --env COUCHDB_USER=${user}      --env COUCHDB_PASSWORD=${pass}      --env COUCHDB_SECRET=${cookie}      --env ERL_FLAGS="-setcookie \"${cookie}\" -name \"couchdb@${node}\""      ibmcom/couchdb3:${VERSION}

