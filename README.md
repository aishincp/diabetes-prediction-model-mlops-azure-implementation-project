# Diabetes Prediction Model Deployment on Azure (MLOps Level 0)

This project demonstrates the foundational principles of MLOps by building and deploying a diabetes prediction model on the Azure cloud platform.

## Project Overview:

* **Goal:** To develop and deploy a ML model that predicts the likelihood of diabetes based on patient data, focusing on establishing a basic MLOps pipeline on Azure.
* **Dataset:** The project uses a publicly available dataset from [Kaggle](link). The dataset contains features such as Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, DiabetesPedigreeFunction, and Age. The target variable is Outcome (0 or 1, indicating the absence or presence of diabetes). The dataset is relatively small and well structured, making it suitable for initial MLOps explorationa and model deployment.
* **Model:** A Linear Regression (LR) model was chosen for this initial phase of project. The primary focus was on learning & implementing the MLOps concepts & Azure services for **data ingestion, processing, and model deployment.** LR serves as a good starting point for this learning purpose. Future iterations of the project will explore and evaluate more complex models (e.g. Random Forest, Gradient Boost) to potentially improve prediction performance. The dataset's size and structure also made LR a suitable choice for this stage.
* **Azure Services:**
   * **Azure Blob Storage:** Used to store the raw dataset in CSV format. A resource group **('diabetes-ml-rg')** was created, containing a stoarge account **('diabetesdatastorage')**. Within the storage account, a container **('diabetes-raw-data')** was created to hold the **'diabetes.csv'** file.
   * **Azure Data Factory (data-factory-diabetes):** Used for **Extract, Transform, Load (ETL)** operations. **A pipeline was created in ADF to ingest data from Azure Blob Storage container ('diabetes-raw-data') and make it available within Azure ML workspace**. The processed dataset is represented as 'diabetes_processed_dataset' within ADF.
   * **Azure ML Workspace (diabetes-ml-ws):** This is the central hub for model training and deployment.
       * **Data Loading:** The dataset, now accessible through ADF pipeline, was loaded into the ML Workspace. The line: ``` dataset = Dataset.get_by_name(ws, name='diabetes_data)``` retrieves the dataset.  The name 'diabetes-data' corresponds to how you registered the dataset *within the ML Workspace*. It doesn't necessarily have to be the same as the name in Blob Storage or ADF, though it often is for clarity. The key is that the pipeline in ADF makes the data available in the ML Workspace and registers it there with the name 'diabetes-data'.
