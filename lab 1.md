# Deploying a LLM on Virtual Server Instance on IBM Cloud

### Step 1. Set up the environment
---
This tutorial uses IBM Cloud. You will provision and use the following components.

Ubuntu 22.04 - 4 vCPU | 16 GiB | 8 Gbps Virtual server instances

Provisioning a VSI auto creates for you:
- A VPC attached to it
- A security group governing the previous VPC
- A Floating IP in the same region to expose your app to internet

1. Provision a virtual server instance for VPC.

2. Name the instance:
- For image options, use ibm-ubuntu-22-04-4-minimal-amd64-1
- For Profile, select for a Balanced 8 vCPU and 32 GB RAM

<img src="images/lab 1/vsi 01.png">

3. Generate an SSH Key that is specific to the system that you will use to log in. You must click Create SSH key, then name the key. Click Create.The key is auto generated and downloaded for you.

<img src="images/lab 1/ssh key.png">

4. Choose Virtual network interface for Networking, and let it create one for you. Click on 'Create VPC' and create a VPC network.

<img src="images/lab 1/vpc.png">

5. Click on 'Create'. That’s it. Now wait for the provisioning to complete.

### Step 2: Setup the Networking
---

Before you can access the cluster, you must also set up the networking.

#### Step 2a: Get a Floating IP

The instance does not come with a Floating IP, so you must get one.

1. Navigate to Floating IP

<img src="images/lab 1/floating ip.png">

2. Click Reserve, and make sure that you select the same zone as the one you chose for the instance, so you can see it listed in the resource to bind drop down list.

<img src="images/lab 1/reserve ip.png">

3. Click Reserve to assign the Floating IP to your instance.

#### Step 2b: Allow inbound on Port 80

The app is deployed on port 80 so that it can be accessed without any redirection. Although the required fire wall setting on the system is controlled by the script, you must still manually add an inbound rule to the security policy created.

1. Navigate to [security groups for VPC](https://cloud.ibm.com/vpc-ext/network/securityGroups).
2. Pick the group that is assigned to your instance (you can find it tagged in the instance details), and navigate to Rules.
3. Add a new TCP Inbound Rule to allow traffic on port 80.

<img src="images/lab 1/inbound rule.png">

### Step 3: Access the cluster
---

1. Open the terminal, and navigate to the folder where you downloaded the SSH key.

2. Update the permissions on the key to allow SSH connect.

` chmod 400 <path to your pem file>`

3. SSH into the cluster by using the following command.

` ssh -i <path to your pem file> root@<Floating IP>`

4. Enter Yes when asked to add the key to known hosts.

<img src="images/lab 1/ssh to vsi.png">

### Step 4: 
---

There is a quick script to install all of the necessary libraries and tools for you as well as a Flask application to give you access to the model over a UI or API. Let’s see how to get it.

1. 

