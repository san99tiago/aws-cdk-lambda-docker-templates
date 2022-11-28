FROM public.ecr.aws/lambda/python:3.9

LABEL maintainer="Santiago Garcia Arango [san99tiago]"

# Copy function code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.handler" ]
