import gradio as gr
import pdfplumber
from huggingface_hub import InferenceClient

HF_TOKEN = "HUGGINGFACE API KEY" 
MODEL_ID = "Qwen/Qwen2.5-7B-Instruct"

client = InferenceClient(api_key=HF_TOKEN)

def extract_text_from_pdf(pdf_file):
    """PDF dosyasından metin çıkarır."""
    text = ""
    try:
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text.strip()
    except Exception as e:
        return f"Hata: PDF okunamadı. {str(e)}"

def ask_ai(pdf_text, question):
    """PDF metni ve soruyu AI'ya gönderir."""
    if not pdf_text:
        return "Lütfen önce bir PDF yükleyin."
    
    context = pdf_text[:5000] 
    
    prompt = f"""Aşağıdaki metne dayanarak soruyu cevapla. Eğer cevap metinde yoksa 'Bu bilgi metinde bulunmuyor' de.

Metin:
{context}

Soru: {question}
Cevap:"""

    messages = [{"role": "user", "content": prompt}]
    
    try:
        response = client.chat.completions.create(
            model=MODEL_ID,
            messages=messages,
            max_tokens=500,
            temperature=0.1
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI Hatası: {str(e)}"

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(f"# 📄 PDF Soru-Cevap Sistemi\nModel: {MODEL_ID}")
    gr.Markdown("Proje Sunumu: Mehmet Can Sarı")
    gr.Markdown("Sınıf: 11/A Bilişim | Okul Numarası: 1237")
    
    with gr.Row():
        with gr.Column():
            pdf_input = gr.File(label="PDF Yükle", file_types=[".pdf"])
            pdf_content = gr.State()
            upload_btn = gr.Button("Metni Çözümle", variant="primary")
            status = gr.Textbox(label="Durum", interactive=False)
            
        with gr.Column():
            question_input = gr.Textbox(label="Sorunuzu Yazın", placeholder="Örn: Bu dökümanın konusu nedir?")
            answer_output = gr.Textbox(label="Yapay Zekanın Cevabı", lines=10)
            ask_btn = gr.Button("Soruyu Sor")

    upload_btn.click(fn=extract_text_from_pdf, inputs=pdf_input, outputs=pdf_content).then(
        fn=lambda x: "PDF başarıyla okundu!" if x and not x.startswith("Hata") else "Okuma başarısız.",
        inputs=pdf_content, outputs=status
    )
    
    ask_btn.click(fn=ask_ai, inputs=[pdf_content, question_input], outputs=answer_output)

if __name__ == "__main__":
    demo.launch()
