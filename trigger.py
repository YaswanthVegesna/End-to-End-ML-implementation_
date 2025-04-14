import papermill as pm
import os
BASE_DIR = r"E:\US_Batch_AI\ML_End-to-End\ML_project"
NOTEBOOKS_DIR = r"E:\US_Batch_AI\ML_End-to-End\ML_project\Notebooks"
RESULTS_DIR = r"E:\US_Batch_AI\ML_End-to-End\ML_project\Results"
# Define base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOTEBOOKS_DIR = os.path.join(BASE_DIR, "Notebooks")
RESULTS_DIR = os.path.join(BASE_DIR, "Results")
# Define notebooks path
notebooks = {
    "EDA": r"E:\US_Batch_AI\ML_End-to-End\ML_project\Notebooks\EDA.ipynb",
    "Feature_Engineering": r"E:\US_Batch_AI\ML_End-to-End\ML_project\Notebooks\Feature_Engineering.ipynb",
    "Machine_Learning": r"E:\US_Batch_AI\ML_End-to-End\ML_project\Notebooks\Machine_Learning.ipynb",
    "Ensembling_techniques": r"E:\US_Batch_AI\ML_End-to-End\ML_project\Notebooks\Ensembling_techniques.ipynb"
}
# Define output paths (overwrite mode)
output_paths = {
    name: path.replace(".ipynb", "_output.ipynb")
    for name, path in notebooks.items()
}

# Create outcomes folders if not exists
os.makedirs("Results/EDA_Results", exist_ok=True)
os.makedirs("Results/Feature_Engineering_Resulst", exist_ok=True)
os.makedirs("Results/ML_with_ensembling", exist_ok=True)
os.makedirs("Results/ML_without_ensembling", exist_ok=True)


# Execute all notebooks sequentially
for name, input_path in notebooks.items():
    print(f"▶️ Running {name} notebook...")

    pm.execute_notebook(
        input_path=input_path,
        output_path=output_paths[name],
        parameters={},  # Optional: pass dynamic params here
        kernel_name="python3"
    )

    print(f"✅ Completed {name}\n{'-'*40}")

print("🎉 All notebooks executed and stored in Results/")