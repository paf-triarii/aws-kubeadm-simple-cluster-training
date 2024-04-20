FROM hashicorp/terraform:1.7 as terraform


FROM ubuntu:jammy-20240227

# This are the environment variables used for Terraform authentication.
# For security reasons are left blank in the image definition
# Those should be passed as parameter in the docker run execution.
ENV AWS_ACCESS_KEY_ID=""
ENV AWS_SECRET_ACCESS_KEY=""
ENV AWS_REGION="eu-west-2"
ENV VERBOSITY="--vvv"


# Installing required dependencies
RUN apt-get update && apt-get install -y git software-properties-common wget curl unzip gnupg-agent gnupg

COPY --from=terraform /bin/terraform /bin/terraform


###################### ANSIBLE BLOCK ##################

RUN apt-add-repository ppa:ansible/ansible \
    && apt-get update

RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip ansible sudo

# This are Ansible requirements for being able to use AWS tasks/modules
RUN ansible-galaxy collection install amazon.aws community.aws

RUN pip install boto3 botocore

RUN apt-get update \
  && apt-get install -y jq

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

COPY entrypoint.sh $DIR/entrypoint.sh
RUN chmod +x $DIR/entrypoint.sh

USER ${UID}:${GID}

RUN sudo curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
  && sudo install -o ${USER} -g ${GROUP} -m 0755 kubectl /usr/local/bin/kubectl

ENV ANSIBLE_HOST_KEY_CHECKING=False
ENV ANSIBLE_USER_LOCAL="perico"
ENV ANSIBLE_USER_REMOTE="ubuntu"

ENTRYPOINT ["/app/entrypoint.sh"]
