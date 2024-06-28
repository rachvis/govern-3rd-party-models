# Monitoring detached prompt templates using watsonx.governance

Once you have completed the setup from lab 0, follow the steps below to setup governance for the prompts for the model deployed in Virtual Server Instance in lab 1. 

Download this git repo to your local computer

### Step 1: Import the notebook in projects
---

1. Login to [watsonx](https://dataplatform.cloud.ibm.com/wx/home) 

2. Open the project 'InsuranceClaim Summary' that's created in lab 1

3. Go to 'Assets' and click on 'New Asset'

Assets -> New Asset -> Work with data and models in Python or R notebooks

<img src="images/lab 2/notebook 01.png">

4. Selct 'Local file', upload the file lab.ipynb and click on 'Create'

<img src="images/lab 2/notebook 02.png">

### Step 2: Edit the notebook 
---

1. Run the notebook cells, edit the segments as mentioned in the notebook. 

- IBM Cloud API Key

- Project ID from watsonx project

- Floating IP of VSI instance where flask app is running

2. Run all cells. Go back to projects, you will see a detached prompt that's created in 'Assets'

<img src="images/lab 2/notebook 03.png">

### Step 3: Explore the metrics on UI
---

1. Go back to projects, you will see a new asset added - 'External prompt template (model flan-t5 on VM)

2. Open the prompt template that's added, explore the Generative AI monitoring dashboards. 

<img src="images/lab 2/governance 01.png">

<img src="images/lab 2/governance 02.png">

### Congratulations, you have now set up monitoring with watsonx for external prompt template!! 