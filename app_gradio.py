import gradio as gr
import numpy as np
# Import your specific chemistry/physics logic here
# from src.predict import predict_tc 

def predict_superconductivity(composition_input):
    """
    This function wraps your existing logic. 
    Replace the return below with your model's actual prediction.
    """
    try:
        # Example processing logic:
        # result = your_model.predict(composition_input)
        return f"Predicted Tc for {composition_input}: 85K (Example Output)"
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio Interface Setup
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# ⚡ Chemcomp SuperCond")
    gr.Markdown("Predict the critical temperature ($T_c$) based on chemical composition.")
    
    with gr.Row():
        with gr.Column():
            inp = gr.Textbox(placeholder="Enter chemical formula (e.g., YBa2Cu3O7)", label="Chemical Composition")
            btn = gr.Button("Predict Tc", variant="primary")
        with gr.Column():
            out = gr.Textbox(label="Prediction Result")

    btn.click(fn=predict_superconductivity, inputs=inp, outputs=out)

if __name__ == "__main__":
    demo.launch()
  
