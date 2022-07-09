#Using fast API to make the model available for access remotely
from fastapi import FastAPI
import joblib,os
import uvicorn
import pickle


app = FastAPI()
#pkl
phish_model = open('phishing.pkl', 'rb')
phish_model_ls = joblib.load(phish_model)

#ML Aspect
@app.get('/predict/{feature}')
async def predict(features):
	url = []
	url.append(str(features))
	y_Predict = phish_model_ls.predict(url)
	if y_Predict == 'bad':
		result = "This is a phishing Site"
	else:
		result = "This is a legitimate Site"
	return (features,result)
if __name__ == '__main__':
 uvicorn.run(app,host="127.0.0.1",port=8000)

#uvicorn app:app --reload