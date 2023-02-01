# STEP-BY-STEP GUIDE FOR PYTHON-BASED DOCKER IMAGES FOR LAMBDA FUNCTIONS

## Understanding the files structure

The following tree structure explains the content of the [`lambdas/python`](lambdas/python/) folder:

```bash
.
└── python/  # Folder for Python-based Lambda solution
    ├── Dockerfile          # Dockerfile that builds the Docker image
    ├── lambda_function.py  # Main "entrypoint" for the Lambda solution
    ├── requirements.txt    # Python requirements (libraries) for the imports
    ├── sample_code_1.py    # "Business logic code" 1 (used in "lambda_function.py")
    └── sample_code_2.py    # "Business logic code" 2 (used in "lambda_function.py")
```

## Dockerfile explained

The Dockerfile uses the official [AWS Python Base Image (Container Image)](https://docs.aws.amazon.com/lambda/latest/dg/python-image.html), which is explained in detail at [aws-lambda-base-image](https://github.com/aws/aws-lambda-base-images):

```Dockerfile
FROM public.ecr.aws/lambda/python:3.9
```

Then, a custom label for traceability is added (optional):

```Dockerfile
LABEL maintainer="Santiago Garcia Arango [san99tiago]"
```

Afterwards, one of the most important steps happen. This is copying the actual code into Lambda Function folder that is dynamically used for the execution (in this case `${LAMBDA_TASK_ROOT}` is an pre-defined environment variable, that based on the source image creation, it corresponds to `/var/task`, as can be seen at [python3.9 (base image)](https://github.com/aws/aws-lambda-base-images/blob/python3.9/Dockerfile.python3.9)):

```Dockerfile
# Copy function's code
COPY . ${LAMBDA_TASK_ROOT}
```

Subsequently, we install the necessary Python dependencies (or external libraries to import), this is usually done via the `pip3 install` command. The `--target` flag specifies where to install it, so we select again the `${LAMBDA_TASK_ROOT}`, for compliance reasons with the Lambda runtime specifications.

```Dockerfile
# Install python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
```

Finally, we finish the Dockerfile with the `CMD` command that specifies which entrypoint is going to be used for running the Lambda function (the handler):

```Dockerfile
# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.handler" ]
```

## Important remarks

1. The CDK Stack creates the Lambda-Python (Docker-based) image by indicating the source folder of the necessary files that should exist in the image creation. This usually needs at least the `Dockerfile` and the `lambda_function.py` files (bare minimum). Then, we must specify at the CDK Stack the following:

   ```Python
   PATH_TO_FUNCTION_FOLDER = "/path/to/folder/with/necessary/files"
   self.docker_lambda_function = aws_lambda.DockerImageFunction(
       code=aws_lambda.DockerImageCode.from_image_asset(PATH_TO_FUNCTION_FOLDER),
       # <Other attributes missing>
   )
   ```

2. You must match the "filename" and "function" of the Lambda entrypoint specified at the [`lambdas/python/Dockerfile`](lambdas/python/Dockerfile) file, with the corresponding Python file that contains the actual code at [`lambdas/python/lambda_function.py`](lambdas/python/lambda_function.py):

   ```Dockerfile
   # In /lambdas/python/Dockerfile
   CMD [ "lambda_function.handler" ]
   ```

   ```Python
   # In /lambdas/python/lambda_function.py
   def handler(event, context):
       # <code>
   ```

   See how the `lambda_function` corresponds to `lambda_function.py` and `handler` corresponds to `hander(event, context)`

3. Even if it sounds funny, remember to have Docker installed and running, otherwise you could get errors like (which shows a failure, but the real reason why it failed, is because it couldn't use Docker commands):
   ```txt
   <ERROR CODE>
   fail: docker login --username AWS --password-stdin https://XXXXXXXXXXXX.dkr.ecr.us-east-1.amazonaws.com exited with error code 1
   ```
