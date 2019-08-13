
# qaptnet-api

FROM pytorch/pytorch

RUN pip install pytorch-transformers
RUN pip install gunicorn flask flask-cors

RUN mkdir /app
RUN mkdir /app/model-pretrained
WORKDIR /app

COPY qaptnet-api.py qaptnet-api.py
COPY qaptnet.py qaptnet.py
COPY model-pretrained/config.json model-pretrained/config.json
COPY model-pretrained/pytorch_model.bin model-pretrained/pytorch_model.bin
COPY model-pretrained/training_args.bin model-pretrained/training_args.bin

EXPOSE 7788

ENTRYPOINT gunicorn -b :7788 --workers=1 --access-logfile - --error-logfile - qaptnet-api:app

