# :whale: AWS-CDK-LAMBDA-DOCKER-TEMPLATES :whale:

The purpose of this project is to showcase how to deploy AWS Lambda Functions with Docker images on top of multiple programming languages (like Python or NodeJs), so they can be used to leverage different personalized solutions in a matter of minutes. The sky is the limit!

## General Architecture :hammer:

<img src="assets/CDK_Lambda_Docker_Templates.png" width=90%>

<br>

## Detailed Docker explanation :mag:

The following README files, created by [san99tiago](https://github.com/san99tiago), explain how the Lambda functions for this project work in detail for different programming languages (base-images):

- PYTHON: [Step-by-step guide for Python-based Docker images for Lambda Functions](PYTHON_README.md)
- NODEJS: [Step-by-step guide for NodeJs-based Docker images for Lambda Functions](NODEJS_README.md)

## AWS CDK :cloud:

[AWS Cloud Development Kit](https://aws.amazon.com/cdk/) is an amazing open-source software development framework to programmatically define cloud-based applications with familiar languages. <br>

My personal opinion is that you should learn about CDK when you feel comfortable with cloud-based solutions with IaC on top of [AWS Cloudformation](https://aws.amazon.com/cloudformation/). At that moment, I suggest that if you need to enhance your architectures, it's a good moment to use these advanced approaches. <br>

The best way to start is from the [Official AWS Cloud Development Kit (AWS CDK) v2 Documentation](https://docs.aws.amazon.com/cdk/v2/guide/home.html). <br>

## Dependencies :vertical_traffic_light:

The dependencies are explained in detail for each project, but the most important ones are AWS-CDK, Python and NodeJS. <br>

My advice is to primary understand the basics on how CDK works, and then, develop amazing projects with this incredible AWS tool!. <br>

### Software dependencies (based on project)

- [Visual Studio Code](https://code.visualstudio.com/) <br>
  Visual Studio Code is my main code editor for high-level programming. This is not absolutely necessary, but from my experience, it gives us a great performance and we can link it with Git and GitHub easily. <br>

- [NodeJs](https://nodejs.org/en/) <br>
  NodeJs is a JavaScript runtime built on Chrome's V8 JavaScript engine programming language. The community is amazing and lets us handle async functionalities in elegant ways. <br>

- [Python](https://www.python.org/) <br>
  Python is an amazing dynamic programming language that let us work fast, with easy and powerful integration of different software solutions. <br>

### Libraries and Package dependencies (based on project)

- [CDK CLI (Toolkit)](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) <br>
  To work with the CDK, it is important to install the main toolkit as a NodeJs global dependency. Then, feel free to install the specific language AWS-CDK library (for example: [aws-cdk.core](https://pypi.org/project/aws-cdk.core/)). <br>

## Usage :dizzy:

All projects are well commented/documented and most of them have specifications and remarks for their purpose and I/O. <br>

## Special thanks :gift:

- Thanks to all contributors of the great OpenSource projects that I am using. <br>

## Author :musical_keyboard:

### Santiago Garcia Arango

<table border="1">
    <tr>
        <td>
            <p align="center">Senior DevOps Engineer passionate about advanced cloud-based solutions and deployments in AWS. I am convinced that today's greatest challenges must be solved by people that love what they do.</p>
        </td>
        <td>
            <p align="center"><img src="assets/SantiagoGarciaArangoCDK.png" width=60%></p>
        </td>
    </tr>
</table>
