# Setting up services on IBM Cloud to run Watsonx
---
### 1. Accept invitation to instance<a name="accept-invitation"></a>
---
If you are enrolled in the bootcamp, you will likely be working in a shared instance. You should have received an email asking you to join an instance from noreply@techzone.ibm.com with subject "[EXTERNAL] A reservation has been shared with you on IBM Technology Zone."

Join the instance by clicking HERE in "Please go HERE to accept your invitation" or "Join now" as in the image below. 

<img width="450" alt="tech-zone-email" src="images/lab 0/invite.png">


When this page displays, click the checkbox as in the image below then click "Join Account".

<img width="450" alt="tech-zone-email" src="images/lab 0/accept.png">

### 2. Navigate to Catalog (https://cloud.ibm.com/catalog)

### 3. Provision an instance of [Watson Studio](https://cloud.ibm.com/catalog/services/watson-studio)
---

- Select the region 'Dallas' and the plan 'Lite'

<img src="images/lab 0/watson studio 01.png">

- Provide a unique instance name, add your name to the tags, click 'Create'

<img src="images/lab 0/watson studio 02.png">

### 4. Launch the service with 'watsonx' once the service is successfully provisioned
---

<img src="images/lab 0/launch in watsonx.png">

### 5. Create a new project<a name="new-project"></a>
---
Now, we can go ahead a create a new project. In the **Projects** section at the bottom, click the "+" symbol next to it to create a new project.

<img src="images/lab 0/create_project.png">

Enter a **unique name** for your project, include both your first and last name and any other information you would like.

<img src="images/lab 0/project_name.png">

### Cloud Object Storage (COS)
It is likely there is also already a Cloud Object Storage instance selected for you, with a name that starts with "itzcos-..." If so, you don't have to do anything! 

Otherwise you may be prompted to select from multiple instances. Please consult with your bootcamp lead which COS instance to select.

<img src="images/lab 0/select-instance.png">

### Click Create
Now go ahead and click Create. It may take a few seconds to officially be created.

### 5. Associate the correct WML instance<a name="wml-instance"></a>
---
With the project created, you should be directed to the project home page. Go ahead and select the "Manage" tab.

Click on "Services and Integrations" in the left side-bar. Then click on "Associate service."

<img src="images/lab 0/associatingwml.png">

Select the service listed with "Type" = "Watson Machine Learning" and click **Associate**. 

<img src="images/lab 0/select-wml-service.png">

**Note:** If you can't find the service, remove all filters from the "Locations" dropdown.

### 6. Create an instance of watsonx.governance
---

Click on Navigation menu and select 'Services catalog' from 'Administration' and select Watsonx.governance in the service catalog

<img src="images/lab 0/openscale 01.png">

Provide the details and click 'Create'

<img src="images/lab 0/openscale 02.png">


### 7. Check that an inventory is created<a name="create-inventory"></a>
---
Now that we have created a project, we'll need to create an inventory for Lab 2. Visit the watsonx home page, and on the left-hand side bar click on the "AI Governance" dropdown, then "AI use cases".

<img src="images/lab 0/navigate_aiUsecase.png">

If you are directed to a page that says "No inventories available yet," click "Manage inventories" and create a new one.

<img src="images/lab 0/manageinventory.png">

Otherwise, if you see some use cases listed in the page, you already have an inventory created and are all set! You are done with Lab 0 and can proceed with Lab 1. **Note:** If you are still interested in creating a new fresh inventory for the bootcamp, click the gear icon at the top. Then navigate to "Inventories" and follow the same instructions below.

<img src="images/lab 0/insuranceClaimInventory.png">

When creating your inventory, give it a unique name, and select the right COS instance.

After setting up a project and inventory, you are now ready for the class!