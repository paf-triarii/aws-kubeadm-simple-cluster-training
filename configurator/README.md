# Configurator

This folder and it subsecuent directories contain the different ansible playbooks to configure target machines depending on the `purpose`, `target platform`, etc.

# Playbook list

This list summarizes all the available playbooks and its tested platforms.

<!-- TABLE OF CONTENTS -->
<details>
  <summary><b>Index</b></summary>
  <ol>
    <li>
      <a href="#windows-server-2019">WINDOWS SERVER 2019</a>
      <ul>
        <li><a href="#scrapping-bundle">Scrapping Bundle</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>


## WINDOWS SERVER 2019

### SCRAPPING BUNDLE

`scrapping_bundle` takes care of installing:
* `Brave`: browser to navigate in the target destinations
* `Docker Desktop`: exposed with HTTPs and dedicated to handle the containers that are scrapping data.
* `Python 12.x or higher`: for being able to execute auxiliar python scripts as needed.

#### REQUIREMENTS

The playbook needs to have the following to be ran successfully:
* `Machine Connection Details`: `private_key` and `user` (Administrator) to be able to connect to the instance.
* `Allowed IPs`: List of IPs to allow as input connections to the target machine in local firewall.

#### USAGE

To run this playbook individually, there main Docker image is used. For more details check [With Docker section](../README.md#with-docker)

```bash
    docker run --user $(id -u):$(id -g) -v $(pwd):/app  \
    -e VERBOSITY="-vvv" -e ANSIBLE_FILTER_PLUGINS=/app/filter_plugins terraform-generator:1.0 ansible-playbook aws/ansible/main.yaml -vv
```