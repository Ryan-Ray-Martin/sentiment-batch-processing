# Batch Processing Server

## Overview

The Batch Processing Server is a high-performance, production-grade application developed by Intrinsic Research Capital. It leverages the power of Starlette for asynchronous handling and Hugging Face Transformers for sentiment analysis. This server is designed to process batch data efficiently and integrate seamlessly with other analytical tools.

## Features

- **ASGI Server**: Utilizes Starlette to handle incoming requests asynchronously, ensuring high throughput and scalability.
- **Sentiment Analysis**: Employs Hugging Face Transformers with the ProsusAI/finbert model for advanced sentiment analysis.
- **Asynchronous Processing**: Manages batch processing through a queue-based system for efficient data handling.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Set Up the Python Environment**

   Ensure you have Python 3.11 installed. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the Server**

   Launch the server using Uvicorn:

   ```bash
   uvicorn batch_server:app --host 0.0.0.0 --port 8000
   ```

2. **Send Batch Data for Analysis**

   You can send a POST request with JSON data to the server. Use `curl` or any HTTP client to interact with the server.

   **Example Request:**

   ```bash
   curl -X POST -H "Content-Type: application/json" -d '[{"text": "Stocks rallied and the British pound gained."}, {"text": "The economy showed significant growth."}, {"text": "Investors are optimistic about the market."}]' http://localhost:8000/
   ```

   **Example Response:**

   ```json
   [
     { "label": "positive", "score": 0.898361325263977 },
     { "label": "positive", "score": 0.948479950428009 },
     { "label": "positive", "score": 0.6735053658485413 }
   ]
   ```

## Configuration

- **Model**: The server uses the `ProsusAI/finbert` model for sentiment analysis. You can configure this by modifying the `server_loop` function in `batch_server.py`.

## Development

For development and testing, follow these steps:

1. **Install Development Dependencies**

   Make sure you have all necessary dependencies installed. These may include testing and linting tools.

   ```bash
   pip install -r requirements.txt
   ```

2. **Run Tests**

   Execute the test suite to ensure everything is working correctly.

   ```bash
   pytest
   ```

3. **Lint Code**

   Use linting tools to maintain code quality.

   ```bash
   flake8 .
   ```

4. **Cloud Formation Stack**

   aws cloudformation create-stack \
  --stack-name MySimplifiedEKSStack \
  --template-body file://eks_template.yaml \
  --parameters ParameterKey=ClusterName,ParameterValue=eks-cluster \
               ParameterKey=NodeGroupName,ParameterValue=eks-nodegroup \
               ParameterKey=NodeInstanceType,ParameterValue=t3.medium \
               ParameterKey=SubnetIds,ParameterValue="subnet-0a9c0a3bc1c3e2135" \
               ParameterKey=SecurityGroupIds,ParameterValue="sg-0f99af2cc7272cc4b" \
  --capabilities CAPABILITY_NAMED_IAM


## Contributing

Contributions are welcome! Please follow the standard GitHub workflow:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and ensure they are well-tested.
4. Submit a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or further information, please contact:

- **Project Maintainer**: [Ryan Martin](mailto:ryanraymartin@gmail.com)
- **Company**: Intrinsic Research Capital

---

_This README provides a comprehensive overview of the Batch Processing Server, including installation, usage, and development instructions. It is designed to assist users in setting up and utilizing the server efficiently._
