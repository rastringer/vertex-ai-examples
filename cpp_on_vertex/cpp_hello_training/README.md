
In this project, we will run a custom C++ container on [Vertex Training](https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform), a service which gives users control over model training process, including choice of framework, training code, and hyperparameter tuning options.

We build the container using Docker and Cloud Build, then store it in a repository on Artifact Registry. Please first set up the Cloud Build prerequisites listed [here].(https://cloud.google.com/build/docs/set-up)

Set up Artifact Registry following the details [here]()https://cloud.google.com/artifact-registry/docs/repositories/create-repos), and create a repository called 'cpp-training' (or choose a name, and adjust the environment variables below).

Add the GCP project id to the placeholder in `CMakeLists.txt`.

Open a Cloud Shell and set the following environment variables:

```
export PROJECT_ID=$(gcloud config list project --format "value(core.project)")
export REPO_NAME=cpp-vertex
export IMAGE_NAME=cpp-hello-training-image
export IMAGE_TAG=cpp-hello-training-image-tag
export IMAGE_URI=us-central1-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${IMAGE_NAME}:${IMAGE_TAG}
```

Run the following commands in Cloud Shell to build and push the image to the repository (will take ~5-10 mins).

```
docker build -f Dockerfile -t ${IMAGE_URI} ./
docker push ${IMAGE_URI}
```

Navigate to Artifact registry and check the image is there. Copy the image uri and update the `imageUri` in the config.yaml file. 

Ensure the relevant permissions for Vertex Training are enabled.

Simply run the following command in Cloud Shell to run the training job, then monitor its progress in the console. Since this is a simple `hello world` program, it should only take 1-2 mins to complete. 

```
// Set environment variables
export LOCATION='<enter project location eg us-central1>'
export JOB_NAME='<choose a name for the training job>

// Create the training job
gcloud ai custom-jobs create \
  --region=LOCATION \
  --display-name=JOB_NAME \
  --config=config.yaml
  ```