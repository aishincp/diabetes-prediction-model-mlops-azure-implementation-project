# Diabetes Prediction Model Deployment on Azure (MLOps Level 0)

This project demonstrates the foundational principles of MLOps by building and deploying a diabetes prediction model on Azure Cloud Services.

![FlowChart](https://github.com/user-attachments/assets/5e002f23-a472-477f-a129-0353c039cd2f)


## Project Overview:

* **Goal:** To develop and deploy a ML model that predicts the likelihood of diabetes based on patient data, focusing on establishing a basic MLOps pipeline on Azure.
* **Dataset:** The project uses a publicly available dataset from [Kaggle](link). The dataset contains features such as Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, DiabetesPedigreeFunction, and Age. The target variable is Outcome (0 or 1, indicating the absence or presence of diabetes). The dataset is relatively small and well structured, making it suitable for initial MLOps explorationa and model deployment.
* **Model:** A Linear Regression (LR) model was chosen for this initial project phase. The primary focus was on learning & implementing the MLOps concepts & Azure services for **data ingestion, processing, and model deployment.** LR serves as a good starting point for this learning purpose. Future iterations of the project will explore and evaluate more complex models (e.g. Random Forest, Gradient Boost) to potentially improve prediction performance. The dataset's size and structure also made LR suitable for this stage.
* **Azure Services:**
   * **Azure Blob Storage:** Used to store the raw dataset in CSV format. A resource group **('diabetes-ml-rg')** was created, containing a stoarge account **('diabetesdatastorage')**. Within the storage account, a container **('diabetes-raw-data')** was created to hold the **'diabetes.csv'** file.
   * **Azure Data Factory (data-factory-diabetes):** Used for **Extract, Transform, Load (ETL)** operations. **A pipeline was created in ADF to ingest data from Azure Blob Storage container ('diabetes-raw-data') and make it available within the Azure ML workspace.**. The processed dataset is represented as 'diabetes_processed_dataset' within ADF.
   * **Azure ML Workspace (diabetes-ml-ws):** This is the central model training and deployment hub.
       * **Data Loading:** The dataset, now accessible through ADF pipeline, was loaded into the ML Workspace. The line: ``` dataset = Dataset.get_by_name(ws, name='diabetes_data')``` retrieves the dataset.  The name 'diabetes-data' corresponds to how you registered the dataset *within the ML Workspace*. It doesn't necessarily have to be the same as the name in Blob Storage or ADF, though it often is for clarity. The key is that the pipeline in ADF makes the data available in the ML Workspace and registers it there with the name 'diabetes-data'.
      * **Model Training:** A **Linear Regression** model was trained using the loaded dataset. The 'train.ipynb' notebook in the Workspace was used for this purpose, leveraging libraries like ```azureml.core, scikit-learn, pandas, and joblib.```
      * **Model Saving:** The trained model was saved usign ```joblib``` as ```model.pkl```
      * **Model Registration:** The model was registered in the ML workspace with path ```model.pkl```, name ```'diabetes-lr'```, and tag ```{"framework": "scikit-learn"}```.
      * **Custom Environment:** A custom environment named ```env``` was created to manage the required Python packages for model training and deployment.
      * **Model Deployment:** The model was deployed to **Azure Container Instances (ACI)**. This process automatically created an Azure Container Registry to store the Docker image of the deplyed model.
      * **Model Testing:** The deployment model was tested in 'test.ipynb' notebook to verify correct predictions.
      * **Scoring Script:** This script was created to handle incoming prediction requests for the deployed model.

* **Deployment:** The model was deplas a containerized web service to Azure Container Instance (ACI). This created a Docker image of the model & deplyed it to ACI, making it accessible for making predictions.

#### This project covers the core aspects of the MLOps Level 0, including **data ingestion, model training, and deployment.** It establishes a basic MLOps pipeline on Azure, demonstrating an understanding of the fundamental steps involved in the machine learning lifecycle.
