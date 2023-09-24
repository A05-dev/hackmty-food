import chromadb
import csv
from chromadb.utils import embedding_functions
from chromaviz import visualize_collection

# Get the column names into an array
def extract_column_names():
    column_names = []
    # Read the CSV file and extract column names
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        # Assuming the first row contains column headers
        column_names = next(reader)
        return column_names
    
# Embed the csv into the vdb
def fill_embeds():
    i = 0
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:  # Iterate over each row in the CSV file
            recipe_name = row['recipe_name']
            total_time = row['total_time']
            servings = row['servings']
            ingredients = row['ingredients']
            rating = row['rating']
            url = row['url']
            cuisine_path = row['cuisine_path']
            nutrition = row['nutrition']
            
            collection.add(
                documents= nutrition + "," + ingredients,
                metadatas= {"total_time" : total_time, "servings" : servings, "rating" : rating, "cuisine_path" : cuisine_path, "url" : url},
                ids = str(i)
            )
            
            i += 1;

if __name__ == "__main__":
    # Import csv file
    csv_file = 'db/recipes.csv'

    # OpenAI Embedings
    openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                    api_key="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",
                    model_name="text-embedding-ada-002"
    )
    
    # Keep the vdb persistent and use OpenAI Embedings
    client = chromadb.PersistentClient(path="db")
    collection = client.get_collection(name="recipes", embedding_function=openai_ef)
    
    # Inicializar visualizacion *
    visualize_collection(collection)
    

    
    