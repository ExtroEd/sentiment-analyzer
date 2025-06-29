from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F


MODEL_NAME = "cointegrated/rubert-tiny-sentiment-balanced"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

LABELS_EN = {
    'negative': 'Negative',
    'neutral': 'Neutral',
    'positive': 'Positive'
}

def get_sentiment(text: str, return_type: str = 'label'):
    inputs = tokenizer(text, return_tensors='pt', truncation=True,
                       padding=True, max_length=512).to(device)
    with torch.no_grad():
        logits = model(**inputs).logits
        probs = F.softmax(logits, dim=-1).squeeze().cpu().numpy()

    if return_type == 'label':
        label_id = probs.argmax()
        return LABELS_EN[model.config.id2label[label_id]]
    elif return_type == 'proba':
        return probs
    elif return_type == 'score':
        score = probs.dot([-1, 0, 1])
        return score
    else:
        raise ValueError("return_type must be 'label', 'proba', or 'score'")
