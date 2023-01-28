from flask import Flask, jsonify
import gdown
app = Flask(__name__)

@app.route('/')
def hello_world():
    #return "Hello, World!"
    gdown.download('https://drive.google.com/drive/folders/1UG3LP3mwzoCUcsWmXQ2TMPOp91tJ_dnt', 'colab.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')

    
    
    
    gdown.download('https://drive.google.com/file/d/<colab_notebook_id>', 'colab.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')




#@app.route('/run-colab')
#def run_colab():
 #   gdown.download('https://drive.google.com/file/d/<colab_notebook_id>', 'colab.ipynb', quiet=False)
  #  return jsonify(message='colab notebook ran successfully')