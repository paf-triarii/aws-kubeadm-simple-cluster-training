FROM hashicorp/terraform:1.4.2@sha256:2734886211a482abaff7efbbfd8bdb32295c9c35dda124092d46f39b69f47c42 as terraform


FROM ubuntu:jammy@sha256:67211c14fa74f070d27cc59d69a7fa9aeff8e28ea118ef3babc295a0428a6d21

# This are the environment variables used for Terraform authentication.
# For security reasons are left blank in the image definition
# Those should be passed as parameter in the docker run execution.
ENV AWS_ACCESS_KEY_ID=""
ENV AWS_SECRET_ACCESS_KEY=""
ENV AWS_REGION="eu-west-1"
ENV VERBOSITY="--vvv"


# Installing required dependencies
RUN apt-get update && apt-get install -y git software-properties-common wget

COPY --from=terraform /bin/terraform /bin/terraform


###################### ANSIBLE BLOCK ##################

RUN apt-add-repository ppa:ansible/ansible \
    && apt-get update

RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip ansible sudo

# This are Ansible requirements for being able to use AWS tasks/modules
RUN ansible-galaxy collection install amazon.aws 
RUN pip3 install boto3 botocore

RUN apt-get update \
  && apt-get install -y jq \
  && wget -qO /usr/bin/yq https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 \
  && chmod a+x /usr/bin/yq

##############################################################

# We define the main arguments used accross user creation and workdir stablishment.
# The idea to have placeholders for the UID, GID, USER and GROUP is avoid volume conflict issues.
# For design simplicity we execute the playbook sharing the project code with a volume in the local path to the target container /app folder.
# If the hardcode those values, if the any of those are different in the container than the user that will execute in the host machine, permissions problems will apprear.
ARG DIR="/app"
WORKDIR ${DIR}
ARG UID="1000"
ARG GID="1000"
ARG GROUP="perico"
ARG USER="perico"

###################### USER CREATION ##################

RUN groupadd -g ${GID} ${GROUP} \
  && useradd -b ${DIR} -d ${DIR} -u ${UID} -g ${GID} ${USER}

RUN echo "${USER} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/10-user

##############################################################

USER ${UID}:${GID}