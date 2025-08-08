# FPInsight Pipeline

A full-stack web application for analyzing retail transaction data using the FP-Growth (Frequent Pattern Growth) algorithm to discover association rules and market basket insights.

## 🚀 Project Overview

FPInsight Pipeline allows users to upload retail transaction datasets and automatically generates association rules that reveal purchasing patterns. The application supports both local processing (for smaller datasets) and AWS Glue-based distributed processing (for large-scale datasets).

### Key Features

- **Dual Processing Modes**: Local processing with Python/MLxtend and distributed processing with AWS Glue/PySpark
- **Interactive Web Interface**: React-based frontend for easy file upload and visualization
- **Association Rule Mining**: Implements FP-Growth algorithm to find frequent itemsets and generate rules
- **Real-time Results**: Background processing with job tracking
- **Cloud Storage**: Results stored in AWS S3 for persistence and scalability
- **Visualization Dashboard**: Charts and insights for discovered patterns

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   React         │    │   FastAPI        │    │   AWS Services  │
│   Frontend      │◄──►│   Backend        │◄──►│   (S3 + Glue)   │
│                 │    │                  │    │                 │
│ - Upload UI     │    │ - File handling  │    │ - Data storage  │
│ - Visualization │    │ - Job management │    │ - Distributed   │
│ - Results       │    │ - Rule processing│    │   processing    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## 📁 Project Structure

```
fpinsight-pipeline/
├── backend/
│   ├── main.py                 # FastAPI application with endpoints
│   ├── local_fp.py            # Local FP-Growth processing using MLxtend
│   ├── aws_glue_trigger.py     # AWS Glue job triggering and S3 operations
│   ├── glue_fp_growth.py       # PySpark script for AWS Glue processing
│   ├── requirements.txt        # Python dependencies
│   └── Dockerfile             # Container configuration
├── frontend/
│   ├── src/
│   │   ├── App.jsx            # Main React application
│   │   ├── main.jsx           # React entry point
│   │   ├── api.js             # API client functions
│   │   ├── components/
│   │   │   └── RuleChart.jsx  # Chart components for visualization
│   │   └── pages/
│   │       ├── IntroPage.jsx      # Landing page
│   │       ├── UploadPage.jsx     # File upload interface
│   │       └── VisualizationPage.jsx # Results dashboard
│   ├── package.json           # Node.js dependencies
│   └── index.html            # HTML template
└── README.md                 # Project documentation
```

## 🛠️ Technology Stack

### Backend
- **FastAPI**: High-performance Python web framework
- **MLxtend**: Machine learning library for local FP-Growth implementation
- **PySpark**: Distributed computing framework for AWS Glue
- **Pandas**: Data manipulation and analysis
- **Boto3**: AWS SDK for Python
- **Scikit-learn**: Additional ML utilities

### Frontend
- **React 18**: Modern JavaScript UI library
- **Vite**: Fast build tool and development server
- **React Router**: Client-side routing
- **Chart.js + React-Chartjs-2**: Data visualization
- **Axios**: HTTP client for API communication

### Cloud Infrastructure
- **AWS S3**: Object storage for datasets and results
- **AWS Glue**: Managed ETL service for large-scale processing
- **Docker**: Containerization support

## 🚦 Getting Started

### Prerequisites

- Python 3.8+
- Node.js 16+
- AWS Account (for cloud processing)
- AWS CLI configured (optional)

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables:**
   ```bash
   export AWS_BUCKET_NAME="your-s3-bucket-name"
   export AWS_GLUE_JOB="your-glue-job-name"
   export AWS_ACCESS_KEY_ID="your-access-key"
   export AWS_SECRET_ACCESS_KEY="your-secret-key"
   export AWS_DEFAULT_REGION="your-region"
   ```

5. **Start the FastAPI server:**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start development server:**
   ```bash
   npm run dev
   ```

4. **Open your browser:**
   Navigate to `http://localhost:5173`

## 📊 Usage

### Data Format

The application expects CSV files with retail transaction data containing at least these columns:
- `InvoiceNo`: Transaction identifier
- `Description`: Product/item description

Example format:
```csv
InvoiceNo,Description,Quantity,InvoiceDate,UnitPrice,CustomerID,Country
536365,WHITE HANGING HEART T-LIGHT HOLDER,6,2010-12-01 08:26:00,2.55,17850,United Kingdom
536365,WHITE METAL LANTERN,6,2010-12-01 08:26:00,3.39,17850,United Kingdom
```

### Processing Workflow

1. **Upload Data**: Use the web interface to upload your CSV file
2. **Configure Parameters**:
   - **Min Support**: Minimum frequency for itemsets (default: 0.05)
   - **Min Confidence**: Minimum confidence for association rules (default: 0.5)
3. **Choose Processing Mode**:
   - **Local**: For smaller datasets (< 1GB)
   - **AWS Glue**: For larger datasets requiring distributed processing
4. **View Results**: Navigate to the visualization dashboard to explore discovered patterns

### API Endpoints

- `GET /`: Health check
- `POST /presign`: Get S3 presigned URL for file upload
- `POST /process/local`: Process dataset locally
- `POST /process/glue`: Process dataset using AWS Glue

## 🔧 Configuration

### AWS Glue Job Setup

To use the distributed processing feature, you'll need to create an AWS Glue job:

1. Upload `glue_fp_growth.py` to an S3 bucket
2. Create a new Glue job with the script location
3. Configure job parameters and IAM roles
4. Update the `AWS_GLUE_JOB` environment variable

### Docker Deployment

Build and run the backend container:
```bash
cd backend
docker build -t fpinsight-backend .
docker run -p 8000:8000 \
  -e AWS_BUCKET_NAME="your-bucket" \
  -e AWS_GLUE_JOB="your-job" \
  fpinsight-backend
```

## 📈 Output and Insights

The application generates association rules with the following metrics:

- **Support**: How frequently items appear together
- **Confidence**: Reliability of the inference
- **Lift**: How much more likely items are purchased together vs. independently
- **Conviction**: Measure of implication strength

Example output:
```json
{
  "antecedents": ["COFFEE"],
  "consequents": ["SUGAR"],
  "support": 0.15,
  "confidence": 0.75,
  "lift": 2.3,
  "conviction": 3.2
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [MLxtend](https://rasbt.github.io/mlxtend/) for the efficient FP-Growth implementation
- [Apache Spark](https://spark.apache.org/) for distributed computing capabilities
- The retail dataset format is inspired by the UCI Online Retail Dataset

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the existing issues in the GitHub repository
2. Create a new issue with detailed information about the problem
3. Include sample data and error logs when possible

---

**Built with ❤️ for retail analytics and market basket analysis**
