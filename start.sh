# Build the docker images
docker build --target api -t runningapi .
docker build --target db -t runningdb .

# Define network and container names
NETWORK_NAME="runningnet"
DB_CONTAINER_NAME="runningdb"
API_CONTAINER_NAME="runningapi"
DB_IMAGE="runningdb"
API_IMAGE="runningapi"

# Check if network exists, create if not
if ! docker network ls | grep -q "$NETWORK_NAME"; then
  echo "Creating Docker network: $NETWORK_NAME"
  docker network create $NETWORK_NAME
else
  echo "Docker network $NETWORK_NAME already exists"
fi

# Create and run the database container, attaching it to the network
echo "Creating and running container: $DB_CONTAINER_NAME with image $DB_IMAGE"
docker run -d --name $DB_CONTAINER_NAME --network $NETWORK_NAME --hostname "database" --env-file ./.env -p 5432:5432 $DB_IMAGE

# Create and run the api container, attaching it to the network
echo "Creating and running container: $API_CONTAINER_NAME with image $API_IMAGE"
docker run -d --name $API_CONTAINER_NAME --network $NETWORK_NAME -p 80:80 $API_IMAGE 

echo "Docker setup complete. Containers $DB_CONTAINER_NAME and $API_CONTAINER_NAME are running and connected to $NETWORK_NAME."